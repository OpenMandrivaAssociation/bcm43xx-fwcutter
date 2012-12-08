%define name	bcm43xx-fwcutter
%define version	006
%define release %mkrel 10

Name: 	 	%{name}
Summary: 	Tool to extract firmware for Broadcom 43xx network chip
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://bcm43xx.berlios.de/
License:	GPLv2+
Group:		System/Configuration/Networking
Patch1:		bcm43xx-fwcutter-006-install_perms.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot

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
%make
										
%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=%buildroot/%_prefix
cat > README.urpmi <<EOF
You need to extract the firmware from the .sys file provided by your vendor.
i.e bcm43xx-fwcutter -w /lib/firmware/ bcmwl5.sys
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README README.urpmi
%{_bindir}/*
%{_mandir}/man1/*



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 006-9mdv2011.0
+ Revision: 663316
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 006-8mdv2011.0
+ Revision: 603758
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 006-7mdv2010.1
+ Revision: 522190
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 006-6mdv2010.0
+ Revision: 413163
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 006-5mdv2009.1
+ Revision: 350206
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 006-4mdv2009.0
+ Revision: 220478
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 006-3mdv2008.1
+ Revision: 148916
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 08 2007 Adam Williamson <awilliamson@mandriva.org> 006-2mdv2008.0
+ Revision: 82320
- rebuild for 2008
- correct text of README.urpmi
- add clarification of bcm43xx / b43 to description
- Fedora license policy


* Tue Feb 27 2007 Thierry Vignaud <tvignaud@mandriva.com> 006-1mdv2007.0
+ Revision: 126469
- Import bcm43xx-fwcutter

* Mon Feb 19 2007 Adam Williamson <awilliamson@mandriva.com> 006-1mdv2007.0
- Update to stable release 006

* Thu Aug 24 2006 Erwan Velu <erwan@mandriva.org> 005-0.1172.2mdv2007.0
- Adding a README.urpmi

* Sat Jun 17 2006 Austin Acton <austin@mandriva.org> 005-0.1172.1mdv2007.0
- initial package

