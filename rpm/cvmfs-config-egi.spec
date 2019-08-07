Summary: CernVM File System EGI Configuration and Public Keys
Name: cvmfs-config-egi
Version: 2.4
Release: 1%{?dist}
Source0: https://github.com/cvmfs/%{name}/archive/%{name}-%{version}.tar.gz

BuildArch: noarch
Group: Applications/System
License: BSD
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Provides: cvmfs-config = %{version}-%{release}
Obsoletes: cvmfs-keys < 1.6
Provides: cvmfs-keys = 1.7
Obsoletes: cvmfs-init-scripts < 1.0.21
Provides: cvmfs-init-scripts = 1.0.22
Obsoletes: cvmfs-config-default

%description
Default configuration parameters and public keys for CernVM-FS

%prep
%setup

%install
rm -rf $RPM_BUILD_ROOT
make install-redhat DESTDIR=$RPM_BUILD_ROOT

%files
%dir %{_sysconfdir}/cvmfs/keys/egi.eu
%{_sysconfdir}/cvmfs/keys/egi.eu/*
%config %{_sysconfdir}/cvmfs/default.d/*
%config %{_sysconfdir}/cvmfs/config.d/*

%changelog
* Wed Aug 07 2019 Dave Dykstra <dwd@fnal.gov> - 2.4-1
- Jump to version 2.4-1 to indicate parity with the current version of
  cvmfs-config-osg.
- Remove Conflicts with old cvmfs version (< 2.1.20).
- Add debian packaging, move redhat packaging to rpm directory.
- Change the server urls for the config-egi repository to use openhtc.io
  aliases when the proxy url can use DIRECT.
- Change the alias klei.nikhef.nl to cvmfs01.nikhef.nl.

* Sat Feb 11 2017 Dave Dykstra <dwd@fnal.gov> - 2.0-1
- Jump to version 2.0-1 to be greater than cvmfs-config-default versions.
- Add CVMFS_CONFIG_REPO_REQUIRED=yes to 60-egi.conf.  This is supported
  beginning in cvmfs-2.3.3.
- Add IHEP stratum one to config-egi.egi.eu.conf.

* Fri Jun 24 2016 Dave Dykstra <dwd@fnal.gov> - 1.1-1
- Add CVMFS_FALLBACK_PROXY to config-egi.egi.eu.conf.

* Fri Jun 10 2016 Dave Dykstra <dwd@fnal.gov> - 1.0-1
- initial creation, based on cvmfs-config-osg.spec
