Summary:	converts a single mail to a tiny text with contents from the mail
Summary(pl):	Konwertuje pojedyñcze maile do niewielkich tekstowych wiadomo¶ci
Name:		mail2sms
Version:	1.3.4
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://www.contactor.se/~dast/stuff/%{name}-%{version}.tar.gz
# Source0-md5:	8466cd164ea3bd140770682e96109fd7
URL:		http://www.contactor.se/~dast/mail2sms/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mail2sms converts a single (large) mail to a tiny text with contents
from the mail. Perfectly suitable to send as an SMS message to a GSM telephone. 

%prep
%setup -q
%{__aclocal}
%{__autoconf}
%configure

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man{1,4},%{_bindir}}

install mail2sms   $RPM_BUILD_ROOT%{_bindir}
install mail2sms.1 $RPM_BUILD_ROOT%{_mandir}/man1
install mail2sms.4 $RPM_BUILD_ROOT%{_mandir}/man4

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README REGEX TODO UPGRADE forward.* example.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
