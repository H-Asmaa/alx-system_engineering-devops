# Puppet configuration script
file_line { 'PasswordAuthentification':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentification no',
  match  => '^#?PasswordAuthentification',
}
file_line { 'IdentityFile':
  ensure => present,
  path   => '/etc/ssh/ssh_config'
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#?IdentityFile',
}
