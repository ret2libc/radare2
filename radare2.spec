# by default it builds from the released version of radare2
%bcond_without  build_release

Name:           radare2
Summary:        The reverse engineering framework
Version:        2.9.0
URL:            https://radare.org/
VCS:            https://github.com/radare/radare2

%global         gituser         radare
%global         gitname         radare2

%global         gitdate         20180904
%global         commit          00144a348c47802f203e5de9add609ea1b0808e4
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})

%global         rel              1

%if %{with build_release}
Release:        %{rel}%{?dist}
Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
Release:        0.%{rel}.%{gitdate}git%{shortcommit}%{?dist}
Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
%endif

License:        LGPLv3+ and GPLv2+ and BSD and MIT and ASLv2.0 and MPLv2.0 and zlib
# Radare2 as a package is targeting to be licensed/compiled as LGPLv3+
# during build for Fedora the GPL code is not omitted so effectively it is GPLv2+
# some code has originally different license:
# libr/asm/arch/ - GPLv2+, MIT, GPLv3
# libr/bin/format/pe/dotnet - Apache License Version 2.0
# libr/hash/xxhash.c - 2 clause BSD
# libr/util/qrcode.c - MIT
# shlr/grub/grubfs.c - LGPL
# shlr/java - Apache 2.0
# shlr/sdb/src - MIT
# shlr/lz4 - 3 clause BSD (system installed shared lz4 is used instead)
# shlr/spp - MIT
# shlr/squashfs/src - GPLv2+
# shlr/tcc - LGPLv2+
# shlr/udis86 - 2 clause BSD
# shlr/wind - LGPL v3+
# shlr/spp - MIT
# shlr/zip/zlib - zlib/libpng License (system installed shared libzip is used instead)
# shlr/zip/zip - 3 clause BSD (system installed shared zlib is used instead)

# Removed from the final package because of the presence of minified JS and
# absence of the source JS - this should be packaged with radare2-webui
# shlr/www/m - Apache-2.0
# shlr/www/enyo/vendors/jquery-ui.min.js - GPL + MIT
# shlr/www/enyo/vendors/jquery.layout-latest.min.js - GPL + MIT
# shlr/www/enyo/vendors/jquery.scrollTo.min.js - MIT
# shlr/www/enyo/vendors/lodash.min.js - lodash license
# shlr/www/enyo/vendors/joint.* - Mozilla MPL 2.0
# shlr/www/enyo/vendors/jquery.min.js - Apache License version 2.0
# shlr/www/p/vendors/jquery* - GPL + MIT
# shlr/www/p/vendors/dagre*|graphlib* - 3 clause BSD
# shlr/www/p/vendors/jquery.onoff.min.js - MIT

%if %{!with build_release}
BuildRequires:  sed
%endif

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  bzip2-devel
BuildRequires:  file-devel
BuildRequires:  libzip-devel
BuildRequires:  zlib-devel
BuildRequires:  lz4-devel
BuildRequires:  capstone-devel >= 3.0.4

Requires:       %{name}-common = %{version}-%{release}

# Package contains several bundled libraries

# ./shlr/zip/zlib/README
# compiled with -D use_sys_zip=true and -D use_sys_zlib=true instead

# ./shlr/lz4/README.md
# compiled with -D use_sys_lz4=true instead

# ./libr/magic/README
# compiled with -D use_sys_magic=true instead

# ./shlr/capstone.sh
# compiled with -D use_sys_capstone=true instead

# ./libr/hash/xxhash.*
# compiled with -D use_sys_xxhash=true instead

# ./libr/hash/{md4,md5,sha1,sha2}.{c,h}
# compiled with -D use_sys_openssl=true instead

# ./shlr/spp/README.md
# SPP stands for Simple Pre-Processor, a templating language.
# https://github.com/radare/spp
Provides:       bundled(spp) = 1.0

# ./shlr/sdb/README.md
# sdb is a simple string key/value database based on djb's cdb
# https://github.com/radare/sdb
Provides:       bundled(sdb) = 1.2.0

# ./shlr/sdb/src/json/README
# https://github.com/quartzjer/js0n
# JSON support for sdb
Provides:       bundled(js0n)

