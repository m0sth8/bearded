define users::common ($login, $name, $email = "", $groups, $password = "*")
{
        user { "${login}":
                ensure     => present,
                comment    => "${name}",
                home       => "/home/${login}",
                managehome => true,
                shell      => "/bin/bash",
#                groups     => $groups,
                password   => "${password}"
        }
        file { "/home/${login}/.ssh":
                ensure  => directory,
                owner   => "${login}",
                group   => "${login}",
                mode    => 700,
                replace => yes,
                backup  => false,
                require => User["${login}"]
        }
#        file { "/home/${login}/.ssh/authorized_keys":
#                ensure  => file,
#                owner   => "${login}",
#                group   => "${login}",
#                mode    => 644,
#                replace => yes,
#                backup  => false,
#                source  => "puppet:///modules/users/${login}.id_rsa.pub",
#                require => File["/home/${login}/.ssh"]
#        }
        file { "/home/${login}/.tmux.conf":
                ensure  => file,
                owner   => "${login}",
                group   => "${login}",
                mode    => 644,
                replace => yes,
                backup  => false,
                source  => "puppet:///modules/users/tmux.conf",
                require => User["${login}"]
        }
        file { "/home/${login}/.bash_aliases":
                ensure  => file,
                owner   => "${login}",
                group   => "${login}",
                mode    => 644,
                replace => yes,
                backup  => false,
                source  => "puppet:///modules/users/bash_aliases",
                require => User["${login}"]
        }
        file { "/home/${login}/.inputrc":
                ensure  => file,
                owner   => "${login}",
                group   => "${login}",
                mode    => 644,
                replace => yes,
                backup  => false,
                source  => "puppet:///modules/users/inputrc",
                require => User["${login}"]
        }
        file { "/home/${login}/.bash_logout":
                ensure  => file,
                owner   => "${login}",
                group   => "${login}",
                mode    => 644,
                replace => yes,
                backup  => false,
                source  => "puppet:///modules/users/bash_logout",
                require => User["${login}"]
        }
        if $email {
                file { "/home/${login}/.gitconfig":
                        ensure  => file,
                        owner   => "${login}",
                        group   => "${login}",
                        mode    => 644,
                        replace => yes,
                        backup  => false,
                        content => template("users/gitconfig.erb"),
                        require => User["${login}"]
                }
        }
}