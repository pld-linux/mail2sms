Summary:	Converts a single mail to a tiny text with contents from the mail
Summary(pl.UTF-8):	Konwersja pojedynczych listów do niewielkich tekstowych wiadomości
Name:		mail2sms
Version:	1.3.5
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://www.contactor.se/~dast/stuff/%{name}-%{version}.tar.gz
# Source0-md5:	6aa360998779bff1d3333c7a762d0e9e
URL:		http://daniel.haxx.se/projects/mail2sms/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mail2sms converts a single (large) mail to a tiny text with contents
from the mail. Perfectly suitable to send as an SMS message to a GSM
telephone.

%description -l pl.UTF-8
mail2sms konwertuje pojedyncze (duże) listy do małego tekstu z treścią
z listu, znakomicie nadającego się do wysyłania jako SMS na telefon
GSM.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure \
	CFLAGS="%{rpmcflags} %{rpmcppflags}"

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
