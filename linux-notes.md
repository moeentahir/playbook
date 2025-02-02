# Notes on Linux
## General points
- Centos is a fork of redhat
- Ubuntu is fork of debian

## Commands:
### Basic
man hier  > help about file system hierarchy  
<img src='./images/hierarchy.png' width='500'/>  
```
yum > Yellowdog update manager  
apt > Advance packaging tool  
dnf > A rewrite of yum and default package manager for fedora  
last > See loging and logout information  
uptime > information about how long the machine is up for  
```
### Archive
```
for i in {1..100}; do touch test_file_$i; done > loop with a range  
tar cf archive.tar test_file_* > create tar
tar tf archive.tar > view(tail) the contents for tar
tar xf archive.tar > extract all files
tar xf archive.tar file3 > extract only one file
tar rf archive.tar file3 > add file3 to tar
tar xf archive.tar --wildcards 'test_file_?' > only extract files that start with test_file_ and git only one digit after that
tar --delete --file=archive.tar file2 > delete file2 from tar
```
### Compression
```
tar czf archive.tar.gz file* > 'create gzip file' > compress in gzip format
tar cjf archive.tar.gz file* > 'create bzip2 file' > compress in bzip2  format
zip -r archive.zip file* > create zip file
```

### Disk management
Amazon EBS volumes are exposed as NVMe block devices on Amazon EC2 instances. The device names are /dev/nvme0n1, /dev/nvme1n1, and so on. The device names that you specify in a block device mapping are renamed using NVMe device names (/dev/nvme[0-26]n1). The block device driver can assign NVMe device names in a different order than you specified for the volumes in the block device mapping.
![image](https://github.com/user-attachments/assets/eb0c4504-65e4-46d8-9189-abbbc0ecf796)

```
nvme id-ctrl -v /head/nvme2n1 | head > check what device is mapped to what volume in EC2
for device in /dev/nvme*n1; do
    echo "$device: $(nvme id-ctrl $device | grep 'sn')" 
done

```

## Install Package
### RPM
```
sudo rpm -i htop-2.2.0-3.el7.x86_64.rpm
sudo rpm -e htop
```
### DEB
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
## Hardware
```
cat /etc/issue > Display Ubuntu version
cat /proc/cpuinfo > display cpu information
cat /prov/version > Display version of os
free -m > See free memory
df -h > 
ifconfig > need to install setup-tools to see network interface
```
## Where data is stored?
### Configuration
```
/boot > Kernel related files - have a look at all the files to get familiar with
/boot/config-5.8.0-38-generic > get boot related configuration
/boot/grub/grub.cfg > 
/etc/fstab > config related to mounted devices
blkid > Get uuid against block devices
/etc/passwd > get list of all the users
/etc/group > get list of all the groups
/etc/hosts > list of all the hosts
/etc/resolv.conf > this is where we specify name server
/etc/vim/vimrc > common vim settings
/sys > datastructure for Kernel
mount | grep sysfs > see where this is mounted
```
### Processes
```
/proc > 1 directory for each process running on the machine
/proc/2872/status > 
/proc/self/status 
/proc/self/status
```
### Messages and logging
```
dmesg | grep -i bluetooth .> Show kernal message. This is a ring buffer, which means new messages get added and old get deleted. This is normally used to troubleshoot hardware.
/var/log/syslog > general system logs
/var/log/auth.log
/var/log/boot.log
/var/log/faillog
```
## The network
Switches - route traffic within the network, switch is then connected to router if traffic needs to be sent to internet.
Router - route traffic outside network
### Querying the network
```
ip addr show
ping example.com
host www.example.com > to translate domain to ip versio 4 or 6
dig example.com > Also used to translate domain to ip but it gives more information
dig @1.1.1.1 example.com > Ask a different server to resolve dns
/etc/resolv.conf > Cofig file to determine which hosts to use for DNS queries.
/etc/hosts > Use for static mapping for IP addresses to host names
```
### Network configuration
```
ip route show > show the current route table
```
Result of above command on my ubuntu machine is:
```
default via 192.168.0.1 dev wlp2s0 proto dhcp metric 600 
169.254.0.0/16 dev wlp2s0 scope link metric 1000 
172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1 linkdown 
192.168.0.0/24 dev wlp2s0 proto kernel scope link src 192.168.0.45 metric 600 
```
The first line of the results say that the default route be via 192.168.0.1 using device wlp2s0
Second line says if I want to talk to address in the range 169.254.0.0/16, I do not go via router, instead I go directly to the device wlp2s0
Third and fourth lines are similar to second line
#### Other Commands
```
ifconfig > View and change network interface Configuration
netstat > View listing services and active connections
netstat -tlnp > to for tcp, l for listening, n for numeric or in other words give me ip names and not the hosnames, p is for PID
ss > Same as netstat
ss -tlnp > show tcp traffic
ss -ulnp > Show udp traffic
nmcli > Command line tool to control network manager
nmcli device show > Show information about known devices
nmcli connection show > Show list of active conneciton profile
```
If you want to see what port is for what
```
cat /etc/services | grep 22
```

