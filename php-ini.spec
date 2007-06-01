%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	INI files for PHP
Name:		php-ini
Version:	5.2.3
Release:	%mkrel 1
Group:		Development/Other
URL:		http://www.php.net
License:	PHP License
Source0:	php.ini
Requires(post):	ccp >= 0.4.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The php-ini package contains the ini file required for PHP.

%prep

%setup -c -T

install -m0644 %{SOURCE0} php.ini

# lib64 hack
perl -p -i -e "s|/usr/lib|%{_libdir}|" php.ini

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/php.d
install -d %{buildroot}%{_libdir}/php/extensions

install -m0644 php.ini %{buildroot}%{_sysconfdir}/php.ini

%post
# Upgrade the configuration file using ccp if needed
# More information in ccp(1)
ccp --backup --delete --ifexist --set NoOrphans --type ini --oldfile %{_sysconfdir}/php.ini --newfile %{_sysconfdir}/php.ini.rpmnew

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.ini
%dir %{_sysconfdir}/php.d
%dir %{_libdir}/php
%dir %{_libdir}/php/extensions
