%define upstream_name    Perl-Critic-Lax
%define upstream_version 0.010

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Policies that let you slide on common exceptions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Perl/Perl-Critic-Lax-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Perl::Critic)
BuildArch:	noarch

%description
The Perl-Critic-Lax distribution includes versions of core Perl::Critic
modules with built-in exceptions. If you really like a Perl::Critic policy,
but find that you often violate it in a specific way that seems pretty darn
reasonable, maybe there's a Lax policy. If there isn't, send one in!

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.8.0-2mdv2011.0
+ Revision: 655609
- rebuild for updated spec-helper

* Mon Sep 06 2010 Jérôme Quelin <jquelin@mandriva.org> 0.8.0-1mdv2011.0
+ Revision: 576301
- update to 0.008

* Fri Aug 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.7.0-1mdv2011.0
+ Revision: 573475
- import perl-Perl-Critic-Lax



