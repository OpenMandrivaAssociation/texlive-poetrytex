Name:		texlive-poetrytex
Version:	3.0.1
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
%{_texmfdistdir}/tex/latex/poetrytex
%doc %{_texmfdistdir}/doc/latex/poetrytex
#- source
%doc %{_texmfdistdir}/source/latex/poetrytex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
