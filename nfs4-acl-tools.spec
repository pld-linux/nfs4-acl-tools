#
# Conditional build:
%bcond_without	gui	# Qt4-based ACL editor
#
Summary:	Command line ACL utilities for the Linux NFSv4 client
Summary(pl.UTF-8):	Narzędzia linii poleceń do ACL dla linuksowego klienta NFSv4
Name:		nfs4-acl-tools
Version:	0.3.3
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/nfs4-acl-tools/%{name}-%{version}.tar.gz
# Source0-md5:	ece4d5599c3b8470990ee1adbe22e047
Patch0:		%{name}-strlcpy.patch
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
BuildRequires:	attr-devel
%if %{with gui}
BuildRequires:	QtGui-devel >= 4.1.4
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
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
License:	BSD
Group:		X11/Applications

%description gui
GUI ACL utility for the Linux NFSv4 client.

%description gui -l pl.UTF-8
Graficzny interfejs użytkownika do ACL dla linuksowego klienta NFSv4.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make} \
	OPTIMIZER="%{rpmcflags}"

%if %{with gui}
cd GUI/nfs4-acl-editor
qmake-qt4 \
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
%doc COPYING README TODO
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
