%define real_name Apache2-TrapSubRequest

Summary:	Apache2::TrapSubRequest - Trap a lookup_file/lookup_uri into a scalar
Name:		perl-%{real_name}
Version:	0.03
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Apache2/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	apache-mod_perl
BuildRequires:	perl(Apache::Test) >= 1.25
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Apache2::TrapSubRequest - Trap a lookup_file/lookup_uri into a
scalar.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Apache2/TrapSubRequest.pm
%{_mandir}/*/*

