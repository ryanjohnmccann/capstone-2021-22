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
cd ~/rpmbuild/SOURCES/
tar -xzvf %{name}-%{version}.tar.gz
mv mongo-python-driver-%{version} %{name}-%{version}
rm %{name}-%{version}.tar.gz
tar -czvf %{name}-%{version}.tar.gz %{name}-%{version}

%setup

%build
env CFLAGS="$RPM_OPT_FLAGS" python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES

%defattr(-,root,root)

%changelog
* Mon Feb 7 2022 Ryan McCann <ryan_mccann@student.uml.edu> and Robert Moeller <robert_moeller@student.uml.edu>
- First pymongo package
