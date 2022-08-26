%global package_speccommit 58133bcf34bf1e191519cf2d13e2125abba42b90
%global package_srccommit v2.3.1
Summary: Bootloader for EL-based distros that support Xen
Name: linux-guest-loader
Version: 2.3.1
Release: 1%{?xsrel}%{?dist}
Source0: linux-guest-loader-2.3.1.tar.gz
%define initrd_url https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions
Source1: el4.5-initrd-additions.cpio
Source2: el4.6-initrd-additions.cpio
Source3: el4.7-initrd-additions.cpio
Source4: el4.8-initrd-additions.cpio
Source5: el5.0-initrd-additions.cpio
Source6: el5.10-initrd-additions.cpio
Source7: el5.11-initrd-additions.cpio
Source8: el5.1-initrd-additions.cpio
Source9: el5.2-initrd-additions.cpio
Source10: el5.3-initrd-additions.cpio
Source11: el5.4-initrd-additions.cpio
Source12: el5.5-initrd-additions.cpio
Source13: el5.6-initrd-additions.cpio
Source14: el5.7-initrd-additions.cpio
Source15: el5.8-initrd-additions.cpio
Source16: el5.9-initrd-additions.cpio
Source17: el6.0-initrd-additions.cpio
Source18: el6.1-initrd-additions.cpio
Source19: el6-initrd-additions.cpio
Source20: ubuntu11.04-initrd-additions.cpio
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
%{__python2} setup.py build

%define pkgdatadir /opt/xensource/packages/files/guest-installer

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot} --install-scripts /opt/xensource/libexec
mkdir -p %{buildroot}/usr/bin
ln -sf /opt/xensource/libexec/eliloader.py %{buildroot}/usr/bin/eliloader

install -d %{buildroot}%{pkgdatadir}
install -m 644 data/*.cpio.map %{buildroot}%{pkgdatadir}/
install -m 644 %{_sourcedir}/*-initrd-additions.cpio %{buildroot}%{pkgdatadir}/

%files
/opt/xensource/libexec/*
/usr/bin/eliloader
%dir %{pkgdatadir}
%exclude %{python2_sitelib}/*-py*.egg-info


%package data
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

