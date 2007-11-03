#
# Conditional build:
%bcond_without	gui	# Qt4-based ACL editor
#
Summary:	Command line ACL utilities for the Linux NFSv4 client
Summary(pl.UTF-8):	Narzędzia linii poleceń do ACL dla linuksowego klienta NFSv4
Name:		nfs4-acl-tools
Version:	0.3.2
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/nfs4-acl-tools/%{name}-%{version}.tar.gz
# Source0-md5:	0980000203a102ff6cf2f59b7cbd7dd4
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
BuildRequires:	attr-devel
%if %{with gui}
BuildRequires:	QtGui-devel >= 4.1.4
BuildRequires:	qt4-build >= 4.1.4
BuildRequires:	qt4-qmake >= 4.1.4
BuildRequires:	rpmbuild(macros) >= 1.167
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command line ACL utilities for the Linux NFSv4 client.

%description -l pl.UTF-8
Narzędzia linii poleceń do ACL dla linuksowego klienta NFSv4.

%package gui
Summary:	GUI ACL utility for the Linux NFSv4 client
Summary(pl.UTF-8):	Graficzny interfejs użytkownika do ACL dla linuksowego klienta NFSv4
# code itself is BSD, but Qt enforces GPL
License:	GPL v2
Group:		X11/Applications

%description gui
GUI ACL utility for the Linux NFSv4 client.

%description gui -l pl.UTF-8
Graficzny interfejs użytkownika do ACL dla linuksowego klienta NFSv4.

%prep
%setup -q

%build
%configure
%{__make}

%if %{with gui}
cd GUI/nfs4-acl-editor
qt4-qmake \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"
%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_MAN='install -m644 $(MAN_PAGES) $(MAN_DEST)'

%if %{with gui}
install GUI/nfs4-acl-editor/nfs4-acl-editor $RPM_BUILD_ROOT%{_bindir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG COPYING README TODO
%attr(755,root,root) %{_bindir}/nfs4_editfacl
%attr(755,root,root) %{_bindir}/nfs4_getfacl
%attr(755,root,root) %{_bindir}/nfs4_setfacl
%{_mandir}/man1/nfs4_editfacl.1*
%{_mandir}/man1/nfs4_getfacl.1*
%{_mandir}/man1/nfs4_setfacl.1*
%{_mandir}/man5/nfs4_acl.5*

%if %{with gui}
%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nfs4-acl-editor
%endif
