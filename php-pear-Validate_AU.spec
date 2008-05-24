%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	AU
%define		_status		alpha
%define		_pearname	Validate_AU
Summary:	%{_pearname} - Data validation class for Australia
Summary(pl.UTF-8):	%{_pearname} - klasa sprawdzająca poprawność danych dla Australii
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	2
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	785632d17681fb51251c3481d90fcc4e
URL:		http://pear.php.net/package/Validate_AU/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Validate >= 0.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package containes locale validation for AU such as:
- Phone Number
- Postal Code
- Tax File Number
- Australian Business Number
- Australian Company Number
- Australian Regional Codes

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności dla Australii danych takich jak:
- numer telefonu,
- kod pocztowym
- numer podatkowy,
- Australian Business Number
- Australian Company Number
- Australian Regional Codes

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Validate_AU/LICENSE
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/AU.php
%{php_pear_dir}/data/Validate_AU/data/AU_postcodes.txt

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Validate_AU
