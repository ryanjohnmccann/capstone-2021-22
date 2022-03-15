%define name python-numdifftools
%define version 0.9.40
%define unmangled_version 0.9.40
%define release 1

Summary: Solves automatic numerical differentiation problems in one or more variables.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: https://github.com/pbrod/numdifftools/archive/v%{version}/%{name}-%{version}.tar.gz 
License: BSD-3-Clause 
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Per A. Brodtkorb <per.andreas.brodtkorb@gmail.com>
Url: https://github.com/pbrod/numdifftools

%description

The numdifftools library is a suite of tools written in _Python to solve automatic numerical differentiation problems in one or more variables. Finite differences are used in an adaptive manner, coupled with a Richardson extrapolation methodology to provide a maximally accurate result. The user can configure many options like; changing the order of the method or the extrapolation, even allowing the user to specify whether complex-step, central, forward or backward differences are used.

%prep
%autosetup -n numdifftools-%{unmangled_version}

%build
%py3_build

%install
%py3_install

%files
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/*

%changelog
* Mon Feb 28 2022 Sage Lyon <sageclyon@gmail.com> 0.9.40-1
- Initial numdifftools package
