%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6Baloo
%define devname %mklibname KF6Baloo -d
#define git 20240217

Name: kf6-baloo
Version: 6.14.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/baloo/-/archive/master/baloo-master.tar.bz2#/baloo-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/frameworks/%{major}/baloo-%{version}.tar.xz
%endif
Summary: Baloo is the file indexing and file search framework for KDE Plasma
URL: https://invent.kde.org/frameworks/baloo
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6Quick)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6IdleTime)
BuildRequires: cmake(KF6FileMetaData)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6KIO)
BuildRequires: pkgconfig(lmdb)
Requires: %{libname} = %{EVRD}

%description
Baloo is the file indexing and file search framework for KDE Plasma.

%package -n %{libname}
Summary: Baloo is the file indexing and file search framework for KDE Plasma
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Baloo is the file indexing and file search framework for KDE Plasma.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Baloo is the file indexing and file search framework for KDE Plasma.

%prep
%autosetup -p1 -n baloo-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/baloo.*
%{_sysconfdir}/xdg/autostart/baloo_file.desktop
%{_bindir}/balooctl6
%{_bindir}/baloosearch6
%{_bindir}/balooshow6
%{_prefix}/lib/systemd/user/kde-baloo.service
%{_datadir}/dbus-1/interfaces/org.kde.BalooWatcherApplication.xml
%{_datadir}/dbus-1/interfaces/org.kde.baloo.file.indexer.xml
%{_datadir}/dbus-1/interfaces/org.kde.baloo.fileindexer.xml
%{_datadir}/dbus-1/interfaces/org.kde.baloo.main.xml
%{_datadir}/dbus-1/interfaces/org.kde.baloo.scheduler.xml

%files -n %{devname}
%{_includedir}/KF6/Baloo
%{_libdir}/cmake/KF6Baloo
%{_qtdir}/doc/KF6Baloo.*
%{_libdir}/pkgconfig/KF6Baloo.pc

%files -n %{libname}
%{_libdir}/libKF6Baloo.so*
%{_libdir}/libKF6BalooEngine.so*
%{_libdir}/libexec/kf6/baloo_file
%{_libdir}/libexec/kf6/baloo_file_extractor
%{_qtdir}/plugins/kf6/kded/*
%{_qtdir}/plugins/kf6/kio/*
%{_qtdir}/qml/org/kde/baloo
