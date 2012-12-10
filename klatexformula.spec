%define major 3
%define libname %mklibname %{name} %major
%define develname %name-devel

Summary:	Easily get an image from a LaTeX formula
Name:		klatexformula
Version:	3.2.6
Release:	1
Source0:	http://freefr.dl.sourceforge.net/project/%name/%name/%name-%version/%name-%version.tar.gz
Patch0:		klatexformula-3.2.0-link.patch
License:	GPLv2+
Group:		Publishing
Url:		http://klatexformula.sourceforge.net/
Requires:	ghostscript, tetex-latex, tetex-dvips
Requires:	%{libname} = %{version}
BuildRequires:	kdelibs4-devel
BuildRequires:	help2man
Obsoletes:	%{_lib}klfbackend3 < 3.2.0

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
Obsoletes:	%{_lib}klfbackend3 < %{version}

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

%build
%cmake_kde4 -DKLF_LIBKLFBACKEND_STATIC=OFF -DKLF_LIBKLFTOOLS_STATIC=OFF -DKLF_LIBKLFAPP_STATIC=OFF
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_kde_bindir}/*
%{_kde_iconsdir}/hicolor/*/apps/%{name}.png
%{_kde_datadir}/applications/%{name}.desktop
%{_kde_datadir}/%{name}
%{_kde_mandir}/man1/*
%{_kde_libdir}/kde4/*.so
%{_kde_services}/*.desktop
%{_kde_appsdir}/ktexteditor_klf
%{_kde_datadir}/mime/packages/*.xml
%{_kde_datadir}/pixmaps/*.png

%files -n %libname
%defattr(-,root,root)
%{_kde_libdir}/*.so.*

%files -n %develname
%defattr(-,root,root)
%{_kde_includedir}/*
%{_kde_libdir}/*.so


%changelog
* Thu May 10 2012 Lev Givon <lev@mandriva.org> 3.2.5-1
+ Revision: 798101
- Update to 3.2.5.

* Mon Jul 11 2011 Lev Givon <lev@mandriva.org> 3.2.4-1
+ Revision: 689507
- Update to 3.2.4.

  + Funda Wang <fwang@mandriva.org>
    - new version 3.2.3

* Sun Dec 05 2010 Funda Wang <fwang@mandriva.org> 3.2.2-1mdv2011.0
+ Revision: 609867
- update to new version 3.2.2

* Mon Oct 04 2010 Funda Wang <fwang@mandriva.org> 3.2.1-1mdv2011.0
+ Revision: 582928
- new version 3.2.1

* Thu Sep 30 2010 Funda Wang <fwang@mandriva.org> 3.2.0-1mdv2011.0
+ Revision: 582158
- New version 3.2.0

* Sun Nov 29 2009 Lev Givon <lev@mandriva.org> 3.1.2-1mdv2010.1
+ Revision: 471555
- Update to 3.1.2.

* Thu May 28 2009 Lev Givon <lev@mandriva.org> 3.0.1-3mdv2010.0
+ Revision: 380447
- Add patch from author to make symbol/library windows be displayed as
  top-level objects.

* Thu May 07 2009 Lev Givon <lev@mandriva.org> 3.0.1-2mdv2010.0
+ Revision: 372956
- Require ghostscript, tetex-latex, and tetex-dvips.

* Mon May 04 2009 Funda Wang <fwang@mandriva.org> 3.0.1-1mdv2010.0
+ Revision: 371541
- import klatexformula


