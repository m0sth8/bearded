exec { 'apt-update':
  command => '/usr/bin/apt-get --list-cleanup update'
}

Exec {
  path => "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
}

# == packages ===

package { "tmux":
  ensure => "latest",
  require => Exec['apt-update'],
}

package { "mc":
  ensure => installed,
  require => Exec['apt-update'],
}

package { "sudo":
  ensure => installed,
  require => Exec['apt-update'],
}

include vim
include locale
include users::vagrant

include nodejs

# === database

include postgresql::devel

class { 'postgresql::server':
  require => Exec['apt-update'],
}

postgresql::pg_hba_rule { 'allow application network to access app database':
  description => "Open up postgresql for access from local",
  type => 'local',
  database => 'all',
  user => 'all',
  #  address => '127.0.0.1',
  auth_method => 'md5',
}

class create_bearded_db {
  postgresql::db { 'bearded':
    user     => 'bearded',
    password => 'dedreab'
}

}
class {'create_bearded_db':
  require => [Class['postgresql::server']]
}



# ===== python



include python::dev

class { "python::venv":
  owner => "vagrant",
  group => "vagrant",
  require => [Package[postgresql-server], Package[postgresql-devel]]
}

class { "python::gunicorn": owner => "vagrant", group => "vagrant" }



class virtualenv_bearded_web {
  python::venv::isolate { "/home/vagrant/venv/bearded_web":
    requirements => "/home/vagrant/sources/requirements.txt",
  }
  python::gunicorn::instance { "bearded_web":
    venv => "/home/vagrant/venv/bearded_web",
    src => "/home/vagrant/sources/bearded_web",
    django => true,
  # django_settings => "bearded_web.settings_vagrant",
  }
}

class {"virtualenv_bearded_web":
  require => [Class['python::venv'], Class['python::gunicorn'], Class['create_bearded_db']]
}

exec { 'sync_and_migrate':
  command => "/home/vagrant/venv/bearded_web/bin/python /home/vagrant/sources/bearded_web/manage.py syncdb --noinput --migrate",
  require => [Package[postgresql-server], Package[postgresql-devel], Class['virtualenv_bearded_web']]
}




# ==== nginx

class { 'nginx': }
nginx::resource::vhost { 'bearded_web.local':
  ensure   => present,
  listen_port => 80,
  proxy   =>  'http://unix:/var/run/gunicorn/bearded_web.sock'
}

# ===== pentest tools ====

#class pentest_tools{
#  include wpscan
#}
#
#class {'pentest_tools':
#  require => Exec['apt-update'],
#}
