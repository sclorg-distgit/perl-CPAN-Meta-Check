%{?scl:%scl_package perl-CPAN-Meta-Check}

Name:		%{?scl_prefix}perl-CPAN-Meta-Check
Summary:	Verify requirements in a CPAN::Meta object
Version:	0.012
Release:	4%{?dist}
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		https://metacpan.org/release/CPAN-Meta-Check
Source0:	http://cpan.metacpan.org/authors/id/L/LE/LEONT/CPAN-Meta-Check-%{version}.tar.gz 
BuildArch:	noarch
# Build
BuildRequires:	%{?scl_prefix}perl
BuildRequires:	%{?scl_prefix}perl-generators
BuildRequires:	%{?scl_prefix}perl(ExtUtils::MakeMaker)
# Module
BuildRequires:	%{?scl_prefix}perl(base)
BuildRequires:	%{?scl_prefix}perl(CPAN::Meta::Prereqs) >= 2.132830
BuildRequires:	%{?scl_prefix}perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:	%{?scl_prefix}perl(Exporter)
BuildRequires:	%{?scl_prefix}perl(Module::Metadata) >= 1.000023
BuildRequires:	%{?scl_prefix}perl(strict)
BuildRequires:	%{?scl_prefix}perl(warnings)
# Test
BuildRequires:	%{?scl_prefix}perl(Env)
BuildRequires:	%{?scl_prefix}perl(Test::Deep)
BuildRequires:	%{?scl_prefix}perl(Test::More) >= 0.88
# Extra tests
%if !%{defined perl_small}
BuildRequires:	%{?scl_prefix}perl(File::Spec)
BuildRequires:	%{?scl_prefix}perl(IO::Handle)
BuildRequires:	%{?scl_prefix}perl(IPC::Open3)
BuildRequires:	%{?scl_prefix}perl(Pod::Coverage::TrustPod)
BuildRequires:	%{?scl_prefix}perl(Test::Pod) >= 1.41
BuildRequires:	%{?scl_prefix}perl(Test::Pod::Coverage) >= 1.08
%endif
# Runtime
Requires:	%{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))

%description
This module verifies if requirements described in a CPAN::Meta object are
present.

%prep
%setup -q -n CPAN-Meta-Check-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}
%if !%{defined perl_small}
%{?scl:scl enable %{scl} '}make test TEST_FILES="%{?scl:'"}$(echo $(find xt/ -name '*.t'))%{?scl:"'}"%{?scl:'}
%endif

%files
%doc LICENSE
%doc Changes README
%{perl_vendorlib}/CPAN/
%{_mandir}/man3/CPAN::Meta::Check.3*

%changelog
* Mon Jul 18 2016 Petr Pisar <ppisar@redhat.com> - 0.012-4
- SCL

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.012-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.012-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Paul Howarth <paul@city-fan.org> - 0.012-1
- Update to 0.012
  - Drop dependency on Exporter 5.57

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.011-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.011-2
- Perl 5.22 rebuild

* Mon Mar 23 2015 Paul Howarth <paul@city-fan.org> - 0.011-1
- Update to 0.011
  - Declare the minimum version required for the "merged_requirements"
    interface
- Explicitly run the extra tests

* Mon Feb  2 2015 Paul Howarth <paul@city-fan.org> - 0.010-1
- Update to 0.010
  - Bump Module::Metadata prereq for $VERSION parsing (CPAN RT#101095)
  - Consistently require same version of CPAN::Meta::Requirements
- Use %%license

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-3
- Perl 5.20 rebuild

* Tue Jul  1 2014 Paul Howarth <paul@city-fan.org> - 0.009-2
- Always run the release tests (#1114859)

* Mon Jun 23 2014 Paul Howarth <paul@city-fan.org> - 0.009-1
- Update to 0.009
  - Various POD fixes

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 17 2013 Paul Howarth <paul@city-fan.org> - 0.008-1
- Update to 0.008
  - Switch to using merged_requirements
  - Test Env instead of Carp for version overshoot (CPAN RT#89591)
  - Document $incdirs in the right function

* Wed Sep  4 2013 Paul Howarth <paul@city-fan.org> - 0.007-3
- Skip the release tests when bootstrapping

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Paul Howarth <paul@city-fan.org> - 0.007-1
- Update to 0.007
  - Swap conflicts test, as underscore versions broke it (CPAN RT#87438)

* Sat Jul 27 2013 Paul Howarth <paul@city-fan.org> - 0.006-1
- Update to 0.006
  - Fixed bad dereference during conflicts checking

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 0.005-3
- Perl 5.18 rebuild

* Wed May  1 2013 Paul Howarth <paul@city-fan.org> - 0.005-2
- Sanitize for Fedora submission

* Sat Apr 27 2013 Paul Howarth <paul@city-fan.org> - 0.005-1
- Initial RPM version
