# Using Puppet to create a manifest that kills a process
exec { 'kill-killmenow':
  path    => '/usr/bin',
  command => 'pkill killmenow',
}
