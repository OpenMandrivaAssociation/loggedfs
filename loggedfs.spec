%define name	loggedfs
%define version	0.4
%define release	%mkrel 3

Name:		%name
Version:	%version
Release:	%release
License:	GPL
Source:		%{name}-%{version}.tar.bz2
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
%setup -q
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
