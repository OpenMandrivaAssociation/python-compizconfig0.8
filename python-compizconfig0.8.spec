Name:		compizconfig-python
Version:	0.8.16
Release:	%mkrel 4
Summary:	Python bindings for libcompizconfig
Group:		System/X11
License:	LGPLv2+
Url:		https://github.com/compiz-reloaded/compizconfig-python
Source0:	https://github.com/compiz-reloaded/compizconfig-python/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	python3-devel
BuildRequires:	python3-cython
BuildRequires:	libcompizconfig-devel
BuildRequires:	pkgconfig(glib-2.0)
Requires:	compiz >= 1:0.8.16
Obsoletes:	%{_lib}compizconfig-python < 0.9.13.1-7

%description
Python bindings for libcompizconfig

#----------------------------------------------------------------------------

%prep
%setup -q

# make autoreconf more happy
mkdir -p m4

%build
autoreconf -vfi

export PYTHON=%{__python3}
%configure2_5x \
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
%{python3_sitearch}/compizconfig.so
