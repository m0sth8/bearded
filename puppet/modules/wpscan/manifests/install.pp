
class wpscan::install{
    package {'ruby1.9.1':
      ensure => latest,
    }
    package {'ruby1.9.1-dev':
      ensure => latest,
    }
    package {'rubygems1.9.1':
      ensure => latest,
    }
    package {'libcurl4-gnutls-dev':
      ensure => installed,
    }
    package {'libruby1.9.1':
      ensure => installed,
    }
    package {'libxml2':
      ensure => installed,
    }
    package {'libxml2-dev':
      ensure => installed,
    }
    package {'libxslt1-dev':
      ensure => installed,
    }
    package {'make': ensure => installed}

}