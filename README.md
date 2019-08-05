# cvmfs-config-egi

## CVMFS configuration package for the European Grid Infrastructure (EGI)

This is the source for the CernVM File System (CVMFS) configuration
files for the European Grid Infrastructure (EGI).  It includes packaging
for Redhat and Debian.

### Redhat

End-user documentation for Redhat systems can be found
[here](https://github.com/cvmfs-contrib/egi-cvmfs/).

### Debian

For Debian, the End-user instructions are to install this package from
[cvmfs-contrib](https://cvmfs-contrib.github.io) and cvmfs from
[the cvmfs download page](https://cernvm.cern.ch/portal/filesystem/downloads).
Then if you want to enable autofs, add the following contents
into /etc/auto.master.d/cvmfs.autofs:
```
/cvmfs /etc/auto.cvmfs
```
and restart autofs with
```
systemctl restart autofs
```
