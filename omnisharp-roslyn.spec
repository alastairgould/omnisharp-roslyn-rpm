%global _prefix /opt

Name:          omnisharp-roslyn
Version:       1.28.0
Release:       1%{?dist}
Summary:       OmniSharp-Roslyn is a .NET development platform based on Roslyn workspaces. It provides project dependencies and language syntax to various IDE and plugins.
Group:         Development Tools

URL:           https://github.com/OmniSharp/omnisharp-roslyn
License:       MIT
Source0:       https://github.com/OmniSharp/omnisharp-roslyn/releases/download/v%{version}/omnisharp-linux-x64.tar.gz
ExclusiveArch: x86_64

Autoreq: 0

%description
OmniSharp-Roslyn is a .NET development platform based on Roslyn workspaces. 
It provides project dependencies and language syntax to various IDE and plugins.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_prefix}/%{name}
tar -xf %{SOURCE0} --directory %{buildroot}/%{_prefix}/%{name}/ --mode=755


%files
/%{_prefix}/%{name}/
