# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'terminate process':
  command => 'pkill killmenow',
  path    => '/usr/bin/',
}
