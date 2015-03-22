%define pkgname sprockets
Summary:	Rack-based asset packaging system
Name:		ruby-%{pkgname}
Version:	2.2.2
Release:	3
License:	MIT
Group:		Development/Libraries
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	9d3c57814c21111357ff5c933ae0901c
URL:		http://github.com/brynary/rack-test
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
Requires:	ruby-hike >= 1.2
Requires:	ruby-multi_json >= 1.0
Requires:	ruby-rack >= 1.0
Requires:	ruby-tilt >= 1.1
Conflicts:	ruby-hike >= 2.0
Conflicts:	ruby-multi_json >= 2.0
Conflicts:	ruby-rack >= 2.0
Conflicts:	ruby-tilt >= 2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sprockets is a Rack-based asset packaging system that concatenates and
serves JavaScript, CoffeeScript, CSS, LESS, Sass, and SCSS.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

rdoc --ri --op ri lib
rdoc --op rdoc lib
rm ri/created.rid
rm ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{ruby_vendorlibdir}/sprockets
%{ruby_vendorlibdir}/sprockets.rb
#%{ruby_vendorlibdir}/rake/sprocketstask.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Sprockets
