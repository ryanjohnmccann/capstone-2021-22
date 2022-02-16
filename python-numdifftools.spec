%define name python-numdifftools
%define version 0.9.4
%define unmangled_version 0.9.4
%define release 1

Summary: Solves automatic numerical differentiation problems in one or more variables.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: https://github.com/pbrod/numdifftools/archive/v%{version}/%{name}-%{version}.tar.gz 
License: new BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Per A. Brodtkorb <per.andreas.brodtkorb@gmail.com>
Url: https://github.com/pbrod/numdifftools

%description

The numdifftools library is a suite of tools written in _Python to solve automatic numerical differentiation problems in one or more variables. Finite differences are used in an adaptive manner, coupled with a Richardson extrapolation methodology to provide a maximally accurate result. The user can configure many options like; changing the order of the method or the extrapolation, even allowing the user to specify whether complex-step, central, forward or backward differences are used.

The methods provided are:

    - Derivative: Compute the derivatives of order 1 through 10 on any scalar function.
    - directionaldiff: Compute directional derivative of a function of n variables
    - Gradient: Compute the gradient vector of a scalar function of one or more variables.
    - Jacobian: Compute the Jacobian matrix of a vector valued function of one or more variables.
    - Hessian: Compute the Hessian matrix of all 2nd partial derivatives of a scalar function of one or more variables.
    - Hessdiag: Compute only the diagonal elements of the Hessian matrix

All of these methods also produce error estimates on the result.

Numdifftools also provide an easy to use interface to derivatives calculated with in _AlgoPy. Algopy stands for Algorithmic Differentiation in Python. The purpose of AlgoPy is the evaluation of higher-order derivatives in the forward and reverse mode of Algorithmic Differentiation (AD) of functions that are implemented as Python programs.

%prep
%setup -n numdifftools-%{unmangled_version}

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT


%files -f INSTALLED_FILES
%defattr(-,root,root)
