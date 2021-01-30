# Notes on Linux
## General points
- Centos is a fork of redhat
- Ubuntu is fork of debian

man hier  > help about file system hierarchy
yum > Yellowdog update manager
apt > Advance packaging tool
dnf > A rewrite of yum and default package manager for fedora


## Basic commands

last > See loging and logout information
uptime > information about how long the machine is up for

## Package management
### RPM
```
sudo rpm -i htop-2.2.0-3.el7.x86_64.rpm
sudo rpm -e htop

```
### Dbpkg
```
sudo dpkg -i htop_2.0.2-1_amd64.deb
sudo dpkg --remove htop
```
### From Source
```
 tar xzf htop-2.2.0.tar.gz
cd htop-2.2.0
./configure
make
sudo make install
sudo make uninstall
```
