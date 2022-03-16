%define name python-pikepdf
%define version 5.0.1
%define unmangled_version 5.0.1
%define release 1

Summary: Read and write PDFs with Python, powered by qpdf
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: MPL-2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: James R. Barlow <james@purplerock.ca>
Url: https://github.com/pikepdf/pikepdf

%description
pikepdf
=======

**pikepdf** is a Python library for reading and writing PDF files.

[![Build Status](https://github.com/pikepdf/pikepdf/actions/workflows/build_wheels.yml/badge.svg)](https://github.com/pikepdf/pikepdf/actions/workflows/build_wheels.yml) [![PyPI](https://img.shields.io/pypi/v/pikepdf.svg)](https://pypi.org/project/pikepdf/) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pikepdf) ![PyPy](https://img.shields.io/badge/PyPy-3.7-blue) [![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/pikepdf/pikepdf.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/pikepdf/pikepdf/context:python) [![Language grade: C/C++](https://img.shields.io/lgtm/grade/cpp/g/pikepdf/pikepdf.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/pikepdf/pikepdf/context:cpp) ![PyPI - License](https://img.shields.io/pypi/l/pikepdf) ![PyPI - Downloads](https://img.shields.io/pypi/dm/pikepdf)  [![codecov](https://codecov.io/gh/pikepdf/pikepdf/branch/master/graph/badge.svg?token=8FJ755317J)](https://codecov.io/gh/pikepdf/pikepdf)

pikepdf is based on [QPDF](https://github.com/qpdf/qpdf), a powerful PDF manipulation and repair library.

Python + QPDF = "py" + "qpdf" = "pyqpdf", which looks like a dyslexia test. Say it out loud, and it sounds like "pikepdf".

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Sat Mar 12 2022 Robert Santos <robert.santoshld2018@gmail.com> and Ali Dia <ali_dia@student.uml.edu>
* -First pikepdf package
