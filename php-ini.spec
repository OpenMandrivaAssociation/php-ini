%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	INI files for PHP
Name:		php-ini
Version:	5.5.6
Release:	5
Group:		Development/Other
Url:		http://www.php.net
License:	PHP License
Source0:	php.ini

%description
The php-ini package contains the ini file required for PHP.

%prep
%setup -c -T

install -m0644 %{SOURCE0} php.ini

# lib64 hack
perl -p -i -e "s|/usr/lib|%{_libdir}|" php.ini

%build

%install
install -d -m 755 %{buildroot}%{_sysconfdir}/php.d
install -d -m 755 %{buildroot}%{_libdir}/php/extensions
install -d -m 755 %{buildroot}%{_datadir}/php

install -m0644 php.ini %{buildroot}%{_sysconfdir}/php.ini
install -m0644 php.ini %{buildroot}%{_sysconfdir}/php-cgi-fcgi.ini

%files
%config(noreplace) %{_sysconfdir}/php.ini
%config(noreplace) %{_sysconfdir}/php-cgi-fcgi.ini
%dir %{_sysconfdir}/php.d
%dir %{_libdir}/php
%dir %{_libdir}/php/extensions
%dir %{_datadir}/php

