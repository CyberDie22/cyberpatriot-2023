#!/usr/bin/env bash
###############################################################################
#
# Bash Remediation Script for Standard System Security Profile for SUSE Linux Enterprise 12
#
# Profile Description:
# This profile contains rules to ensure standard security baseline
# of a SUSE Linux Enterprise 12 system. Regardless of your system's workload
# all of these checks should pass.
#
# Profile ID:  xccdf_org.ssgproject.content_profile_standard
# Benchmark ID:  xccdf_org.ssgproject.content_benchmark_SLE-12
# Benchmark Version:  0.1.70
# XCCDF Version:  1.2
#
# This file can be generated by OpenSCAP using:
# $ oscap xccdf generate fix --profile xccdf_org.ssgproject.content_profile_standard --fix-type bash ssg-sle12-ds.xml
#
# This Bash Remediation Script is generated from an XCCDF profile without preliminary evaluation.
# It attempts to fix every selected rule, even if the system is already compliant.
#
# How to apply this Bash Remediation Script:
# $ sudo ./remediation-script.sh
#
###############################################################################

###############################################################################
# BEGIN fix (1 / 3) for 'xccdf_org.ssgproject.content_rule_file_groupowner_etc_passwd'
###############################################################################
(>&2 echo "Remediating rule 1/3: 'xccdf_org.ssgproject.content_rule_file_groupowner_etc_passwd'")
chgrp 0 /etc/passwd

# END fix for 'xccdf_org.ssgproject.content_rule_file_groupowner_etc_passwd'

###############################################################################
# BEGIN fix (2 / 3) for 'xccdf_org.ssgproject.content_rule_file_owner_etc_passwd'
###############################################################################
(>&2 echo "Remediating rule 2/3: 'xccdf_org.ssgproject.content_rule_file_owner_etc_passwd'")
chown 0 /etc/passwd

# END fix for 'xccdf_org.ssgproject.content_rule_file_owner_etc_passwd'

###############################################################################
# BEGIN fix (3 / 3) for 'xccdf_org.ssgproject.content_rule_file_permissions_etc_passwd'
###############################################################################
(>&2 echo "Remediating rule 3/3: 'xccdf_org.ssgproject.content_rule_file_permissions_etc_passwd'")





chmod u-xs,g-xws,o-xwt /etc/passwd

# END fix for 'xccdf_org.ssgproject.content_rule_file_permissions_etc_passwd'

