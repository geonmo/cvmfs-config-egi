#!/usr/bin/make -f

# This make file takes care of installing files

all: # nothing to build

# default install target is debian because that's the easist way to
#   set up the 'rules' file.
install: install-debian

install-common:
	mkdir -p $(DESTDIR)/etc/cvmfs/default.d \
	  $(DESTDIR)/etc/cvmfs/config.d \
	  $(DESTDIR)/etc/cvmfs/keys/egi.eu
	install -D -m 444 60-egi.conf $(DESTDIR)/etc/cvmfs/default.d
	install -D -m 444 config-egi.egi.eu.conf $(DESTDIR)/etc/cvmfs/config.d
	install -D -m 444 egi.eu.pub $(DESTDIR)/etc/cvmfs/keys/egi.eu

install-debian: install-common

# assume DESTDIR=$RPM_BUILD_ROOT is passed in
install-redhat: install-common
