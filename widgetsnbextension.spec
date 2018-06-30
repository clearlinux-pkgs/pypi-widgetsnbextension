#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : widgetsnbextension
Version  : 3.2.1
Release  : 30
URL      : https://pypi.python.org/packages/da/c4/53da2ddb67be3610e985f9b1ffa8cce45cef2ef3b8d2cd42009235394a65/widgetsnbextension-3.2.1.tar.gz
Source0  : https://pypi.python.org/packages/da/c4/53da2ddb67be3610e985f9b1ffa8cce45cef2ef3b8d2cd42009235394a65/widgetsnbextension-3.2.1.tar.gz
Summary  : IPython HTML widgets for Jupyter
Group    : Development/Tools
License  : BSD-3-Clause
Requires: widgetsnbextension-python3
Requires: widgetsnbextension-data
Requires: widgetsnbextension-python
Requires: notebook
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: change-widgetsnbextension-json-path.patch

%description
No detailed description available

%package data
Summary: data components for the widgetsnbextension package.
Group: Data

%description data
data components for the widgetsnbextension package.


%package python
Summary: python components for the widgetsnbextension package.
Group: Default
Requires: widgetsnbextension-python3

%description python
python components for the widgetsnbextension package.


%package python3
Summary: python3 components for the widgetsnbextension package.
Group: Default
Requires: python3-core

%description python3
python3 components for the widgetsnbextension package.


%prep
%setup -q -n widgetsnbextension-3.2.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529094264
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
