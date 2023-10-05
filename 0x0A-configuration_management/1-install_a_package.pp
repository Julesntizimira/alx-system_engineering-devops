# installs puppet-lint package

package {'flask':
  ensure   => '2.3.3',
  name     => 'flask',
  provider => 'pip3'
}
