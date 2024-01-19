# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'kill killmenow':
  command => 'pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'pgrep -f killmenow',
}
