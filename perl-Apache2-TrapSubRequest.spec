%define upstream_name    Apache2-TrapSubRequest
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Apache2::TrapSubRequest - Trap a lookup_file/lookup_uri into a scalar
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Apache2/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	apache-mod_perl
BuildRequires:	perl(Apache::Test) >= 1.25
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Apache2::TrapSubRequest - Trap a lookup_file/lookup_uri into a
scalar.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Apache2/TrapSubRequest.pm
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 680467
- mass rebuild

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 402974
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.03-5mdv2009.0
+ Revision: 241146
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.03-3mdv2008.0
+ Revision: 25446
- rebuild


* Thu Apr 27 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.03-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL
- use mkrel

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 0.03-1mdk
- initial Mandriva package

