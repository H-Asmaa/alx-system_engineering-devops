# A script that removes p from php in the wp-settings.php file that was causing 500 status-code.
exec { 'fixing-syntax':
  command => 'sed -i s/.phpp/.php/g /var/www/wp-settings.php',
  path    => ['/usr/bin', '/bin'],
}
