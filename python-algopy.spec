%define name python-algopy
%define version 0.5.7
%define release 1
%global commit 1e2430f803289bbaed6bbdff6c28f98d7767835c
%global shortcommit 1e2430f

Summary: ALGOPY: Taylor Arithmetic Computation and Algorithmic Differentiation
Name: %{name}
Version: %{version}
Release: %{release}
Source0: https://github.com/b45ch1/algopy/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
License: BSD-2-Clause
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Sebastian F. Walter <sebastian.walter@gmail.com>
Url: http://packages.python.org/algopy

%description
ALGOPY is a tool for Algorithmic Differentiation (AD) and Taylor polynomial approximations.
ALGOPY makes it possible to perform computations on scalar and polynomial matrices.
It is designed to be as compatible to numpy as possible. I.e. views, broadcasting and most
functions of numpy can be performed on polynomial matrices. Exampels are dot,trace,qr,solve,
inv,eigh.
The reverse mode of AD is also supported by a simple code evaluation tracer.

Documentation with examples is available at http://packages.python.org/algopy/.

%prep
%setup -n algopy-%{commit}

%build
%py3_build

%install
%py3_install

%files
%doc README.rst
%{python3_sitelib}/*

%defattr(-,root,root)

%changelog
* Mon Mar 15 2022 Sage Lyon <sage_lyon@student.uml.edu> 0.5.7
- Initial algopy package
