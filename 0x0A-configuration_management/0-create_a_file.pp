exec { 'fileCreation':
  command => 'echo "I love Puppet" > /tmp/school'
}
exec { 'grantPermission':
  command => 'chmod 744 school'
  require => Exec['fileCreation']
}
exec { 'ownerGroupSetUp':
  command => 'chown www-data:www-data school /tmp/school'
  require => Exec['grantPermission']
}
