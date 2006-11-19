# $Revision: 1.4 $
%define		module	nose
Summary:	A unittest extension with automatic discovery, simplified authoring, and output capture
Summary(pl):	Rozszerzenie testów jednostkowych z automatycznym wykrywaniem, prostym tworzeniem i przechwytywaniem wyj±cia
Name:		python-%{module}
Version:	0.9.1
Release:	0.3
License:	LGPL
Group:		Libraries/Python
Source0:	http://somethingaboutorange.com/mrl/projects/nose/%{module}-%{version}.tar.gz
# Source0-md5:	97771e186ff3680e1abe5566a939966c
URL:		http://somethingaboutorange.com/mrl/projects/nose/
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-devel-tools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nose provides an alternate test discovery and running process for
unittest, one that is intended to mimic the behavior of py.test as
much as is reasonably possible without resorting to magic. By default,
nose will run tests in files or directories under the current working
directory whose names include "test". nose also supports doctest tests
and may optionally provide a test coverage report.

%description -l pl
nose dostarcza alternatywny proces wykrywania i uruchamiania testów
dla testów jednostkowych (unittest), maj±cy przypominaæ zachowanie
py.test na ile to mo¿liwe bez uciekania siê do magii. Domy¶lnie nose
uruchamia testy z tych plików lub katalogów od bie¿±cego katalogu,
których nazwa zawiera "test". Obs³uguje tak¿e testy doctest i
opcjonalnie przedstawia raport pokrycia testów.

%prep
%setup -qn %{module}-%{version}

%build
python setup.py build
	
%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nosetests
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
