Summary: Bootloader for EL-based distros that support Xen
Name: linux-guest-loader
Version: 2.3.1
Release: 1%{?dist}

Source0: https://code.citrite.net/rest/archive/latest/projects/XS/repos/linux-guest-loader/archive?at=v2.3.1&format=tar.gz&prefix=linux-guest-loader-2.3.1#/linux-guest-loader-2.3.1.tar.gz
Source1: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/el4.5-initrd-additions.cpio
Source2: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/el4.6-initrd-additions.cpio
Source3: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/el4.7-initrd-additions.cpio
Source4: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/el4.8-initrd-additions.cpio
Source5: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/el5.0-initrd-additions.cpio
Source6: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/el5.10-initrd-additions.cpio
Source7: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/el5.11-initrd-additions.cpio
Source8: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/el5.1-initrd-additions.cpio
Source9: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/el5.2-initrd-additions.cpio
Source10: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/el5.3-initrd-additions.cpio
Source11: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/el5.4-initrd-additions.cpio
Source12: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/el5.5-initrd-additions.cpio
Source13: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/el5.6-initrd-additions.cpio
Source14: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/el5.7-initrd-additions.cpio
Source15: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/el5.8-initrd-additions.cpio
Source16: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/el5.9-initrd-additions.cpio
Source17: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/el6.0-initrd-additions.cpio
Source18: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/el6.1-initrd-additions.cpio
Source19: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/el6-initrd-additions.cpio
Source20: https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions/ubuntu11.04-initrd-additions.cpio


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/linux-guest-loader/archive?at=v2.3.1&format=tar.gz&prefix=linux-guest-loader-2.3.1#/linux-guest-loader-2.3.1.tar.gz) = 6de142564e932fbb5e0e449f5c6bf8fdc9a98b00

%define initrd_url https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions
License: GPL
BuildArch: noarch

BuildRequires: python-devel python-setuptools
Requires: gzip
Requires: xz

%description
Bootloader for EL-based distros that support Xen.

%prep
%autosetup -p1

%build
%{__python} setup.py build

%define pkgdatadir /opt/xensource/packages/files/guest-installer

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --install-scripts /opt/xensource/libexec
mkdir -p %{buildroot}/usr/bin
ln -sf /opt/xensource/libexec/eliloader.py %{buildroot}/usr/bin/eliloader

install -d %{buildroot}%{pkgdatadir}
install -m 644 data/*.cpio.map %{buildroot}%{pkgdatadir}/
install -m 644 %{_sourcedir}/*-initrd-additions.cpio %{buildroot}%{pkgdatadir}/

%files
/opt/xensource/libexec/*
/usr/bin/eliloader
%dir %{pkgdatadir}
%exclude %{python_sitelib}/*-py*.egg-info


%package data
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/linux-guest-loader/archive?at=v2.3.1&format=tar.gz&prefix=linux-guest-loader-2.3.1#/linux-guest-loader-2.3.1.tar.gz) = 6de142564e932fbb5e0e449f5c6bf8fdc9a98b00
Summary: Data files for eliloader
Group: Applications/System

%description data
This package contains data files to enable installation of specific
Linux distros.

%files data
%{pkgdatadir}/*

%changelog
* Thu Feb 14 2019 Ross Lagerwall <ross.lagerwall@citrix.com> - 2.3.1-1
- CA-294507: add force/lazy flag to make umount more robust

* Tue Jan 15 2019 Yuan Ren <yuan.ren@citrix.com> - 2.3.0-1
- CP-28593: Add cpio mapping files for EL6.10 guests.

* Tue May 15 2018 Simon Rowe <simon.rowe@citrix.com> - 2.2.2-1
- CA-289156: Always give a proper Pygrub error when called
- Set more standard message, and set message as error message

* Mon Mar 26 2018 Simon Rowe <simon.rowe@citrix.com> - 2.2.1-1
- CP-27183: Add cpio mapping files for EL6.9 guests

* Fri Aug 18 2017 Deli Zhang <deli.zhang@citrix.com> - 2.2.0-1
- CP-22495: Add cpio mapping file for NeoKylin Linux Security OS 5.0 (Update8) x64

* Fri Jun 02 2017 Wei Xie <wei.xie@citrix.com> - v2.1.0-1
- Add cpio mapping file for Turbo Linux.
- CP-22350: Add cpio mapping file for Asianux Linux.

