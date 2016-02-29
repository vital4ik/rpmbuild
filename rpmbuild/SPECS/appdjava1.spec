#
# JAVA 1.8 install required to run the appdynamics machine agent
#
Summary: Java 1.8 for machineagent appd
Name:  appdjava18
Version: 1.0
Release: 1
#Copyright: GPL
License: GPL+
Group: Applications/java
#BuildRoot: /opt/rpmbuild/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
#%_topdir /opt/rpmbuild/
#Sourcedir:  /opt/rpmbuild/SOURCES/
Source0: jre1.8.0_40.tar.gz
#URL: http://www.gnomovision.com/cdplayer/cdplayer.html
Distribution: CentOs Linux
Vendor: Oracle
Packager: Vital4ik <vmf11@hotmail.com>

%description
Needs to be installed into /opt/Appdynamics folder and symlink java
created to point to the installed folde

%prep
#%autosetup -q
#cd /home/rpmbuild/rpmbuild/SOURCES/
#cp ../SOURCES/jre1.8.0_40.tar.gz //home/rpmbuild/rpmbuild/BUILD/
#tar -xvzf jre1.8.0_40.tar.gz
#rm -f jre1.8.0_40.tar.gz
#%setup 


%build 

mkdir /opt/Appdynamics
cp ../SOURCES/jre1.8.0_40.tar.gz /opt/Appdynamics
cd /opt/Appdynamics
tar -xvzf jre1.8.0_40.tar.gz
rm -f /opt/Appdynamics/jre1.8.0_40.tar.gz
ln -s  /opt/Appdynamics/jre1.8.0_40 java

#rm -rf %{buildroot}

%changelog
* Sun Feb 28 2016  Vital4ik <vmf11@hotmail.com> 1.0-1
- First Build
