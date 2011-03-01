%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	Validate_AU
Summary:	%{_pearname} - Data validation class for Australia
Summary(pl.UTF-8):	%{_pearname} - klasa sprawdzająca poprawność danych dla Australii
Name:		php-pear-%{_pearname}
Version:	0.1.4
Release:	2
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f45157618a42e85567634462f4ab5382
URL:		http://pear.php.net/package/Validate_AU/
BuildRequires:	php-pear-PEAR >= 1:1.4.9
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Validate >= 0.5.0
Obsoletes:	php-pear-Validate_AU-tests
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

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/%{_pearname}/{data/*,}
rmdir .%{php_pear_dir}/data/%{_pearname}/data
mv docs/{%{_pearname}/*,.}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/LICENSE
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/AU.php
%{php_pear_dir}/data/%{_pearname}
