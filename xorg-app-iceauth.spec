Summary:	iceauth application - ICE authority file utility
Summary(pl.UTF-8):	Aplikacja iceauth - narzędzie do plików autoryzacji ICE
Name:		xorg-app-iceauth
Version:	1.0.10
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/iceauth-%{version}.tar.xz
# Source0-md5:	30f898d71a7d8e817302970f1976198c
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.70
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.22
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The iceauth program is used to edit and display the authorization
information used in connecting with ICE. This program is usually used
to extract authorization records from one machine and merge them in on
another (as is the case when using remote logins or granting access to
other users). Commands may be entered interactively, on the iceauth
command line, or in scripts.

%description -l pl.UTF-8
Program iceauth służy do modyfikowania i wyświetlania informacji
autoryzacyjnych używanych przy łączeniu się z ICE. Ten program zwykle
jest używany do wyciągania rekordów autoryzacyjnych z jednej maszyny i
dołączania ich na innej (tak robi się w przypadku używania zdalnych
logowań lub dawania dostępu innym użytkownikom). Polecenia można
wprowadzać interaktywnie, z linii poleceń lub w skrypcie.

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
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/iceauth
%{_mandir}/man1/iceauth.1*
