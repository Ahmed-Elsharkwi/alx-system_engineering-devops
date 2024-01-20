# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'install flask':
  command => 'pip3 install flask==2.1.0',
  path    => '/usr/bin/',
}
