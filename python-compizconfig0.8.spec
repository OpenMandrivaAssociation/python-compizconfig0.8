Name:		compizconfig-python
Version:	0.8.16
Release:	1
Summary:	Python bindings for libcompizconfig
Group:		System/X11
License:	LGPLv2+
Url:		https://github.com/compiz-reloaded/compizconfig-python
Source0:	https://github.com/compiz-reloaded/compizconfig-python/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	python-devel
BuildRequires:	python-cython
BuildRequires:	pkgconfig(libcompizconfig)
BuildRequires:	pkgconfig(glib-2.0)
Requires:	compiz

%description
Python bindings for libcompizconfig

#----------------------------------------------------------------------------

%prep
%setup -q

# make autoreconf more happy
mkdir -p m4

%build
autoreconf -vfi

export PYTHON=%{__python}
%configure \
	--disable-static \
	--with-cython=cython-3
%make_build

%install
%make_install

# we don't want these
find %{buildroot} -name "*.la" -delete
rm -rf %{buildroot}%{_libdir}/pkgconfig/compizconfig-python.pc

%files
%doc COPYING NEWS
%{python_sitearch}/compizconfig.so
