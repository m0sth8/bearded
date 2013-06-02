class wpscan {
    include wpscan::install

    git::repo{'repo_name':
        path   => '/home/vagrant/tools/wpscan',
        source => 'https://github.com/wpscanteam/wpscan.git',
        update => true,
    }
    exec {'install_bundler':
      command => 'gem install bundler',
      require => Class['wpscan::install']
    }

    exec {'wpscan_bundle_install':
      command => 'bundle install --without test development',
      cwd     => '/home/vagrant/tools/wpscan',
      require => Exec['install_bundler']
    }

    exec {'change_permission':
      command => 'chown -R vagrant:vagrant ./',
      cwd => '/home/vagrant/tools/wpscan',
      require => Exec['wpscan_bundle_install']
    }

}
