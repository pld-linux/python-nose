# $Revision: 1.2 $
%define     module  nose
%define     python_version 2.4
Summary:	A unittest extension offering automatic test suite discovery, simplified test authoring, and output capture
Name:		python-%{module}
Version:	0.9.1
Release:	0.2
License:	LGPL
Group:		Libraries
Source0:    http://somethingaboutorange.com/mrl/projects/%{module}/%{module}-%{version}.tar.gz
URL:		http://somethingaboutorange.com/mrl/projects/nose/
Requires:   python >= %{python_version}
BuildArch:  noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nose provides an alternate test discovery and running process for unittest,
one that is intended to mimic the behavior of py.test as much as is reasonably
possible without resorting to magic. By default, nose will run tests in files
or directories under the current working directory whose names include "test".
nose also supports doctest tests and may optionally provide a test coverage
report.

%prep
%setup -qn %{module}-%{version}

%build
python setup.py build
	
%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2
	
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/%{module}
%attr(755,root,root) %{_bindir}/nosetests
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py%{python_version}.egg-info
