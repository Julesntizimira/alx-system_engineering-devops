file_line{'alias name':
  path => '/etc/ssh/ssh_config',
  line => 'Host 54.90.32.25',
}
file_line{'host name':
  path => '/etc/ssh/ssh_config',
  line => '    HostName 54.90.32.25',
}
file_line{'user name':
  path => '/etc/ssh/ssh_config',
  line => '    User ubuntu',
}
file_line{'identity file':
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/school',
}
file_line{'Turn off passwd authantication':
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
}
