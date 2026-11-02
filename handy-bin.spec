%global upstream_release 1

Name:           handy-bin
Version:        0.10.0
Release:        1%{?dist}
Summary:        Offline speech-to-text application (upstream binary package)

License:        MIT
URL:            https://github.com/cjpais/Handy
Source0:        %{url}/releases/download/v%{version}/Handy-%{version}-%{upstream_release}.%{_arch}.rpm
Source1:        https://raw.githubusercontent.com/cjpais/Handy/v%{version}/LICENSE

ExclusiveArch:  x86_64 aarch64
BuildRequires:  cpio
BuildRequires:  rpm
Requires:       libappindicator-gtk3
Provides:       handy = %{version}-%{release}
Conflicts:      handy

# Keep the prebuilt, upstream-tested binaries intact.
%global debug_package %{nil}
%global __strip /bin/true

%description
Handy is a cross-platform, offline speech-to-text application. This package
repackages the architecture-specific RPM published with the corresponding
upstream stable release.


%prep
%setup -q -c -T
rpm2cpio %{SOURCE0} | cpio -idmu


%build
# The application is built and published by upstream.


%install
mkdir -p %{buildroot}
cp -a usr %{buildroot}/
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_licensedir}/%{name}/LICENSE


%files
%license %{_licensedir}/%{name}/LICENSE
%{_bindir}/handy
%{_prefix}/lib/Handy/
%{_datadir}/applications/Handy.desktop
%{_datadir}/icons/hicolor/*/apps/handy.png


%changelog
* Mon Nov 02 2026 Ponesicek <ponesicek@users.noreply.github.com> - 0.10.0-1
- Package upstream Handy 0.10.0 binary release
* Sat Oct 03 2026 Ponesicek <ponesicek@users.noreply.github.com> - 0.9.8-1
- Package upstream Handy 0.9.8 binary release
* Fri Sep 18 2026 Ponesicek <ponesicek@users.noreply.github.com> - 0.9.7-1
- Package upstream Handy 0.9.7 binary release
* Mon Aug 24 2026 Ponesicek <ponesicek@users.noreply.github.com> - 0.9.6-1
- Package upstream Handy 0.9.6 binary release
* Wed Aug 12 2026 Ponesicek <ponesicek@users.noreply.github.com> - 0.9.5-1
- Package upstream Handy 0.9.5 binary release
* Fri Jul 31 2026 Ponesicek <ponesicek@users.noreply.github.com> - 0.9.4-1
- Package upstream Handy 0.9.4 binary release
