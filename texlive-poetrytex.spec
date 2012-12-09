# revision 27174
# category Package
# catalog-ctan /macros/latex/contrib/poetrytex
# catalog-date 2012-07-26 10:22:38 +0200
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-poetrytex
Version:	1.1
Release:	1
Summary:	Typeset anthologies of poetry
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/poetrytex
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poetrytex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poetrytex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poetrytex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is designed to aid in the management and formatting
of anthologies of poetry and other writings; it does not
concern itself with actually typesettinig the verse itself.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/poetrytex/poetrytex.sty
%doc %{_texmfdistdir}/doc/latex/poetrytex/README
%doc %{_texmfdistdir}/doc/latex/poetrytex/poetrytex.pdf
#- source
%doc %{_texmfdistdir}/source/latex/poetrytex/Makefile
%doc %{_texmfdistdir}/source/latex/poetrytex/poetrytex.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 813733
- Import texlive-poetrytex
- Import texlive-poetrytex

