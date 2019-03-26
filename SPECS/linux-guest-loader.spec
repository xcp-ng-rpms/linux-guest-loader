Summary: Bootloader for EL-based distros that support Xen
Name: linux-guest-loader
Version: 2.2.2
Release: 1%{dist}
Source: https://code.citrite.net/rest/archive/latest/projects/XS/repos/%{name}/archive?at=v%{version}&format=tar.gz&prefix=%{name}-%{version}#/%{name}-%{version}.tar.gz
%define initrd_url https://repo.citrite.net/xs-local-contrib/citrix/xenserver/initrd-additions
Source1: %{initrd_url}/el4.5-initrd-additions.cpio
Source2: %{initrd_url}/el4.6-initrd-additions.cpio
Source3: %{initrd_url}/el4.7-initrd-additions.cpio
Source4: %{initrd_url}/el4.8-initrd-additions.cpio
Source5: %{initrd_url}/el5.0-initrd-additions.cpio
Source6: %{initrd_url}/el5.10-initrd-additions.cpio
Source7: %{initrd_url}/el5.11-initrd-additions.cpio
Source8: %{initrd_url}/el5.1-initrd-additions.cpio
Source9: %{initrd_url}/el5.2-initrd-additions.cpio
Source10: %{initrd_url}/el5.3-initrd-additions.cpio
Source11: %{initrd_url}/el5.4-initrd-additions.cpio
Source12: %{initrd_url}/el5.5-initrd-additions.cpio
Source13: %{initrd_url}/el5.6-initrd-additions.cpio
Source14: %{initrd_url}/el5.7-initrd-additions.cpio
Source15: %{initrd_url}/el5.8-initrd-additions.cpio
Source16: %{initrd_url}/el5.9-initrd-additions.cpio
Source17: %{initrd_url}/el6.0-initrd-additions.cpio
Source18: %{initrd_url}/el6.1-initrd-additions.cpio
Source19: %{initrd_url}/el6-initrd-additions.cpio
Source20: %{initrd_url}/ubuntu11.04-initrd-additions.cpio
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
Summary: Data files for eliloader
Group: Applications/System

%description data
This package contains data files to enable installation of specific
Linux distros.

%files data
%{pkgdatadir}/*

%changelog
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

