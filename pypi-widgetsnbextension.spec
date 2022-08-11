#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-widgetsnbextension
Version  : 3.6.1
Release  : 73
URL      : https://files.pythonhosted.org/packages/3c/9c/a6ddc7ef107a0fa96ba8acb3b272293a517c929a9f61536434706bb38942/widgetsnbextension-3.6.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/3c/9c/a6ddc7ef107a0fa96ba8acb3b272293a517c929a9f61536434706bb38942/widgetsnbextension-3.6.1.tar.gz
Summary  : IPython HTML widgets for Jupyter
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-widgetsnbextension-data = %{version}-%{release}
Requires: pypi-widgetsnbextension-license = %{version}-%{release}
Requires: pypi-widgetsnbextension-python = %{version}-%{release}
Requires: pypi-widgetsnbextension-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(notebook)
Patch1: change-widgetsnbextension-json-path.patch

%description
No detailed description available

%package data
Summary: data components for the pypi-widgetsnbextension package.
Group: Data

%description data
data components for the pypi-widgetsnbextension package.


%package license
Summary: license components for the pypi-widgetsnbextension package.
Group: Default

%description license
license components for the pypi-widgetsnbextension package.


%package python
Summary: python components for the pypi-widgetsnbextension package.
Group: Default
Requires: pypi-widgetsnbextension-python3 = %{version}-%{release}

%description python
python components for the pypi-widgetsnbextension package.


%package python3
Summary: python3 components for the pypi-widgetsnbextension package.
Group: Default
Requires: python3-core
Provides: pypi(widgetsnbextension)
Requires: pypi(notebook)

%description python3
python3 components for the pypi-widgetsnbextension package.


%prep
%setup -q -n widgetsnbextension-3.6.1
cd %{_builddir}/widgetsnbextension-3.6.1
%patch1 -p1
pushd ..
cp -a widgetsnbextension-3.6.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656361552
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-widgetsnbextension
cp %{_builddir}/widgetsnbextension-3.6.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-widgetsnbextension/5dc7e0ef3878c3d4a92a7233208e6f91553de266
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/nbextensions/jupyter-js-widgets/extension.js
/usr/share/jupyter/nbextensions/jupyter-js-widgets/extension.js.map
/usr/share/jupyter/nbextensions/nbconfig/notebook.d/widgetsnbextension.json

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-widgetsnbextension/5dc7e0ef3878c3d4a92a7233208e6f91553de266

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
