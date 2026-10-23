%define major 12
%define libname %mklibname courier-unicode %{major}
%define devname %mklibname courier-unicode -d

Name:		courier-unicode
Version:	2.6.0
Release:	1
Summary:	Unicode library used by Courier mail packages
License:	GPL-3.0-or-later
Group:		System/Libraries
URL:		https://www.courier-mta.org/unicode/
Source0:	http://prdownloads.sourceforge.net/courier/%{name}-%{version}.tar.bz2
BuildSystem:	autotools
BuildOption:	--disable-static
BuildRequires:	perl

%description
The Courier Unicode library implements the Unicode algorithms used by
Courier Authlib, Courier IMAP, and the other Courier mail packages.
Courier Authlib 0.73 and Courier IMAP 6 require version 2.6.

%package -n %{libname}
Summary:	Unicode library used by Courier mail packages
Group:		System/Libraries

%description -n %{libname}
Shared library for the Courier Unicode algorithms.

%package -n %{devname}
Summary:	Development files for the Courier Unicode library
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Headers, man pages, and the autoconf macro for building software
against the Courier Unicode library.

%files
%license COPYING
%doc README AUTHORS ChangeLog

%files -n %{libname}
%{_libdir}/libcourier-unicode.so.%{major}*

%files -n %{devname}
%{_includedir}/courier-unicode.h
%{_includedir}/courier-unicode-categories-tab.h
%{_includedir}/courier-unicode-script-tab.h
%{_libdir}/libcourier-unicode.so
%{_datadir}/aclocal/courier-unicode-version.m4
%{_mandir}/man3/*
%{_mandir}/man7/*
