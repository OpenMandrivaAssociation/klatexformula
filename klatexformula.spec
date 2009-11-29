%define name	klatexformula
%define version 3.1.2
%define release 1

%define major 3
%define libname %mklibname klfbackend %major
%define develname %name-devel

Summary:	Easily get an image from a LaTeX formula
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Source0:	http://ovh.dl.sourceforge.net/sourceforge/klatexformula/%name-%version.tar.gz
Patch0:		klatexformula-no-undefined-3.1.2.patch
Patch1:		klatexformula-shared-3.1.2.patch
License:	GPLv2+
Group:		Publishing
Url:		http://klatexformula.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	%{libname} = %{version}-%{release}
Requires:	ghostscript, tetex-latex, tetex-dvips
BuildRequires:	qt4-devel

%description
This application provides an easy-to-use graphical user interface
for generating images from LaTeX equations. These images can be
dragged and dropped or copied and pasted into external applications
(presentations, text documents, graphics...), or can be saved to
disk in a variety of formats (PNG, JPG, BMP, EPS, PDF, etc.). In
addition to the graphical user interface, a command-line interface
and a C++ library are provided to perform the same job.

%package -n %libname
Summary:	Shared libraries for KLatexFormula
Group:		Publishing

%description -n %libname
This package contains shared libraries for KLatexFormula.

%package -n %develname
Summary:	Development files for KLatexFormula
Group:		Development/C++
Requires:	%libname = %version-%release

%description -n %develname
This package contains development files for KLatexFormula.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0

%build
%qmake_qt4
%make

%install
%__rm -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %develname
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*.h
