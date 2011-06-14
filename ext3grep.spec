Summary:	A tool to investigate an ext3 FS for deleted content and possibly recover it
Name:		ext3grep
Version:	0.10.2
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://ext3grep.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	38e134734d6c8856370ed00a9c73dbee
URL:		http://code.google.com/p/ext3grep/
BuildRequires:	e2fsprogs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool to investigate an ext3 file system for deleted content and
possibly recover it.

%prep
%setup -q

%build
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
%doc NEWS README
%attr(755,root,root) %{_bindir}/%{name}
