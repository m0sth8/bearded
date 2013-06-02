class users::vagrant {
        users::common { "users::common::vagrant":
                login   => "vagrant",
                name    => "vagrant",
                groups  => "sudo",
                require => Package["sudo"]
        }
}