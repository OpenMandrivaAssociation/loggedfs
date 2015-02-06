%define name	loggedfs
%define version	0.5
%define release	6

Name:		%name
Version:	%version
Release:	%release
License:	GPL
Source:		http://downloads.sourceforge.net/loggedfs/loggedfs-%{version}.tar.bz2
Patch0:		%{name}_makefile.patch
URL:		http://loggedfs.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-root
Group:		File tools
Summary:	Fuse-based filesystem which can log every operations that happens in it
BuildRequires:	fuse-devel, pcre-devel, rlog-devel, libxml2-devel
Requires:	fuse
%description
LoggedFS is a fuse-based filesystem which can log every operations that happens
in it.

How it works: Fuse does almost everything. LoggedFS only sends a message
to syslog when called by fuse and then let the real filesystem do the
rest of the job.

%prep
%setup -q -c
%patch0 -p1

%build
%make

%install
%{__mkdir} -p $RPM_BUILD_ROOT%{_mandir}/man1 $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_sysconfdir}

%makeinstall

%files
%defattr(-,root,root)
%doc LICENSE
%{_sysconfdir}/loggedfs.xml
%{_bindir}/loggedfs
%{_mandir}/man1/loggedfs.*


%changelog
* Sat Feb 11 2012 Oden Eriksson <oeriksson@mandriva.com> 0.5-5mdv2012.0
+ Revision: 773000
- relink against libpcre.so.1

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5-4mdv2011.0
+ Revision: 612771
- the mass rebuild of 2010.1 packages

* Tue Nov 24 2009 Jérôme Brenier <incubusss@mandriva.org> 0.5-3mdv2010.1
+ Revision: 469745
- rebuild for new rlog

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.5-2mdv2010.0
+ Revision: 439564
- rebuild

* Mon Oct 13 2008 Nicolas Vigier <nvigier@mandriva.com> 0.5-1mdv2009.1
+ Revision: 293372
- new version 0.5

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 0.4-5mdv2009.0
+ Revision: 251349
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.4-3mdv2008.1
+ Revision: 170966
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request
- fix man pages

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Jun 19 2007 Nicolas Vigier <nvigier@mandriva.com> 0.4-2mdv2008.0
+ Revision: 41488
- add license file

* Tue Jun 19 2007 Nicolas Vigier <nvigier@mandriva.com> 0.4-1mdv2008.0
+ Revision: 41482
- Import loggedfs