# libr/util/regex/README
# Modified OpenBSD regex to be portable
# cvs -qd anoncvs@anoncvs.ca.openbsd.org:/cvs get -P src/lib/libc/regex
# version from 2010/11/21 00:02:30, version of files ranges from v1.11 to v1.20
Provides:       bundled(openbsdregex) = 1.11

# ./shlr/tcc/README.md
# This is a stripped down version of tcc without the code generators and heavily modified.
Provides:       bundled(tcc) = 0.9.26

# ./libr/asm/arch/tricore/README.md
# Based on code from https://www.hightec-rt.com/en/downloads/sources/14-sources-for-tricore-v3-3-7-9-binutils-1.html
# part of binutils to read machine code for Tricore architecture
# ./libr/asm/arch/ppc/gnu/
# part of binutils to read machine code for ppc architecture
# ./libr/asm/arch/arm/gnu/
Provides:       bundled(binutils) = 2.13

# ./libr/asm/arch/avr/README
# * This code has been ripped from vavrdisasm 1.6
Provides:       bundled(vavrdisasm) = 1.6

# ./shlr/grub/*
# It is not clear which version has been copied
Provides:       bundled(grub2)


%description
The radare2 is a reverse-engineering framework that is multi-architecture,
multi-platform, and highly scriptable.  Radare2 provides a hexadecimal
editor, wrapped I/O, file system support, debugger support, diffing
between two functions or binaries, and code analysis at opcode,
basic block, and function levels.


%package devel
Summary:        Development files for the radare2 package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for the radare2 package. See radare2 package for more
information.


%package common
Summary:        Arch-independent SDB files for the radare2 package
BuildArch:      noarch
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description common
Arch-independent SDB files used by radare2 package. See radare2 package for more
information


%prep
%if %{with build_release}
# Build from git release version
%setup -q -n %{gitname}-%{version}
%else
# Build from git commit
%setup -q -n %{gitname}-%{commit}
# Rename internal "version-git" to "version"
sed -i -e "s|%{version}-git|%{version}|g;" configure configure.acr
%endif
# Removing some fortunes because inappropriate
rm doc/fortunes.{creepy,nsfw,fun}
# Removing zip/lzip and lz4 files because we use system dependencies
rm -rf shlr/zip shlr/lz4

