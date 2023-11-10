# A script that removes p from php in the wp-settings.php file that was causing 500 status-code.
$file_to_edit = '/var/www/html/wp-settings.php'
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
