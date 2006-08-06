%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	DataGrid_DataSource_DBQuery
%define		_status		beta
%define		_pearname	Structures_DataGrid_DataSource_DBQuery

Summary:	%{_pearname} - DataSource driver using PEAR::DB and an SQL query
Summary(pl):	%{_pearname} - sterownik DataSource do PEAR::DB i kwerend SQL
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fd6b57859ff145e920de097cb1a5218e
URL:		http://pear.php.net/package/Structures_DataGrid_DataSource_DBQuery/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-DB >= 1.7.6
Requires:	php-pear-PEAR >= 1:1.4.-0.9
Requires:	php-pear-Structures_DataGrid >= 0.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a DataSource driver for Structures_DataGrid using PEAR::DB and
an SQL query.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet dostarcza sterownik do PEAR::DB i kwerend SQL dla
Structures_DataGrid.

Ta klasa ma w PEAR status: %{_status}.

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
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Structures/DataGrid/DataSource/DBQuery.php
