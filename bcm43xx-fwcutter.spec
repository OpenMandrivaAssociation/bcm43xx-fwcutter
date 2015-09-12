Name:		bcm43xx-fwcutter
Summary:	Tool to extract firmware for Broadcom 43xx network chip
Version:	006
Release:	20
URL:		http://bcm43xx.berlios.de/
Source:		%{name}-%{version}.tar.bz2
License:	GPLv2+
Group:		System/Configuration/Networking
Patch1:		bcm43xx-fwcutter-006-install_perms.patch

%description
Fwcutter allows you to extract the firmware required for Broadcom 43xx chips
out of the .sys files commonly available with the card or on the internet.

Once extracted, place all .fw files into /lib/firmware.

This variant of the tool is for the bcm43xx variant of the driver. For the
b43 variant of the driver, use the package b43-fwcutter.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p0
perl -pi -e 's|man/man1|share/man/man1|g' Makefile

%build
%setup_compile_flags
%make

%install
make install PREFIX=%{buildroot}%{_prefix}

cat > README.urpmi <<EOF
You need to extract the firmware from the .sys file provided by your vendor.
i.e bcm43xx-fwcutter -w /lib/firmware/ bcmwl5.sys
EOF

%files
%doc README README.urpmi
%{_bindir}/*
%{_mandir}/man1/*


