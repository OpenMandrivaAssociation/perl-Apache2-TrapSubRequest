%define upstream_name    Apache2-TrapSubRequest
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Apache2::TrapSubRequest - Trap a lookup_file/lookup_uri into a scalar
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Apache2-TrapSubRequest
Source0:	https://cpan.metacpan.org/authors/id/D/DO/DORIAN/Apache2-TrapSubRequest-%{upstream_version}.tar.gz

BuildRequires:	make
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

