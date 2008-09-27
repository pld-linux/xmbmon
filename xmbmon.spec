Summary:	Mother Board Monitor Program
Summary(pl.UTF-8):	Program do monitorowania płyty głównej
Name:		xmbmon
Version:	205
Release:	2
License:	BSD-like
Group:		Applications/System
Source0:	http://www.nt.phys.kyushu-u.ac.jp/shimizu/download/xmbmon/%{name}%{version}.tar.gz
# Source0-md5:	ab6614c785f5b653fcc69fb9c02058f0
Patch0:		%{name}-fflush.patch
URL:		http://www.nt.phys.kyushu-u.ac.jp/shimizu/download/download.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Recent motherboards have functionalities to monitor the CPU
temperatures and the frequency of CPU cooling fans etc. Although some
programs utilizing these hardware monitoring facilities have been
developed for the Microsoft Windows platforms, no programs seem to
exist for PC-UNIX and the X Window System platforms. These small
programs have only least functionalities, the one "mbmon" used at the
command line reports the temperatures, voltages and rpm (rounds per
minute) of cooling fans, and the other "xmbmon" displays the three
temperatures and a core voltage as simple curves.

%description -l pl.UTF-8
Nowe płyty główne mają funkcjonalność monitorowania temperatur CPU,
szybkości wiatraczków chłodzących CPU itp. Mimo że powstały programy
wykorzystujące te możliwości dla platform Microsoft Windows, żaden
nie istniał dla platform PC-UNIX i X Window System. Te małe programy
mają minimalną funkcjonalność - mbmon używany z linii poleceń wypisuje
temperatury, napięcia i rpm (liczbę obrotów na minutę) wiatraczków, a
xmbmon wyświetla temperatury i napięcia jako proste krzywe.

%package X11
Summary:	Mother Board Monitor Program for X Window System
Summary(pl.UTF-8):	Program do monitorowania płyty głównej dla X Window System
Group:		X11/Applications

%description X11
Mother Board Monitor Program for X Window System.

%description X11 -l pl.UTF-8
Program do monitorowania płyty głównej dla X Window System.

%prep
%setup -q -n %{name}%{version}
%patch0 -p0

%build
cp -f /usr/share/automake/config.sub AC-TOOLS/
%{__aclocal}
%{__autoconf}
%configure
%{__make} \
	CC="%{__cc} %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install mbmon $RPM_BUILD_ROOT%{_bindir}
install xmbmon $RPM_BUILD_ROOT%{_bindir}
install mbmon.1 $RPM_BUILD_ROOT%{_mandir}/man1
install xmbmon.1x $RPM_BUILD_ROOT%{_mandir}/man1/xmbmon.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ReadMe ReadMe.tech ChangeLog CopyRight mbmon-rrd.pl
%attr(755,root,root) %{_bindir}/mbmon
%{_mandir}/man1/mbmon*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/xmbmon*
