
Summary:	Mother Board Monitor Program
Summary(pl):	-
Name:		xmbmon
Version:	203
Release:	1
License:	Freeware
Group:		Tools
Source0:	http://www.nt.phys.kyushu-u.ac.jp/shimizu/download/%{name}%{version}.tar.gz
# Source0-md5:	f84e48b8e433170358cec840020b2419
URL:		http://www.nt.phys.kyushu-u.ac.jp/shimizu/download/download.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Recent motherboards have functionalities to monitor the CPU
temperatures and the frequency of CPU cooling fans etc. Although some
programs utilizing these hardware monitoring facilities have been
developed for the Microsoft Windows platforms, no programs seem to
exist for PC-UNIX and the X Windows System platforms. Thus, I have
tried to make small programs. They have only least functionalities,
the one "mbmon" used at the command line reports the temperatures,
voltages and rpm (rounds per minute) of cooling fans, and the other
"xmbmon" displays the three temperatures and a core voltage as simple
curves.

%description -l pl
- -

%package X11
Summary:	Mother Board Monitor Program for X Window System
Summary(pl):	-
Group:		X11/Aplications
Requires:	XFree86-libs

%description X11
Mother Board Monitor Program for Xwindows

%description X11 -l pl
- -

%prep
%setup -q -n "%{name}%{version}"

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make} \
	CC="%{__cc} %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

install mbmon $RPM_BUILD_ROOT%{_bindir}
install xmbmon $RPM_BUILD_ROOT%{_bindir}

cp 00READMEtech.txt READMEtech.txt
cp 00README.txt README.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc READMEtech.txt README.txt mbmon-rrd.pl
%attr(755,root,root) %{_bindir}/mbmon

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
