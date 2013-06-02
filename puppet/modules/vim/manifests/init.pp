class vim {
        package { "vim":
                ensure  => installed,
        }
        file { "/etc/alternatives/editor":
                ensure  => link,
                target  => "/usr/bin/vim",
                require => Package["vim"]
        }
        file { "/etc/alternatives/editor.1.gz":
                ensure  => link,
                target  => "/usr/share/man/man1/vim.1.gz",
                require => Package["vim"]
        }
}