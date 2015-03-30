Summary: Setup OPTS system

Name: OPTS-setup

Version: 1.1

Release: beta

License: 2-clause BSD-like license

Group: Applications/Internet

Source: etc.tar.gz
Source1: srv.tar.gz
Source2: usr.tar.gz

URL: http://my.oschina.net/doomred/blog/

Requires: ImageMagick cjkuni-fonts-ghostscript ghostscript git mysql mysql-server nginx openldap-servers openssl php php-fpm php-gd php-intl php-mcrypt php-mysql php-pecl-imagick php-xcache sudo

Distribution: Centos/Redhat

Packager: Dye Jarhoo <gene0mega@zoho.com>



%description

Don't panic. It's the truth that setup a CMS system is no longer a hard work.


%prep
# I don't trust `setup -q` anymore...
cd %{_builddir}
tar -xf %{_sourcedir}/etc.tar.gz
tar -xf %{_sourcedir}/srv.tar.gz
tar -xf %{_sourcedir}/usr.tar.gz



%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin
cp -p %{_builddir}/usr/local/bin/* %{buildroot}/usr/local/bin/

mkdir -p %{buildroot}/srv
cp -pr %{_builddir}/srv/* %{buildroot}/srv/

mkdir -p %{buildroot}/etc/nginx/conf.d

mkdir -p %{buildroot}/etc/php-fpm.d
cp -pr %{_builddir}/etc/* %{buildroot}/etc/


%preun
%files
%defattr(644,root, root, 755)
/etc/crontab
/etc/nginx/conf.d/default.conf
/etc/nginx/nginx.conf
/etc/nginx/default.conf
/etc/nginx/fastcgi_params
/etc/php-fpm.conf
/etc/php-fpm.d/www.conf
/etc/php.ini
/etc/ssh/sshd_config
/etc/sudoers
/etc/sysctl.conf
/usr
/usr/local
/usr/local/bin
/usr/local/bin/bakcache.sh
/usr/local/bin/baketc.sh
/usr/local/bin/bakwww.sh
/usr/local/bin/grant
/usr/local/bin/revoke
/srv/*




%post
echo 'SELINUX=disabled' >>/etc/sysconfig/selinux
echo 'SELINUXTYPE=targeted' >>/etc/sysconfig/seliux
rm -rf /var/www
ln -s /srv/www /var/www

groupadd sftp
groupadd sa
useradd -m sa -G wheel -g sa
echo 321321a | passwd --stdin sa
chown -R apache:apache /srv/www
chown -R root:root /srv/sftp
chmod 1755 /srv/sftp
chkconfig php-fpm on
chkconfig nginx on

pushd /etc
git add .
git commit -m 'OPTS-setup installed'
popd

