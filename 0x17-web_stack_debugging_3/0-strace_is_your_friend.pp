# A script that removes p from php in the wp-settings.php file that was causing 500 status-code.
exec { 'fixing-syntax':
  command => 'sudo /usr/bin/sed -i s/.phpp/.php/g /var/www/wp-settings.php',
}
