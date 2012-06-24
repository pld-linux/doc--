Summary:	DOC++ - A Documentation System for C, C++, IDL and Java
Summary(es):	DOC++ - Un sistema de documentacion para C, C++, IDL y Java
Summary(fr):	DOC++ - Un g�n�rateur de documentation pour C, C++, IDL et Java
Summary(pl):	DOC++ - System dokuentacji dla C, C++, IDL oraz Java
Summary(ro):	DOC++ - Generator de documentatii pentru C, C++, IDL si Java
Summary(ru):	DOC++ - ������� ���������������� �������� ������� ��� C, C++, IDL � Java
Summary(sv):	DOC++ - Ett dokumentationsgenereringssystem f�r C, C++, IDL och Java
Name:		doc++
Version:	3.4.9
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	ftp://metalab.unc.edu/pub/Linux/apps/doctools/%{name}-%{version}.tar.gz
Patch0:		%{name}-gcc3.patch
URL:		http://docpp.sourceforge.net
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	flex >= 2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DOC++ is a documentation system for C, C++, IDL and Java, generating
both TeX output for high quality hardcopies and HTML output for
sophisticated online browsing of your documentation. The documentation
is extracted directly from the C/C++/IDL header/source files or Java
class files.

%description -l pl
DOC++ is jest systemem dokumentacji dla C, C++, IDL oraz Java, generuj�cym
zar�wno pliki TeX dla wysokiej jako�ci wydruku i HTML dla wyszukanego
przegl�dania twojej dokumentacji. Dokumentacja jest tworzona bezpo�rednio
z kodu C/C++/IDL lub klas Javy.

%description -l es
DOC++ es un sistema de documentacion para C, C++, IDL y Java, que
genera textos en TeX para crear copias de alta calidad de la
documentaci�n y en HTML para poder navegar por ella. La documentaci�n
se extrae directamente de lso ficheros de cabecera C/C++/IDL o de los
ficheros de clase en Java.

%description -l fr
DOC++ est un syst�me de documentation pour C, C++, IDL et Java. Il
peut g�n�rer au choix un document TeX pour produire une documentation
imprim�e de qualit�, ou un fichier HTML pour un parcours en-ligne ais�
de la documentation. La documentation est extraite directement du
fichier d'en-t�te C/C++/IDL ou du fichier des classes Java.

%description -l ro
DOC++ este un generator de documentatii pentru C, C++, IDL si Java,
producand iesire atat in format TeX pentru copii de calitate cat si
HTML pentru navigare on-line prin documentatie. Documentatia este
extrasa direct din fisierele header/sursa C/C++/IDL sau din fisierele
de tip clasa Java.

%description -l ru
DOC++ -- ������� ���������������� �������� ������� ��� ������ C, C++,
IDL � Java. �������������� ����� � ������� TeX ��� ������ � HTML --
��� �������� �������������� ������������. ������������ �������������
��������������� � �������� ������, � �������������� ������������
������������ �������.

%description -l sv
DOC++ �r ett dokumentationsgenereringssystem f�r C, C++, IDL och Java
som genererar b�de TeX-kod f�r h�gkvalitativa utskrifter och HTML f�r
sofistikerad webbvisning av dokumentationen. Dokumentationen
extraheras direkt fr�n C/C++/IDL-headerfilen eller javaklassfilen.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CREDITS NEWS PLATFORMS README REPORTING-BUGS doc/doc++.conf doc/docxx-br.sty doc/docxx-fr.sty doc/docxx-ja.sty doc/docxx-ro.sty doc/docxx.sty
%doc doc/manual
%attr(755,root,root) %{_bindir}/doc++
%attr(755,root,root) %{_bindir}/docify
%attr(755,root,root) %{_bindir}/promote
