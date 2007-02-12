Summary:	iceauth application
Summary(pl.UTF-8):	Aplikacja iceauth
Name:		xorg-app-iceauth
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Application
Source0:	http://xorg.freedesktop.org/releases/individual/app/iceauth-%{version}.tar.bz2
# Source0-md5:	50df9a5718b3cb6544a1c9f38b392b09
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iceauth application.

%description -l pl.UTF-8
Aplikacja iceauth.

%prep
%setup -q -n iceauth-%{version}

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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/iceauth
%{_mandir}/man1/iceauth.1x*
