#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : widgetsnbextension
Version  : 3.5.1
Release  : 53
URL      : https://files.pythonhosted.org/packages/e0/c4/b7211bfc8e998fe55764539d2b169fb200e6427dfe4e62d1d83013caa9ef/widgetsnbextension-3.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/e0/c4/b7211bfc8e998fe55764539d2b169fb200e6427dfe4e62d1d83013caa9ef/widgetsnbextension-3.5.1.tar.gz
Summary  : IPython HTML widgets for Jupyter
Group    : Development/Tools
License  : BSD-3-Clause
Requires: widgetsnbextension-data = %{version}-%{release}
Requires: widgetsnbextension-license = %{version}-%{release}
Requires: widgetsnbextension-python = %{version}-%{release}
Requires: widgetsnbextension-python3 = %{version}-%{release}
Requires: notebook
BuildRequires : buildreq-distutils3
BuildRequires : notebook
Patch1: change-widgetsnbextension-json-path.patch

%description
No detailed description available

%package data
Summary: data components for the widgetsnbextension package.
Group: Data

%description data
data components for the widgetsnbextension package.


%package license
Summary: license components for the widgetsnbextension package.
Group: Default

%description license
license components for the widgetsnbextension package.


%package python
Summary: python components for the widgetsnbextension package.
Group: Default
Requires: widgetsnbextension-python3 = %{version}-%{release}

%description python
python components for the widgetsnbextension package.


%package python3
Summary: python3 components for the widgetsnbextension package.
Group: Default
Requires: python3-core
Provides: pypi(widgetsnbextension)
Requires: pypi(notebook)

%description python3
python3 components for the widgetsnbextension package.


%prep
%setup -q -n widgetsnbextension-3.5.1
cd %{_builddir}/widgetsnbextension-3.5.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603408089
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/widgetsnbextension
cp %{_builddir}/widgetsnbextension-3.5.1/LICENSE %{buildroot}/usr/share/package-licenses/widgetsnbextension/5dc7e0ef3878c3d4a92a7233208e6f91553de266
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/nbextensions/jupyter-js-widgets/extension.js
/usr/share/jupyter/nbextensions/jupyter-js-widgets/extension.js.map
/usr/share/jupyter/nbextensions/nbconfig/notebook.d/widgetsnbextension.json

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/widgetsnbextension/5dc7e0ef3878c3d4a92a7233208e6f91553de266

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
