%bcond_without check
%global debug_package %{nil}

%global crate parking_lot_core

Name:           rust-%{crate}
Version:        0.8.5
Release:        1
Summary:        Advanced API for creating custom synchronization primitives

# Upstream license specification: Apache-2.0/MIT
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/parking_lot_core
Source:         %{crates_source}
Patch0:		parking_lot_core-windoze-go-to-hell.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(cfg-if/default) >= 1.0.0 with crate(cfg-if/default) < 2.0.0)
BuildRequires:  (crate(instant/default) >= 0.1.9 with crate(instant/default) < 0.2.0)
BuildRequires:  (crate(libc/default) >= 0.2.95 with crate(libc/default) < 0.3.0)
BuildRequires:  (crate(redox_syscall/default) >= 0.2.8 with crate(redox_syscall/default) < 0.3.0)
BuildRequires:  (crate(smallvec/default) >= 1.6.1 with crate(smallvec/default) < 2.0.0)
%endif

%global _description %{expand:
Advanced API for creating custom synchronization primitives.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(parking_lot_core) = 0.8.5
Requires:       cargo
Requires:       (crate(cfg-if/default) >= 1.0.0 with crate(cfg-if/default) < 2.0.0)
Requires:       (crate(instant/default) >= 0.1.9 with crate(instant/default) < 0.2.0)
Requires:       (crate(libc/default) >= 0.2.95 with crate(libc/default) < 0.3.0)
Requires:       (crate(redox_syscall/default) >= 0.2.8 with crate(redox_syscall/default) < 0.3.0)
Requires:       (crate(smallvec/default) >= 1.6.1 with crate(smallvec/default) < 2.0.0)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(parking_lot_core/default) = 0.8.5
Requires:       cargo
Requires:       crate(parking_lot_core) = 0.8.5

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+backtrace-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(parking_lot_core/backtrace) = 0.8.5
Requires:       cargo
Requires:       (crate(backtrace/default) >= 0.3.60 with crate(backtrace/default) < 0.4.0)
Requires:       crate(parking_lot_core) = 0.8.5

%description -n %{name}+backtrace-devel %{_description}

This package contains library source intended for building other packages
which use "backtrace" feature of "%{crate}" crate.

%files       -n %{name}+backtrace-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+deadlock_detection-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(parking_lot_core/deadlock_detection) = 0.8.5
Requires:       cargo
Requires:       (crate(backtrace/default) >= 0.3.60 with crate(backtrace/default) < 0.4.0)
Requires:       (crate(petgraph/default) >= 0.5.1 with crate(petgraph/default) < 0.6.0)
Requires:       (crate(thread-id/default) >= 4.0.0 with crate(thread-id/default) < 5.0.0)
Requires:       crate(parking_lot_core) = 0.8.5

%description -n %{name}+deadlock_detection-devel %{_description}

This package contains library source intended for building other packages
which use "deadlock_detection" feature of "%{crate}" crate.

%files       -n %{name}+deadlock_detection-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(parking_lot_core/nightly) = 0.8.5
Requires:       cargo
Requires:       crate(parking_lot_core) = 0.8.5

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages
which use "nightly" feature of "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+petgraph-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(parking_lot_core/petgraph) = 0.8.5
Requires:       cargo
Requires:       (crate(petgraph/default) >= 0.5.1 with crate(petgraph/default) < 0.6.0)
Requires:       crate(parking_lot_core) = 0.8.5

%description -n %{name}+petgraph-devel %{_description}

This package contains library source intended for building other packages
which use "petgraph" feature of "%{crate}" crate.

%files       -n %{name}+petgraph-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+thread-id-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(parking_lot_core/thread-id) = 0.8.5
Requires:       cargo
Requires:       (crate(thread-id/default) >= 4.0.0 with crate(thread-id/default) < 5.0.0)
Requires:       crate(parking_lot_core) = 0.8.5

%description -n %{name}+thread-id-devel %{_description}

This package contains library source intended for building other packages
which use "thread-id" feature of "%{crate}" crate.

%files       -n %{name}+thread-id-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
