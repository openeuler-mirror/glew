Name:           glew
Version:        2.1.0
Release:        5
Summary:        The OpenGL Extension Wrangler Library
License:        BSD-3-Clause and MIT
URL:            http://glew.sourceforge.net

Source0:        https://sourceforge.net/projects/glew/files/glew/%{version}/glew-%{version}.tgz
Patch0000:      glew-2.1.0-install.patch
BuildRequires:  libGLU-devel gcc

Provides:       libGLEW = %{version}-%{release}
Obsoletes:      libGLEW < %{version}-%{release}

%description
OpenGL Extension Wrangler Library (GLEW) is a cross-platform
extension loading library for c / c ++.
GLEW provides a runtime mechanism for determining
which OpenGL extensions are supported on the platform.
The OpenGL core and extensions are exposed in a single header file.
GLEW can be used on a variety of operating systems,
including Windows, Linux, Irix, Solaris, Mac OS X, FreeBSD.
This package contains the demo GLEW program.
The libraries themselves are in libGLEW

%package devel
Summary:        Development files for glew
Requires:       %{name} = %{version}-%{release} mesa-libGLU-devel

%description devel
Development files for glew

%prep
%autosetup -n %{name}-%{version} -p1

cp /usr/lib/rpm/%{_vendor}/config.guess config/

%build
%make_build CFLAGS.EXTRA="$RPM_OPT_FLAGS -fPIC" includedir=%{_includedir} STRIP= LIBDIR=%{_libdir} PKGDIR=%{_libdir}/pkgconfig

%install
make install.all DESTDIR="$RPM_BUILD_ROOT" LIBDIR=%{_libdir} PKGDIR=%{_libdir}/pkgconfig
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/*.so*
%delete_la_and_a

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%license LICENSE.txt
%{_bindir}/*
%{_libdir}/libGLEW.so.*

%files devel
%{_libdir}/libGLEW.so
%{_libdir}/pkgconfig//glew.pc
%{_includedir}/GL/*.h
%doc doc/*

%changelog
* Tue May 10 2022 xu_ping<xuping33@h-partners.com> - 2.1.0-5
- License compliance rectification

* Wed Jun 2 2021 baizhonggui <baizhonggui@huawei.com> - 2.1.0-4
- Fixed make: cc: No such file or directory
- Add gcc in BuildRequires

* Wed Nov 20 2019 yangjian<yangjian79@huawei.com> - 2.1.0-3
- Package init
