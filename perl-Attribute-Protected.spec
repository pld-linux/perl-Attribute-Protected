#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Attribute
%define		pnam	Protected
Summary:	Attribute::Protected - implementing proctected methods with attributes
Summary(pl.UTF-8):   Attribute::Protected - implementacja metod i atrybutów chronionych
Name:		perl-Attribute-Protected
Version:	0.03
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	797463820a6149feadf1aa52fae2673a
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Attribute::Protected implements something like public / private /
protected methods in C++ or Java.

%description -l pl.UTF-8
Attribute::Protected implementuje coś na kształt publicznych / prywatnych
/ chronionych metod w C++ i Javie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*.3pm*
