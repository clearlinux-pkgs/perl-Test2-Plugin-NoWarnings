#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test2-Plugin-NoWarnings
Version  : 0.09
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Test2-Plugin-NoWarnings-0.09.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Test2-Plugin-NoWarnings-0.09.tar.gz
Summary  : 'Fail if tests warn'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Test2-Plugin-NoWarnings-license = %{version}-%{release}
Requires: perl-Test2-Plugin-NoWarnings-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Importer)
BuildRequires : perl(Sub::Info)
BuildRequires : perl(Test2::Require::Module)
BuildRequires : perl(Test2::V0)

%description
# NAME
Test2::Plugin::NoWarnings - Fail if tests warn
# VERSION
version 0.09
# SYNOPSIS

%package dev
Summary: dev components for the perl-Test2-Plugin-NoWarnings package.
Group: Development
Provides: perl-Test2-Plugin-NoWarnings-devel = %{version}-%{release}
Requires: perl-Test2-Plugin-NoWarnings = %{version}-%{release}

%description dev
dev components for the perl-Test2-Plugin-NoWarnings package.


%package license
Summary: license components for the perl-Test2-Plugin-NoWarnings package.
Group: Default

%description license
license components for the perl-Test2-Plugin-NoWarnings package.


%package perl
Summary: perl components for the perl-Test2-Plugin-NoWarnings package.
Group: Default
Requires: perl-Test2-Plugin-NoWarnings = %{version}-%{release}

%description perl
perl components for the perl-Test2-Plugin-NoWarnings package.


%prep
%setup -q -n Test2-Plugin-NoWarnings-0.09
cd %{_builddir}/Test2-Plugin-NoWarnings-0.09

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test2-Plugin-NoWarnings
cp %{_builddir}/Test2-Plugin-NoWarnings-0.09/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test2-Plugin-NoWarnings/5586816d65cedc4c52fb3e6704d529fb9535d8fe
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test2::Event::Warning.3
/usr/share/man/man3/Test2::Plugin::NoWarnings.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test2-Plugin-NoWarnings/5586816d65cedc4c52fb3e6704d529fb9535d8fe

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
