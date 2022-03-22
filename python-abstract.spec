%define pkgname abstract
%define release 1
%define version 1
%global commit 7c948af70282f0bae031a7f82ef33502e8e41754
%global shortcommit 7c948af

Summary: Python library for creating and drawing graphs and taking advantage of graph properties
Name: python-%{pkgname}
Version: %{version}
Release: %{release}
Source0: https://github.com/idin/abstract/archive/%{commit}/%{pkgname}-%{shortcommit}.tar.gz
License: MIT
Prefix: %{_prefix}
BuildArch: noarch
Url: https://github.com/idin/abstract

%description
Abstract is a Python library for creating and drawing graphs 
and taking advantage of graph properties.

%prep
%autosetup -n %{pkgname}-%{commit}

%build
%py3_build

%install
%py3_install


%files
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%changelog
* Sat Feb 26 2022 Robert Santos <robert.santoshld2018@gmail.com> and Ali Dia <ali_dia@student.uml.edu>
* - First abstract package
