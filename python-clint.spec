# Created by pyp2rpm-3.3.2
%global pypi_name clint

Name:           python-%{pypi_name}
Version:        0.5.1
Release:        1%{?dist}
Summary:        Python Command Line Interface Tools

License:        ISC
URL:            https://github.com/kennethreitz/clint
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(args)
BuildRequires:  python3dist(setuptools)

%description
Clint: Python Command-line Application Tools **Clint** is a module filled with
a set of awesome tools for developing commandline applications. **C** ommand
**L** ine **IN** terface **T** oolsClint is awesome. Crazy awesome. It supports
colors, but detects if the session is a TTY, so doesn't render the colors if
you're piping stuff around. Automagically.Awesome nest-able indentation
context...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(args)
%description -n python3-%{pypi_name}
Clint: Python Command-line Application Tools **Clint** is a module filled with
a set of awesome tools for developing commandline applications. **C** ommand
**L** ine **IN** terface **T** oolsClint is awesome. Crazy awesome. It supports
colors, but detects if the session is a TTY, so doesn't render the colors if
you're piping stuff around. Automagically.Awesome nest-able indentation
context...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py3_install

%check
%{__python3} test_clint.py

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Mar 26 2019 Evan Klitzke <evan@eklitzke.org> - 0.5.1-1
- Initial package.
