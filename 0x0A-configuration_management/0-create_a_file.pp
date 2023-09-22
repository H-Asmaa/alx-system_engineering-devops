# Creation of a file with permissions
exec { 'fileCreation':
  command => '/bin/echo "I love Puppet" > /tmp/school',
}

exec { 'grantPermission':
  command => '/bin/chmod 744 /tmp/school',
  require => Exec['fileCreation'],
}

exec { 'ownerGroupSetUp':
  command => '/bin/chown www-data:www-data /tmp/school',
  require => Exec['grantPermission'],
}
