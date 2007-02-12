Summary:	DOC++ - A Documentation System for C, C++, IDL and Java
Summary(es.UTF-8):   DOC++ - Un sistema de documentacion para C, C++, IDL y Java
Summary(fr.UTF-8):   DOC++ - Un générateur de documentation pour C, C++, IDL et Java
Summary(pl.UTF-8):   DOC++ - System dokumentacji dla C, C++, IDL oraz Java
Summary(ro.UTF-8):   DOC++ - Generator de documentatii pentru C, C++, IDL si Java
Summary(ru.UTF-8):   DOC++ - Система документирования исходных текстов для C, C++, IDL и Java
Summary(sv.UTF-8):   DOC++ - Ett dokumentationsgenereringssystem för C, C++, IDL och Java
Name:		doc++
Version:	3.4.10
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/docpp/%{name}-%{version}.tar.gz
# Source0-md5:	095c7a3a822f00a33033b8bb40147445
URL:		http://docpp.sourceforge.net/
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

%description -l es.UTF-8
DOC++ es un sistema de documentacion para C, C++, IDL y Java, que
genera textos en TeX para crear copias de alta calidad de la
documentación y en HTML para poder navegar por ella. La documentación
se extrae directamente de lso ficheros de cabecera C/C++/IDL o de los
ficheros de clase en Java.

%description -l fr.UTF-8
DOC++ est un système de documentation pour C, C++, IDL et Java. Il
peut générer au choix un document TeX pour produire une documentation
imprimée de qualité, ou un fichier HTML pour un parcours en-ligne aisé
de la documentation. La documentation est extraite directement du
fichier d'en-tête C/C++/IDL ou du fichier des classes Java.

%description -l pl.UTF-8
DOC++ is jest systemem dokumentacji dla C, C++, IDL oraz Java,
generującym zarówno pliki TeX dla wysokiej jakości wydruku i HTML dla
wyszukanego przeglądania własnej dokumentacji. Dokumentacja jest
tworzona bezpośrednio z kodu C/C++/IDL lub klas Javy.

%description -l ro.UTF-8
DOC++ este un generator de documentatii pentru C, C++, IDL si Java,
producand iesire atat in format TeX pentru copii de calitate cat si
HTML pentru navigare on-line prin documentatie. Documentatia este
extrasa direct din fisierele header/sursa C/C++/IDL sau din fisierele
de tip clasa Java.

%description -l ru.UTF-8
DOC++ -- система документирования исходных текстов для языков C, C++,
IDL и Java. Поддерживается вывод в формате TeX для печати и HTML --
для создания гипертекстовых справочников. Документация располагается
непосредственно в исходном тексте, с использованием комментариев
специального формата.

%description -l sv.UTF-8
DOC++ är ett dokumentationsgenereringssystem för C, C++, IDL och Java
som genererar både TeX-kod för högkvalitativa utskrifter och HTML för
sofistikerad webbvisning av dokumentationen. Dokumentationen
extraheras direkt från C/C++/IDL-headerfilen eller javaklassfilen.

%prep
%setup -q

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
