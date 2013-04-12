%define __noautoprov 'pkgconfig(.*)'
%define __noautoreq 'pkgconfig\\(libcompizconfig\\)'

%define shortname compizconfig
%define oname compizconfig-python
%define oversion 0.8

%define git 20130330

%if  %{git}
%define srcname %{oname}-compiz-%{oversion}.tar.bz2
%define distname %{oname}-compiz-%{oversion}
%define rel 0.%{git}.1
%else
%define srcname %{oname}-%{version}.tar.bz2
%define distname %{oname}-%{version}
%define rel 1
%endif

Name:		python-%{shortname}%{oversion}
Version:	0.8.5
Release:	%{rel}
Summary:	Python bindings for libcompizconfig
Group:		System/X11
License:	GPL
URL:		http://www.compiz.org/
Source:		http://cgit.compiz.org/compiz/%{shortname}/%{oname}/snapshot/%{srcname}
BuildRequires:	compiz0.8-devel
BuildRequires:	compizconfig0.8-devel
BuildRequires:	pygtk2.0-devel
BuildRequires:	python-pyrex
Requires:	compizconfig0.8-devel
Conflicts:	python-%{shortname} > 0.9
Conflicts:	%{_lib}%{oname}
Conflicts:	%{_lib}%{oname}-devel

%description
Python bindings for libcompizconfig.

%files
%{py_platsitedir}/%{shortname}.so
%{_libdir}/pkgconfig/%{oname}.pc

#----------------------------------------------------------------------------

%prep
%setup -q -n %{distname}

%build
%if %{git}
# This is a GIT snapshot, so we need to generate makefiles.
  sh autogen.sh -V
%endif

%configure2_5x --disable-static
%make

%install
%makeinstall_std

