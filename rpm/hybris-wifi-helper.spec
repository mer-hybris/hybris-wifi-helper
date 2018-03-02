Name:		hybris-wifi-helper
Version:	0.0.1
Release:	1%{?dist}
Summary:	Helper to utilize the legacy android wifi HAL

Group:		Applications/System
License:	ASL 2.0
URL:		https://github.com/mer-hybris/hybris-wifi-helper
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	libhybris-tests

%define bin_name hybris_wifi_helper

%description
%{summary}. It is simply a repackaged version of test_wifi from libhybris.

%prep
# nothing to do

%build
# nothing to do

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp %{_bindir}/test_wifi $RPM_BUILD_ROOT/%{_bindir}/%{bin_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/%{bin_name}

