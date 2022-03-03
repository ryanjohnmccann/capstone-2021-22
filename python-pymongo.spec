%define name python-pymongo
%define version 4.0.1
%define release 1

Summary: Python driver for MongoDB
Name: %{name}
Version: %{version}
Release: %{release}
Source0: https://github.com/mongodb/mongo-python-driver/archive/%{version}/%{name}-%{version}.tar.gz
License: Apache License, Version 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: The MongoDB Python Team
Url: http://github.com/mongodb/mongo-python-driver

%description
The PyMongo distribution contains tools for interacting with MongoDB
database from Python.

%prep
%setup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.rst RELEASE.rst
%{python3_sitearch}/*

%changelog
* Mon Feb 7 2022 Ryan McCann <ryan_mccann@student.uml.edu> and Robert Moeller <robert_moeller@student.uml.edu>
- First pymongo package
