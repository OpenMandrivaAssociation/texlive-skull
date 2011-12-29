# revision 15878
# category Package
# catalog-ctan /fonts/skull
# catalog-date 2007-02-28 00:02:05 +0100
# catalog-license gpl
# catalog-version 0.1
Name:		texlive-skull
Version:	0.1
Release:	1
Summary:	A font to draw a skull
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/skull
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skull.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skull.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The font (defined in MetaFont) defines a single character, a
black solid skull. A package is supplied to make this character
available as a symbol in maths mode.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/skull/skull.mf
%{_texmfdistdir}/tex/latex/skull/skull.sty
#- source
%doc %{_texmfdistdir}/source/latex/skull/skull.dtx
%doc %{_texmfdistdir}/source/latex/skull/skull.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex source %{buildroot}%{_texmfdistdir}
