Summary: Easily get an image from a LaTeX formula
Name: klatexformula
Version: 3.0.1
Release: %mkrel 1
Source0: http://ovh.dl.sourceforge.net/sourceforge/klatexformula/%name-%version.tar.gz
Patch0: klatexformula-3.0.1-shared.patch
Patch1: klatexformula-3.0.1-lib464.patch
License: GPLv2+
Group: Office
Url: http://klatexformula.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: qt4-devel

%description
KLatexFormula is a program to easily get an image from a LaTeX formula.
It is based on LaTeX.

With KLatexFormula, just enter a formula, click "Evaluate", then you
can drag&drop or copy the resulting image to another location (an
OpenOffice document, for example) or save it as an image (many formats
are available).

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*

#--------------------------------------------------------------------
%define major 3
%define libname %mklibname klfbackend %major

%package -n %libname
Summary: Shared libraries for KLatexFormula
Group: Office

%description -n %libname
This package contains shared libraries for KLatexFormula.

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*


#--------------------------------------------------------------------
%define develname %name-devel

%package -n %develname
Summary: Development files for KLatexFormula
Group: Office
Requires: %libname = %version-%release

%description -n %develname
This package contains development files for KLatexFormula.

%files -n %develname
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*.h

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version
%patch0 -p0
%if "%_lib" == "lib64"
%patch1 -p0
%endif

%build
%qmake_qt4
%make

%install
rm -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}
