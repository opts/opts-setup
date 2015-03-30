Summary: Bootstrap the OPTS setup process.


Name: OPTS-bootstrap

Version: 1.2

Release: stable

License: 2-clause BSD-like license

Group: Applications/Internet

Source: yes.tar.gz

URL: http://my.oschina.net/doomred/blog/

Requires: epel-release git

Distribution: Centos/Redhat

Packager: Dye Jarhoo <gene0mega@zoho.com>



%description

otstrap for the OPTS-setup.
Install the 'epel-release' package to enable the access of nginx, php-xcache, etc.


%prep


%build



%install


%preun

%files

%post
git config --global user.email "webmaster@example.com"
git config --global user.name "SA"

