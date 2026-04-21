%bcond clang 1

# Default version for this component
%define tde_pkg tdeknighttour
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif

# TDE specific building variables
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Summary:		A logic game for TDE
Version:		0.1.0
Release:		%{?tde_version:%{tde_version}_}3

License:		GPLv2+
Group:			Applications/Utilities


URL:			http://www.trinitydesktop.org/

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/games/%{tarball_name}-%{tde_version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DDATA_INSTALL_DIR=%{tde_prefix}/share/apps
BuildOption:    -DBUILD_ALL=ON

BuildRequires:	pkgconfig(tqt)
BuildRequires:	trinity-arts-devel >= 1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	trinity-tdegames-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	libtool

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
A knight's tour is a sequence of moves of a knight on a chessboard such that 
the knight visits every square exactly once. If the knight ends on a square 
that is one knight's move from the beginning square (so that it could tour 
the board again immediately, following the same path), the tour is closed 
(or re-entrant); otherwise, it is open.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"

%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYRIGHT README.md
%{tde_prefix}/bin/knighttour
%{tde_prefix}/share/applications/tde/knighttour.desktop

