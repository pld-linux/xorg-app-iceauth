# $Rev: 3346 $, $Date: 2005-08-27 17:42:47 $
#
Summary:	iceauth application
Summary(pl):	Aplikacja iceauth
Name:		xorg-app-iceauth
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Application
######		Unknown group!
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/iceauth-%{version}.tar.bz2
# Source0-md5:	64ac4d6ebaf4eec9cdc4d968e0e9840b
Patch0:		iceauth-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/iceauth-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
iceauth application.

%description -l pl
Aplikacja iceauth.


%prep
%setup -q -n iceauth-%{version}
%patch0 -p1


%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
