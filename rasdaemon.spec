%define _hardened_build 1

Name:			rasdaemon
Version:		0.4.1
Release:		33.1%{?dist}
Summary:		Utility to receive RAS error tracings
Group:			Applications/System
License:		GPLv2
URL:			https://pagure.io/rasdaemon
Source0:		http://mchehab.fedorapeople.org/%{name}-%{version}.tar.bz2

ExclusiveArch:		%{ix86} x86_64 aarch64 %{power64}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 
BuildRequires:		autoconf, automake, gettext-devel, libtool, sqlite-devel
Requires:		hwdata, perl-DBD-SQLite
%ifnarch %{arm}
%ifnarch %{power64}
Requires:		dmidecode
%endif
%endif

Requires(post):		systemd-units
Requires(preun):	systemd-units
Requires(postun):	systemd-units

Patch1: 0001-ras-mc-ctl-Improve-error-summary-to-show-label-and-m.patch
Patch2: 0002-ras-record-make-the-code-more-generic.patch
Patch3: 0003-ras-record-rename-stmt-to-stmt_mc_event.patch
Patch4: 0004-ras-record-reorder-functions.patch
Patch5: 0005-ras-record-Make-the-code-easier-to-add-support-for-o.patch
Patch6: 0006-Add-support-to-record-AER-events.patch
Patch7: 0007-Add-support-to-store-MCE-events-at-the-database.patch
Patch8: 0008-ras-mc-ctl-add-summary-for-MCE-and-PCIe-AER-errors.patch
Patch9: 0009-ras-mc-ctl-report-errors-also-for-PCIe-AER-and-MCE.patch
Patch10: 0010-ras-mc-ctl-Fix-the-name-of-the-error-table-data.patch
Patch11: 0013-ras-mc-ctl-Improve-parser.patch
Patch12: 0014-ras-mc-ctl-Fix-label-register-with-2-layers.patch
Patch13: 0015-Add-an-example-of-labels-file.patch
Patch14: 0017-ras-mc-ctl-Fix-the-DIMM-layout-display.patch
Patch15: 0019-ras-mc-ctl-remove-completely-use-of-modprobe.patch
Patch16: 0022-mce-amd-k8.c-fix-a-warning.patch
Patch17: 0023-add-abrt-suppport-for-rasdaemon.patch
Patch18: 0026-rasdaemon-Add-record-option-to-rasdaemon-man-page.patch
Patch19: 0027-ras-mc-ctl-Print-useful-message-when-run-without-ras.patch
Patch20: 0028-Make-paths-in-the-systemd-services-configurable.patch
Patch21: 0031-Correct-ABRT-report-data.patch
Patch22: 0032-rasdaemon-handle-failures-of-snprintf.patch
Patch23: 0033-rasdaemon-correct-range-while-parsing-top-middle-and.patch
Patch24: 0034-rasdaemon-enable-recording-by-default.patch
Patch25: 0035-eMCA-support.patch
Patch26: 0036-rasdaemon-fix-some-errors-in-sqlite.patch
Patch27: 0037-rasdaemon-sqlite-truncates-some-MCE-fields-to-32-bit.patch
Patch28: 0038-rasdaemon-fix-mce-numfield-decoded-error.patch
Patch29: 0039-rasdaemon-do-not-assume-dimmX-directories-will-be-pr.patch
Patch30: 0040-rasdaemon-add-more-dell-labels.patch
Patch31: 0041-rasdaemon-add-support-for-Haswell.patch
Patch32: 0042-rasdaemon-decode-new-simple-error-code-number-6.patch
Patch33: 0043-rasdaemon-Add-missing-entry-to-Ivy-Bridge-memory-con.patch
Patch34: 0044-rasdaemon-Identify-Ivy-Bridge-properly.patch
Patch35: 0045-rasdaemon-add-support-for-Broadwell.patch
Patch36: 0046-rasdaemon-add-support-for-Knights-Landing.patch
Patch37: 0047-rasdaemon-properly-pring-message-strings-in-decode_b.patch
Patch38: 0048-rasdaemon-add-missing-semicolon-in-hsw_decode_model.patch
Patch39: 0049-rasdaemon-enable-IMC-status-usage-for-Haswell-E.patch
Patch40: 0050-rasdaemon-make-sure-the-error-is-valid-before-handli.patch
Patch41: 0051-rasdaemon-add-support-to-match-the-machine-by-system.patch
Patch42: 0052-rasdaemon-add-internal-errors-of-IA32_MC4_STATUS-for.patch
Patch43: 0053-rasdaemon-remove-a-space-from-mcgstatus_msg.patch
Patch44: 0054-rasdaemon-unnecessary-comma-for-empty-mc_location-st.patch
Patch45: 0055-rasdaemon-use-MCA-error-msg-as-error_msg.patch
Patch46: 0056-x86-rasdaemon-Add-support-to-log-Local-Machine-Check.patch
Patch47: 0057-rasdaemon-add-support-for-haswell-ex.patch
Patch48: 0058-rasdaemon-fix-typos-on-ras-mc-ctl-man-page.patch
Patch49: 0059-rasdaemon-Add-support-for-Knights-Landing-processor.patch
Patch50: 0060-mce-intel-knl-Fix-CodingStyle.patch
Patch51: 0061-Add-Broadwell-DE-MSCOD-values.patch
Patch52: 0062-Add-Broadwell-EP-EX-MSCOD-values.patch
# Patch53 was submitted upstream but not merged yet
Patch53: rasdaemon-dont_use_memerror_log_enable_on_knl.patch
Patch54: 0063-add_support_for_knights_mill.patch
Patch55: 0064-add_support_for_skylake.patch
Patch56: 0065-rasdaemon-Update-DIMM-labels-for-Dell-Servers.patch
Patch57: 0066-rasdaemon-Update-DIMM-labels-for-Intel-Skylake-serve.patch
Patch58: 0067-rasdaemon-add-support-for-non-standard-CPER-section-.patch
Patch59: 0068-rasdaemon-add-support-for-non-standard-error-decoder.patch
Patch60: 0069-rasdaemon-add-support-for-ARM-events.patch
Patch61: 0070-rasdaemon-ARM-fully-initialize-ras_arm_event.patch

