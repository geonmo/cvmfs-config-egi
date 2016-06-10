Summary: CernVM File System EGI Configuration and Public Keys
Name: cvmfs-config-egi
Version: 1.0
Release: 1%{?dist}
Source0: %{name}-%{version}.tgz

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

Conflicts: cvmfs < 2.2.0
Conflicts: cvmfs-server < 2.2.0

%description
Default configuration parameters and public keys for CernVM-FS

%prep
%setup

%install
rm -rf $RPM_BUILD_ROOT
for cvmfsdir in keys/egi.eu config.d default.d; do
    mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/cvmfs/$cvmfsdir
done
for key in egi.eu.pub; do
    install -D -m 444 "${key}" $RPM_BUILD_ROOT%{_sysconfdir}/cvmfs/keys/egi.eu
done
for defaultconf in 60-egi.conf; do
    install -D -m 444 "${defaultconf}" $RPM_BUILD_ROOT%{_sysconfdir}/cvmfs/default.d
done
for conf in config-egi.egi.eu.conf; do
    install -D -m 444 "${conf}" $RPM_BUILD_ROOT%{_sysconfdir}/cvmfs/config.d
done

%files
%dir %{_sysconfdir}/cvmfs/keys/egi.eu
%{_sysconfdir}/cvmfs/keys/egi.eu/*
%config %{_sysconfdir}/cvmfs/default.d/*
%config %{_sysconfdir}/cvmfs/config.d/*

%changelog
* Fri Jun 10 2016 Dave Dykstra <dwd@fnal.gov> - 1.0-1
- initial creation, based on cvmfs-config-osg.spec
