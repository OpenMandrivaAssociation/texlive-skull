Name:		texlive-skull
Version:	51907
Release:	2
Summary:	A font to draw a skull
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/skull
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skull.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skull.source.r%{version}.tar.xz
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
%{_texmfdistdir}/fonts/tfm/public/skull
%{_texmfdistdir}/fonts/source/public/skull
%{_texmfdistdir}/tex/latex/skull
#- source
%doc %{_texmfdistdir}/source/fonts/skull

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex source %{buildroot}%{_texmfdistdir}