%description
%{name} is a RAS (Reliability, Availability and Serviceability) logging tool.
It currently records memory errors, using the EDAC tracing events.
EDAC is drivers in the Linux kernel that handle detection of ECC errors
from memory controllers for most chipsets on i386 and x86_64 architectures.
EDAC drivers for other architectures like arm also exists.
This userspace component consists of an init script which makes sure
EDAC drivers and DIMM labels are loaded at system startup, as well as
an utility for reporting current error counts from the EDAC sysfs files.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1

%build
autoreconf -vfi
%configure --enable-mce --enable-aer --enable-sqlite3 --enable-extlog \
	--enable-arm --enable-non-standard
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -D -p -m 0644 misc/rasdaemon.service %{buildroot}/%{_unitdir}/rasdaemon.service
install -D -p -m 0644 misc/ras-mc-ctl.service %{buildroot}%{_unitdir}/ras-mc-ctl.service
install -D -p -m 0655 labels/* %{buildroot}%{_sysconfdir}/ras/dimm_labels.d
rm INSTALL %{buildroot}/usr/include/*.h

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root) 
%doc AUTHORS ChangeLog COPYING README TODO
%{_sbindir}/rasdaemon
%{_sbindir}/ras-mc-ctl
%{_mandir}/*/*
%{_unitdir}/*.service
%{_sharedstatedir}/rasdaemon
%{_sysconfdir}/ras/dimm_labels.d

%changelog
* Thu Mar 29 2018 Aristeu Rozanski <aris@redhat.com> 0.4.1-33.1.el7
- Refreshed build for zstream [1562017]

* Mon Mar 19 2018 Aristeu Rozanski <aris@redhat.com> 0.4.1-33.el7
- Enabled not standard errors [1520602]

* Fri Feb 02 2018 Aristeu Rozanski <aris@redhat.com> 0.4.1-32.el7
- Fixed covscan error [1520602]

* Wed Jan 24 2018 Aristeu Rozanski <aris@redhat.com> 0.4.1-31.el7
- Added ARM support [1520602]

* Thu Oct 19 2017 Aristeu Rozanski <aris@redhat.com> 0.4.1-30.el7
- Updated project url [1502400]

* Wed Aug 23 2017 Aristeu Rozanski <aris@redhat.com> 0.4.1-29.el7
- Updating Dell labels [1458938]

* Tue May 30 2017 Aristeu Rozanski <aris@redhat.com> 0.4.1-28.el7
- Bump release [1448113]

* Tue May 30 2017 Aristeu Rozanski <aris@redhat.com> 0.4.1-28.el7
- Identify as Knights Mill systems as such [1448113]

* Mon May 8 2017 Aristeu Rozanski <aris@redhat.com> 0.4.1-27.el7
- Fixed error found by covscan in the last patch [1377467]

* Tue Apr 11 2017 Aristeu Rozanski <aris@redhat.com> 0.4.1-26.el7
- add support for Skylake client and server [1377467]

* Wed Mar 22 2017 Aristeu Rozanski <aris@redhat.com> 0.4.1-25.el7
- add support for Knights Mill [1433862]

* Wed Aug 24 2016 Aristeu Rozanski <aris@redaht.com> 0.4.1-24.el7
- don't use MemError Log Enable on Knights Landing [1273326]

* Fri Apr 15 2016 Aristeu Rozanski <aris@redhat.com> 0.4.1-23.el7
- add Broadwell DE/EP/EX MSCOD values [1299512]

* Mon Feb 08 2016 Aristeu Rozanski <aris@redhat.com> 0.4.1-22.el7
- add missing upstream patches for Knights Landing [1273326]
- fix documentation typos [1247562]

* Thu Dec 03 2015 Aristeu Rozanski <aris@redhat.com> 0.4.1-21.el7
- add support for Knights Landing [1273326]

* Wed Sep 30 2015 Aristeu Rozanski <aris@redhat.com> 0.4.1-20.el7
- add support for Haswell EP/EX [1267137]

* Mon Jul 27 2015 Aristeu Rozanski <aris@redhat.com> 0.4.1-19.el7
- pull latest fixes by Seiichi Ikarashi from upstream [1243941]

* Mon Jul 27 2015 Aristeu Rozanski <aris@redhat.com> 0.4.1-18.el7
- don't depend on dmidecode on ppc64, fix typo [1244593]

* Wed Jul 22 2015 Aristeu Rozanski <aris@redhat.com> 0.4.1-17.el7
- don't depend on dmidecode on ppc64 [1244593]

* Wed Jul 08 2015 Aristeu Rozanski <aris@redhat.com> 0.4.1-16.el7
- allow label files to specify by system product name [1168340]

* Wed Jun 03 2015 Aristeu Rozanski <aris@redhat.com> 0.4.1-15.el7
- add support to Haswell and newer processors [1221912]

* Tue Dec 16 2014 Aristeu Rozanski <aris@redhat.com> 0.4.1-14.el7
- properly install the labels so it can be packaged [1073090]

* Tue Dec 02 2014 Aristeu Rozanski <aris@redhat.com> 0.4.1-13.el7
- updated labels patch to the new version submitted upstream [1073090]

* Tue Nov 25 2014 Aristeu Rozanski <aris@redhat.com> 0.4.1-12.el7
- fix on how sysfs tree is parsed for DIMMs [1073090]
- include new Dell labels [1073090]

* Fri Oct 10 2014 Aristeu Rozanski <aris@redhat.com> 0.4.1-11.el7
- don't require dmidecode for ppc64le [1151385]

* Fri Aug 22 2014 Aristeu Rozanski <aris@redhat.com> 0.4.1-10.el7
- use power64 macro instead, we have a driver enabled on ppc64 [1125663]

* Mon Aug 18 2014 Aristeu Rozanski <aris@redhat.com> 0.4.1-9.el7
- eMCA support [1085519]
- enable ppc64le [1125663]

* Mon Jun 09 2014 Aristeu Rozanski <aris@redhat.com> 0.4.1-8.el7
- Revert patch in 0.4.1-7.el7, replaced by a better patch
- Fix sizeof() usage on pointer [1035742]
- Added macro to build the package with stack protector [1092558]
- Handle failures of snprintf() [1035741]
- Fix range checking on signed char variables [1035746]
- Added aarch64 as architecture [1070973]
- Start recording by default [1117366] [1117367]

* Fri Jan 17 2014 Aristeu Rozanski <aris@redhat.com> 0.4.1-7.el7
- Fixed rasdaemon.service executable path [1043478]
 
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.4.1-6
- Mass rebuild 2013-12-27

* Tue Aug 20 2013 Aristeu Rozanski <aris@redhat.com> 0.4.1-5.el7
- Applied Jarod Wilson fixes required to pass rpmlint tests

* Thu Aug 15 2013 Aristeu Rozanski <aris@redhat.com> 0.4.1-4.el7
- Rebuild

* Sun Jun  2 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.4.1-3
- ARM has EDMA drivers (currently supported in Calxeda highbank)

* Tue May 28 2013 Mauro Carvalho Chehab <mchehab@redhat.com> 0.4.1-2
- Fix the name of perl-DBD-SQLite package

* Tue May 28 2013 Mauro Carvalho Chehab <mchehab@redhat.com> 0.4.1-1
- Updated to version 0.4.1 with contains some bug fixes

* Mon May 27 2013 Mauro Carvalho Chehab <mchehab@redhat.com> 0.4.0-1
- Updated to version 0.4.0 and added support for mce, aer and sqlite3 storage

* Mon May 20 2013 Mauro Carvalho Chehab <mchehab@redhat.com> 0.3.0-1
- Package created

