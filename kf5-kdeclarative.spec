#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.107
%define		qtver		5.15.2
%define		kfname		kdeclarative

Summary:	Integration of QML and KDE work spaces
Name:		kf5-%{kfname}
Version:	5.107.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	52eb0b49ba27dcde5b1646feafb86749
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-attica-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-kauth-devel >= %{version}
BuildRequires:	kf5-kbookmarks-devel >= %{version}
BuildRequires:	kf5-kcodecs-devel >= %{version}
BuildRequires:	kf5-kcompletion-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kconfigwidgets-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kdbusaddons-devel >= %{version}
BuildRequires:	kf5-kglobalaccel-devel >= %{version}
BuildRequires:	kf5-kguiaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kiconthemes-devel >= %{version}
BuildRequires:	kf5-kio-devel >= %{version}
BuildRequires:	kf5-kitemviews-devel >= %{version}
BuildRequires:	kf5-kjobwidgets-devel >= %{version}
BuildRequires:	kf5-kpackage-devel >= %{version}
BuildRequires:	kf5-kservice-devel >= %{version}
BuildRequires:	kf5-ktextwidgets-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf5-kwindowsystem-devel >= %{version}
BuildRequires:	kf5-kxmlgui-devel >= %{version}
BuildRequires:	kf5-solid-devel >= %{version}
BuildRequires:	kf5-sonnet-devel >= %{version}
BuildRequires:	libepoxy-devel
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KDeclarative provides integration of QML and KDE work spaces.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kf5-kconfig-devel
Requires:	kf5-kpackage-devel

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}5

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/kpackagelauncherqml
%ghost %{_libdir}/libKF5CalendarEvents.so.5
%attr(755,root,root) %{_libdir}/libKF5CalendarEvents.so.5.*.*
%ghost %{_libdir}/libKF5Declarative.so.5
%attr(755,root,root) %{_libdir}/libKF5Declarative.so.*.*
%ghost %{_libdir}/libKF5QuickAddons.so.5
%attr(755,root,root) %{_libdir}/libKF5QuickAddons.so.*.*
%{_libdir}/qt5/qml/org/kde/kio/qmldir
%attr(755,root,root) %{qt5dir}/qml/org/kde/kio/libkio.so
%{_libdir}/qt5/qml/org/kde/kwindowsystem/qmldir
%attr(755,root,root) %{qt5dir}/qml/org/kde/kwindowsystem/libkwindowsystem.so
%attr(755,root,root) %{qt5dir}/qml/org/kde/draganddrop/libdraganddropplugin.so
%{qt5dir}/qml/org/kde/draganddrop/qmldir
%attr(755,root,root) %{qt5dir}/qml/org/kde/kcoreaddons/libkcoreaddonsplugin.so
%{qt5dir}/qml/org/kde/kcoreaddons/qmldir
%{qt5dir}/qml/org/kde/kquickcontrols/ColorButton.qml
%{qt5dir}/qml/org/kde/kquickcontrols/KeySequenceItem.qml
%{qt5dir}/qml/org/kde/kquickcontrols/qmldir
%attr(755,root,root) %{qt5dir}/qml/org/kde/kquickcontrolsaddons/libkquickcontrolsaddonsplugin.so
%{qt5dir}/qml/org/kde/kquickcontrolsaddons/qmldir
%attr(755,root,root) %{qt5dir}/qml/org/kde/private/kquickcontrols/libkquickcontrolsprivateplugin.so
%{qt5dir}/qml/org/kde/private/kquickcontrols/qmldir
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/kconfig/libkconfigplugin.so
%{_libdir}/qt5/qml/org/kde/kconfig/qmldir
%dir %{_libdir}/qt5/qml/org/kde/kcm
%{_libdir}/qt5/qml/org/kde/kcm/GridDelegate.qml
%{_libdir}/qt5/qml/org/kde/kcm/GridView.qml
%{_libdir}/qt5/qml/org/kde/kcm/GridViewKCM.qml
%{_libdir}/qt5/qml/org/kde/kcm/SimpleKCM.qml
%{_libdir}/qt5/qml/org/kde/kcm/libkcmcontrolsplugin.so
%dir %{_libdir}/qt5/qml/org/kde/kcm/private
%{_libdir}/qt5/qml/org/kde/kcm/private/GridViewInternal.qml
%{_libdir}/qt5/qml/org/kde/kcm/qmldir
%{_libdir}/qt5/qml/org/kde/kcm/ScrollView.qml
%{_libdir}/qt5/qml/org/kde/kcm/ScrollViewKCM.qml
%{_libdir}/qt5/qml/org/kde/kcm/AbstractKCM.qml
%{_libdir}/qt5/qml/org/kde/kcm/SettingHighlighter.qml
%{_libdir}/qt5/qml/org/kde/kcm/SettingStateBinding.qml
%{_libdir}/qt5/qml/org/kde/kcm/ContextualHelpButton.qml
%dir %{_libdir}/qt5/qml/org/kde/graphicaleffects
%{_libdir}/qt5/qml/org/kde/graphicaleffects/Lanczos.qml
%{_libdir}/qt5/qml/org/kde/graphicaleffects/lanczos2sharp.frag
%{_libdir}/qt5/qml/org/kde/graphicaleffects/lanczos2sharp_core.frag
%{_libdir}/qt5/qml/org/kde/graphicaleffects/preserveaspect.vert
%{_libdir}/qt5/qml/org/kde/graphicaleffects/preserveaspect_core.vert
%{_libdir}/qt5/qml/org/kde/graphicaleffects/qmldir

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KDeclarative
%{_libdir}/cmake/KF5Declarative
%{_libdir}/libKF5CalendarEvents.so
%{_libdir}/libKF5Declarative.so
%{_libdir}/libKF5QuickAddons.so
%{qt5dir}/mkspecs/modules/qt_KDeclarative.pri
%{qt5dir}/mkspecs/modules/qt_QuickAddons.pri
