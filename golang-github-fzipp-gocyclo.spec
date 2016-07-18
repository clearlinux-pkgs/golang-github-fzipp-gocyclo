Name     : golang-github-fzipp-gocyclo
Version  : 6acd4345c835499920e8426c7e4e8d7a34f1bb83
Release  : 1
URL      : https://github.com/fzipp/gocyclo/archive/6acd4345c835499920e8426c7e4e8d7a34f1bb83.tar.gz
Source0  : https://github.com/fzipp/gocyclo/archive/6acd4345c835499920e8426c7e4e8d7a34f1bb83.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires : go

%description
Gocyclo calculates cyclomatic complexities of functions in Go source code.
The cyclomatic complexity of a function is calculated according to the
following rules:

%prep
%setup -q -n gocyclo-6acd4345c835499920e8426c7e4e8d7a34f1bb83

%build
export LANG=C

%install
gopath="/usr/lib/golang"
library_path="github.com/fzipp/gocyclo"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/fzipp/gocyclo/gocyclo.go
