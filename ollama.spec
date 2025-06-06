#
# Using build pattern: cmake
#
Name     : ollama
Version  : 0.9.0
Release  : 8
URL      : https://github.com/ollama/ollama/archive/refs/tags/v0.9.0.tar.gz
Source0  : https://github.com/ollama/ollama/archive/refs/tags/v0.9.0.tar.gz
Source1  : http://localhost/cgit/projects/ollama-vendor/snapshot/ollama-vendor-0.1.tar.gz
Source2  : ollama.service

Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: ollama-lib = %{version}-%{release}
Requires: ollama-bin = %{version}-%{release}
Requires: ollama-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : glibc-dev
BuildRequires : openblas
BuildRequires : pkg-config
BuildRequires : pkgconfig(openblas)
BuildRequires : buildreq-golang
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description

%package lib
Summary: lib components for the ollama package.
Group: Libraries
Requires: ollama-license = %{version}-%{release}

%description lib

%package bin
Summary: lbin components for the ollama package.
Group: Libraries
Requires: ollama-license = %{version}-%{release}

%description bin
lib components for the ollama package.


%package license
Summary: license components for the ollama package.
Group: Default

%description license
license components for the ollama package.


%prep
%setup -q -n ollama-0.9.0
cd %{_builddir}/ollama-0.9.0
tar xf %{_sourcedir}/ollama-vendor-0.1.tar.gz
mv ollama-vendor-0.1/vendor .

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1749138018

mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
#%cmake ..   -G 'Unix Makefiles'
#make  %{?_smp_mflags}
popd

export  CGO_ENABLED=1
unset CLEAR_DEBUG_TERSE
export GOAMD64=v3
CXXFLAGS="$CXXFLAGS -O3 -march=x86-64-v3"
CGO_CPPFLAGS="$CXXFLAGS"
export CXX="/usr/bin/g++ -O3 -march=x86-64-v3"
go build -v  -tags "avx,avx2"



%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1749138018
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ollama
cp %{_builddir}/ollama-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/ollama/d4f3ba2fbf9cad2020105ee33123c1be60d29f59 || :
cp %{_builddir}/ollama-%{version}/llama/llama.cpp/LICENSE %{buildroot}/usr/share/package-licenses/ollama/fe2abc0422badd844ef61006dd764836b5ebd6a7 || :
cp %{_builddir}/ollama-%{version}/ml/backend/ggml/ggml/LICENSE %{buildroot}/usr/share/package-licenses/ollama/fe2abc0422badd844ef61006dd764836b5ebd6a7 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
popd
mkdir -p %{buildroot}/usr/bin
cp ollama  %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/ollama.service

%files
%defattr(-,root,root,-)
/usr/lib/systemd/system/ollama.service


%files bin
/usr/bin/ollama

%files lib
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ollama/d4f3ba2fbf9cad2020105ee33123c1be60d29f59
/usr/share/package-licenses/ollama/fe2abc0422badd844ef61006dd764836b5ebd6a7
