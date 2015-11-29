%define		module	nose
Summary:	A unittest extension with automatic discovery, simplified authoring, and output capture
Summary(pl.UTF-8):	Rozszerzenie testów jednostkowych z automatycznym wykrywaniem, prostym tworzeniem i przechwytywaniem wyjścia
Name:		python-%{module}
Version:	1.3.6
Release:	4
License:	LGPL v2.1
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/n/nose/%{module}-%{version}.tar.gz
# Source0-md5:	0ca546d81ca8309080fc80cb389e7a16
URL:		https://pypi.python.org/pypi/nose
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-devel-tools >= 1:2.5
BuildRequires:	python-setuptools >= 0.6-0.c5
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	rpm-pythonprov
Requires:	python-devel-tools >= 1:2.5
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

%package -n python3-%{module}
Summary:	A unittest extension with automatic discovery, simplified authoring, and output capture
Summary(pl.UTF-8):	Rozszerzenie testów jednostkowych z automatycznym wykrywaniem, prostym tworzeniem i przechwytywaniem wyjścia
Group:		Libraries/Python
Requires:	python3-devel-tools

%description -n python3-%{module}
nose provides an alternate test discovery and running process for
unittest, one that is intended to mimic the behavior of py.test as
much as is reasonably possible without resorting to magic. By default,
nose will run tests in files or directories under the current working
directory whose names include "test". nose also supports doctest tests
and may optionally provide a test coverage report.

%description -n python3-%{module} -l pl.UTF-8
nose dostarcza alternatywny proces wykrywania i uruchamiania testów
dla testów jednostkowych (unittest), mający przypominać zachowanie
py.test na ile to możliwe bez uciekania się do magii. Domyślnie nose
uruchamia testy z tych plików lub katalogów od bieżącego katalogu,
których nazwa zawiera "test". Obsługuje także testy doctest i
opcjonalnie przedstawia raport pokrycia testów.

%define	_duplicate_files_terminate_build	0

%prep
%setup -qn %{module}-%{version}

%build
%py_build --build-base py2
%py3_build --build-base py3

%install
rm -rf $RPM_BUILD_ROOT

%py_build \
	--build-base py2 \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py3_build \
	--build-base py3 \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}
for v in %{py_ver} %{py3_ver} ; do
	cp -p $RPM_BUILD_ROOT%{_mandir}/man1/nosetests.1 $RPM_BUILD_ROOT%{_mandir}/man1/nosetests-${v}.1
done

# default to python2 for now
ln -sf nosetests-%{py_ver} $RPM_BUILD_ROOT%{_bindir}/nosetests
echo '.so nosetests-%{py_ver}.1' > $RPM_BUILD_ROOT%{_mandir}/man1/nosetests.1

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG NEWS README.txt
%attr(755,root,root) %{_bindir}/nosetests-%{py_ver}
%attr(755,root,root) %{_bindir}/nosetests
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%{_mandir}/man1/nosetests-%{py_ver}.1*
%{_mandir}/man1/nosetests.1*

%files -n python3-%{module}
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nosetests-%{py3_ver}
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%{_mandir}/man1/nosetests-%{py3_ver}.1*
