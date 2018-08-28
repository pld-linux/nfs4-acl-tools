# TODO: shared library when fixed upstream (missing exports file)
Summary:	Command line ACL utilities for the Linux NFSv4 client
Summary(pl.UTF-8):	Narzędzia linii poleceń do ACL dla linuksowego klienta NFSv4
Name:		nfs4-acl-tools
Version:	0.3.5
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://linux-nfs.org/~bfields/nfs4-acl-tools/%{name}-%{version}.tar.gz
# Source0-md5:	7d69a96c4d6def3db53151646fbcde65
URL:		http://linux-nfs.org/
BuildRequires:	attr-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command line ACL utilities for the Linux NFSv4 client.

%description -l pl.UTF-8
Narzędzia linii poleceń do ACL dla linuksowego klienta NFSv4.

%package devel
Summary:	Header files and static libnfs4acl library
Summary(pl.UTF-8):	Pliki nagłówkowe i biblioteka statyczna libnfs4acl
Group:		Development/Libraries

%description devel
Header files and static libnfs4acl library.

%description devel -l pl.UTF-8
Pliki nagłówkowe i biblioteka statyczna libnfs4acl.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%configure
# --enable-shared (broken as of 0.3.5, missing "exports" file)
%{__make} \
	LIBTOOL="libtool --tag=CC" \
	LTLDFLAGS="-rpath %{_libdir} -static" \
	OPTIMIZER="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-dev \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_MAN='install -m644 $(MAN_PAGES) $(MAN_DEST)' \
	PKG_INC_DIR=$RPM_BUILD_ROOT%{_includedir}

cp -p include/{libacl_nfs4,nfs4}.h $RPM_BUILD_ROOT%{_includedir}

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

%files devel
%defattr(644,root,root,755)
%{_libdir}/libnfs4acl.a
%{_includedir}/libacl_nfs4.h
%{_includedir}/nfs4.h
