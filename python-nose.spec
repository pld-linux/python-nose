%define		module	nose
Summary:	A unittest extension with automatic discovery, simplified authoring, and output capture
Summary(pl.UTF-8):	Rozszerzenie testów jednostkowych z automatycznym wykrywaniem, prostym tworzeniem i przechwytywaniem wyjścia
Name:		python-%{module}
Version:	1.0.0
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/n/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	47a4784c817afa6ef11a505b574584ed
URL:		http://pypi.python.org/pypi/nose
BuildRequires:	python-devel
BuildRequires:	python-devel-tools >= 1:2.5
BuildRequires:	python-setuptools >= 0.6-0.c5
BuildRequires:	python3-devel
BuildRequires:	python3-devel-tools >= 1:2.5
BuildRequires:	python3-distribute
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

%description -l pl.UTF-8
nose dostarcza alternatywny proces wykrywania i uruchamiania testów
dla testów jednostkowych (unittest), mający przypominać zachowanie
py.test na ile to możliwe bez uciekania się do magii. Domyślnie nose
uruchamia testy z tych plików lub katalogów od bieżącego katalogu,
których nazwa zawiera "test". Obsługuje także testy doctest i
opcjonalnie przedstawia raport pokrycia testów.

%package -n	python3-%{module}
Summary:	Serial port interface module
Version:	%{version}
Release:	%{release}
Group:		Libraries/Python

%description -n python3-%{module}
nose provides an alternate test discovery and running process for
unittest, one that is intended to mimic the behavior of py.test as
much as is reasonably possible without resorting to magic. By default,
nose will run tests in files or directories under the current working
directory whose names include "test". nose also supports doctest tests
and may optionally provide a test coverage report.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build --build-base py2
%{__python3} setup.py build --build-base py3

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py build \
	--build-base py2 \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%{__python3} setup.py build \
	--build-base py3 \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

mv $RPM_BUILD_ROOT%{_prefix}/man/ $RPM_BUILD_ROOT%{_datadir}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nosetests-2.7
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%{_mandir}/man1/*

%files -n python3-%{module}
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nosetests-3.2
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%{_mandir}/man1/*
