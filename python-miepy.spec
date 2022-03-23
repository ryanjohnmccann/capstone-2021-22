%define pkgname miepy
%define release 1
%define version 1
%global commit 4951d9e16fd85d197dee092b73cd9a763c7cc2ae
%global shortcommit 8d5f342

Summary: Solve Maxwell's equations for a cluster of particles using the generalized multiparticle Mie theory (GMMT)
Name: python-%{pkgname}
Version: %{version}
Release: %{release}
Source0: https://github.com/johnaparker/miepy/archive/%{commit}/%{pkgname}-%{shortcommit}.tar.gz
License: GPLv3
Group: Development/Libraries
Prefix: %{_prefix}
BuildArch: noarch
Url: https://github.com/johnaparker/miepy

%description
MiePy is a Python module for the generalized multiparticle Mie theory (GMMT), also known as the aggregate T-matrix method. MiePy solves the electrodynamics of a collection of spherical or non-spherical scatterers with an arbitrary incident source.

%prep
%autosetup -n %{pkgname}-%{commit}

%build
%py3_build

%install
%py3_install


%files 
%license LICENSE.md
%doc README.md
%{python3_sitelib}/*

%changelog
* Wed Mar 23 2022 Robert Santos <robert.santoshld2018@gmail.com> and Ali Dia <ali_dia@student.uml.edu>
* - First miepy package
