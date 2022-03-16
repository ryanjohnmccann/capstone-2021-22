%define name python-miepy
%define version 0.4
%define unmangled_version 0.4
%define release 1

Summary: Solve Maxwell's equations for a cluster of particles using the generalized multiparticle Mie theory (GMMT)
Name: %{name}
Version: %{version}
Release: %{release}
Source0: https://github.com/johnaparker/miepy/archive/%{version}/%{name}-%{version}.tar.gz
License: GPLv3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: John Parker <japarker@uchicago.edu>
Url: https://github.com/johnaparker/miepy


%description
MiePy is a Python module for the generalized multiparticle Mie theory (GMMT), also known as the aggregate T-matrix method. MiePy solves the electrodynamics of a collection of spherical or non-spherical scatterers with an arbitrary incident source.

%prep
%setup -n %{name}-%{version} 

%build
%py3_build

%install
%py3_install

%files 
%license LICENSE
%doc README
%{python3_sitearch}/*

%changelog
* Tue Mar 15 2022 Robert Santos <robert.santoshld2018@gmail.com> and Ali Dia <ali_dia@student.uml.edu>
- First miepy package
