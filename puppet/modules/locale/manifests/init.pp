class locale {
        package { "locales":
                ensure  => installed,
        }
        file { "/etc/default/locale":
                ensure  => file,
                owner   => root,
                group   => root,
                mode    => 644,
                replace => yes,
                backup  => false,
                content => "LANG=ru_RU.UTF-8\n"
        }
}