# Webui contains pre-build and/or minimized versions of JS libraries without source code
# Consider installing the web-interface from https://github.com/radare/radare2-webui
rm -rf ./shlr/www/*
echo "The radare2 source usually comes with a pre-built version of the web-interface, but without the source code" > ./shlr/www/README.Fedora
echo "This has been removed in the Fedora package to follow the Fedora Packaging Guidelines." >> ./shlr/www/README.Fedora
echo "Available under https://github.com/radare/radare2-webui" >> ./shlr/www/README.Fedora


%build
# Whereever possible use the system-wide libraries instead of bundles
%meson \
    -Duse_sys_capstone=true \
    -Duse_sys_magic=true \
    -Duse_sys_zip=true \
    -Duse_sys_zlib=true \
    -Duse_sys_lz4=true \
    -Duse_sys_xxhash=true \
    -Duse_sys_openssl=true
%meson_build

%install
%meson_install
# removing r2pm because it is a package manager which could install packages
# system wide or in the user home directory
rm %{buildroot}/%{_bindir}/r2pm
# create r2 symlink because meson build does not create it (yet)
ln -s radare2 %{buildroot}/%{_bindir}/r2

%ldconfig_scriptlets


%check
# Do not run the testsuite yet - it pulls another package
# https://github.com/radare/radare2-regressions from github make tests



%files
%doc AUTHORS.md CONTRIBUTING.md DEVELOPERS.md README.md
%doc doc/3D/ doc/node.js/ doc/pdb/ doc/sandbox/
%doc doc/avr.md doc/brainfuck.md doc/calling-conventions.md doc/debug.md
%doc doc/esil.md doc/gdb.md doc/gprobe.md doc/intro.md doc/io.md doc/rap.md
%doc doc/siol.md doc/strings.md doc/windbg.md doc/yara.md
# Webui removed cuz of having minified js code and missing source code
%doc %{_datadir}/%{name}/%{version}/www/README.Fedora
%license COPYING COPYING.LESSER
%{_bindir}/r*
%{_libdir}/libr_*.so.2.9.*
%{_mandir}/man1/r*.1.*
%{_mandir}/man7/esil.7.*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{version}
%dir %{_datadir}/%{name}/%{version}/www


%files devel
%{_includedir}/libr
%{_libdir}/libr*.so
%{_libdir}/pkgconfig/*.pc


%files common
%{_datadir}/%{name}/%{version}/cons
%{_datadir}/%{name}/%{version}/fcnsign
%{_datadir}/%{name}/%{version}/flag
%{_datadir}/%{name}/%{version}/format
%{_datadir}/%{name}/%{version}/hud
%{_datadir}/%{name}/%{version}/magic
%{_datadir}/%{name}/%{version}/opcodes
%{_datadir}/%{name}/%{version}/syscall
%{_datadir}/doc/%{name}/fortunes.*
%dir %{_datadir}/%{name}
%dir %{_datadir}/doc/%{name}


%changelog
* Tue Sep 4 2018 Riccardo Schirone <rschirone91@gmail.com> 2.9.0-1
- use system xxhash and openssl
- bump to 2.9.0 release
- use bcond_without to choose between release build or git one
- add gcc as BuildRequires
- do not directly call ldconfig but use RPM macros

* Fri Aug 3 2018 Riccardo Schirone <rschirone91@gmail.com> 2.8.0-0.2.20180718git51e2936
- add grub2 and xxhash Provides
- add some license comments
- move SDB files in -common subpackage

* Mon Jul 16 2018 Riccardo Schirone <rschirone91@gmail.com> 2.8.0-0.1.20180718git51e2936
- bump to 2.8.0 version and switch to meson

* Fri Apr 13 2018 Michal Ambroz <rebus at, seznam.cz> 2.5.0-1
- bump to 2.5.0 release

* Sun Feb 11 2018 Michal Ambroz <rebus at, seznam.cz> 2.4.0-1
- bump to 2.4.0 release

* Mon Feb 05 2018 Michal Ambroz <rebus at, seznam.cz> 2.3.0-1
- bump to 2.3.0 release
- drop the web-interface for now

* Tue Nov 14 2017 Michal Ambroz <rebus at, seznam.cz> 2.0.1-1
- bump to 2.0.1 release

* Fri Aug 04 2017 Michal Ambroz <rebus at, seznam.cz> 1.6.0-1
- bump to 1.6.0 release

* Thu Jun 08 2017 Michal Ambroz <rebus at, seznam.cz> 1.5.0-1
- bump to 1.5.0 release

* Sun Apr 23 2017 Michal Ambroz <rebus at, seznam.cz> 1.4.0-1
- bump to 1.4.0 release

* Sat Mar 18 2017 Michal Ambroz <rebus at, seznam.cz> 1.3.0-1
- bump to 1.3.0 release

* Sat Feb 18 2017 Michal Ambroz <rebus at, seznam.cz> 1.3.0-0.1.gita37af19
- switch to git version fixing sigseg in radiff2

* Wed Feb 08 2017 Michal Ambroz <rebus at, seznam.cz> 1.2.1-1
- bump to 1.2.1
- removed deprecated post postun calling of /sbin/ldconfig

* Sat Oct 22 2016 Michal Ambroz <rebus at, seznam.cz> 0.10.6-1
- bump to 0.10.6

* Sun Aug 21 2016 Michal Ambroz <rebus at, seznam.cz> 0.10.5-1
- bump to 0.10.5

* Mon Aug 01 2016 Michal Ambroz <rebus at, seznam.cz> 0.10.4-1
- bump to 0.10.4

* Sun Jun 05 2016 Michal Ambroz <rebus at, seznam.cz> 0.10.3-1
- build for Fedora for release of 0.10.3

* Mon Apr 25 2016 Michal Ambroz <rebus at, seznam.cz> 0.10.2-1
- build for Fedora for release of 0.10.2

* Thu Jan 21 2016 Michal Ambroz <rebus at, seznam.cz> 0.10.0-2
- build for Fedora for release of 0.10.0

* Sat Oct 10 2015 Michal Ambroz <rebus at, seznam.cz> 0.10.0-1
- build for Fedora for alpha of 0.10.0

* Sun Nov 09 2014 Pavel Odvody <podvody@redhat.com> 0.9.8rc3-0
- initial radare2 package
