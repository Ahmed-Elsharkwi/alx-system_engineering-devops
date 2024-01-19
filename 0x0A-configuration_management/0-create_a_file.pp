# create a file in /tmp
file { 'name':
  path    => '/tmp/school',
  mode    => '0644',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
