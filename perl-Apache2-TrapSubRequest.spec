%define upstream_name    Apache2-TrapSubRequest
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Apache2::TrapSubRequest - Trap a lookup_file/lookup_uri into a scalar
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Apache2/%{upstream_name}-%{upstream_version}.tar.gz

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

# The tests will fail to run inside ABF chroot
# %check
# make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Apache2/TrapSubRequest.pm
%{_mandir}/*/*

