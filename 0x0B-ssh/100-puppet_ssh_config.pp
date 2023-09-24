# Puppet configuration script
file_line { '/etc/ssh/ssh_config':
  ensure => present,
  line   => 'PasswordAuthentification no',
  match  => '^#?PasswordAuthentification'
  mode   => '0600'
}
file_line { '~/.ssh/school':
  ensure => present,
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#?IdentityFile'
}
