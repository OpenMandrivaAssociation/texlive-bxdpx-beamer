%global tl_name bxdpx-beamer
%global tl_revision 41813

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Dvipdfmx extras for use with beamer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/bxdpx-beamer
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxdpx-beamer.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxdpx-beamer.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is a driver to support beamer Navigation symbols and
\framezoomed regions when using dvipdfmx as PDF generator (e.g., as part
of e-pTeX). The package does not define any 'user' commands.

