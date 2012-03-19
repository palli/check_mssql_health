%define debug_package %{nil}

Summary:	Nagios plugins to check the status of MS-SQL Servers
Name:		nagios-plugins-mssql
Version:	1.5.9.2
Release:	7%{?dist}
License:	GPLv2+
Group:		Applications/System
URL:		http://labs.consol.de/lang/en/nagios/check_mssql_health/
#Source1:	http://labs.consol.de/download/shinken-nagios-plugins/check_mssql_health-%{version}.tar.gz
Source0:	http://labs.consol.de/download/shinken-nagios-plugins/nagios-plugins-mssql-%{version}.tar.gz
Requires:	perl-Nagios-Plugin
Requires:	perl-DBD-Sybase
BuildRequires:	automake
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
check_mssql_health is a plugin, which is used to monitor different parameters of a MS SQL server.

%prep
%setup -T -b0 

%build
aclocal
autoconf
automake
./configure --libexecdir=%{_libdir}/nagios/plugins/ --libdir=%{_libdir}
make 


%install
make install DESTDIR="%{buildroot}"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README COPYING
%{_libdir}/nagios/plugins/check_mssql_health

%changelog
* Mon Mar 19 2012 Pall Sigurdsson <palli@opensource.is> 1.5.9.2-7
- new package built with tito

* Mon Mar 19 2012 Pall Sigurdsson <palli@opensource.is> 1.5.9.2-6
- test (palli@opensource.is)
- test (palli@opensource.is)

* Mon Mar 19 2012 Pall Sigurdsson <palli@opensource.is> 1.5.9.2-5
- Source1 commented 

* Mon Mar 19 2012 Pall Sigurdsson <palli@opensource.is> 1.5.9.2-4
- test (palli@opensource.is)

* Mon Mar 19 2012 Pall Sigurdsson <palli@opensource.is> 1.5.9.2-3
- test (palli@opensource.is)

* Mon Mar 19 2012 Pall Sigurdsson <palli@opensource.is> 1.5.9.2-2
- new package built with tito

* Mon Mar 19 2012 Pall Sigurdsson <palli@opensource.is> 0.0.6-1
- new package built with tito

* Mon Mar 12 2012 Pall Sigurdsson <palli@opensource.is> 0.0.4-1
- new package built with tito

* Sun Nov 21 2010  Tomas Edwardsson <tommi@opensource.is> 0.0.3-1
- Initial packaging
