# revision 30220
# category Package
# catalog-ctan /macros/latex/contrib/beamer-contrib/bxdpx-beamer
# catalog-date 2013-05-03 01:03:17 +0200
# catalog-license other-free
# catalog-version 0.2
Name:		texlive-bxdpx-beamer
Version:	0.2
Release:	6
Summary:	Dvipdfmx extras for use with beamer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/bxdpx-beamer
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxdpx-beamer.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxdpx-beamer.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is a driver to support beamer Navigation symbols
and \framezoomed regions when using dvipdfmx as PDF generator
(e.g., as part of e-pTeX). The package does not define any
'user' commands.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bxdpx-beamer/bxdpx-beamer.sty
%doc %{_texmfdistdir}/doc/latex/bxdpx-beamer/LICENSE
%doc %{_texmfdistdir}/doc/latex/bxdpx-beamer/README
%doc %{_texmfdistdir}/doc/latex/bxdpx-beamer/sample/test-framezoom.tex
%doc %{_texmfdistdir}/doc/latex/bxdpx-beamer/sample/test-navisymbol.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
