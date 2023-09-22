# Killing a process named killmenow.
exec { 'killMeNow':
  command => 'pkill -f killmenow'
}
