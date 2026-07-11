%global tl_name poetrytex
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0.1
Release:	%{tl_revision}.1
Summary:	Typeset anthologies of poetry
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/poetrytex
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/poetrytex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/poetrytex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/poetrytex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is designed to aid in the management and formatting of
anthologies of poetry and other writings; it does not concern itself
with actually typesetting the verse itself.

