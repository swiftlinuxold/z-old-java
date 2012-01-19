#! /usr/bin/env python

# Check for root user login
import os, sys
if not os.geteuid()==0:
    sys.exit("\nOnly root can run this script\n")

# Get your username (not root)
import pwd
uname=pwd.getpwuid(1000)[0]

# The remastering process uses chroot mode.
# Check to see if this script is operating in chroot mode.
# /home/mint directory only exists in chroot mode
is_chroot = os.path.exists('/usr/lib/live-installer')
dir_develop=''
if (is_chroot):
	dir_develop='/usr/local/bin/develop'	
else:
	dir_develop='/home/'+uname+'/develop'

# Everything up to this point is common to all Python scripts called by shared-*.sh
# =================================================================================

print ("============================")
print ("BEGIN REMOVING JAVA PACKAGES")

# Add gcj-jre as a lighter replacement for sun-java6-jre and sun-java6-bin (41.4MB).
# LibreOffice requires one of the following packages:
# default-jre, gcj-jre, java-gcj-compat, openjdk-6-jre, sun-java6-jre, java5-runtime, jre
# LMDE only comes with sun-java6-jre.  gcj-jre is the most suitable replacement.
# Adding default-jre adds 92.4 MB.  Adding openjdk-6-jre requires 92.3 MB.
# java-gcj-compat, java5-runtime, and jre are not available in the normal repositories.
os.system('apt-get install -y gcj-jre')

# Now that gcj-jre is installed, sun-java6-jre and sun-java6-jre are no longer needed.
# Remove sun-java6-jre (14.7 MB) and sun-java6-bin (89.5 MB)
os.system('apt-get purge -y sun-java6-jre sun-java6-bin')

print ("FINISHED REMOVING JAVA PACKAGES")
print ("===============================")
