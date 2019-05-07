# Kickstart
## Basic Configuration
```
# System language
lang en_US.UTF-8

# Keyboard layouts
keyboard --vckeymap=us --xlayouts='us'

# System timezone
timezone America/Chicago --nontp
```
## Installation Method
You must specify whether you are installing or upgrading the system.
### Install
You must specify the type of installation from cdrom, harddrive, nfs, liveimg,
 or url (for FTP, HTTP, or HTTPS installations). The **install** command and the 
 installation method command must be on seperate lines. For example:
```
install
liveimg --url=file:///images/install/squashfs.img --noverifyssl
```

Install from the first optical drive on the system.
```
install
cdrom
```

Install from an installation tree or full installation ISO image on a local
 drive. The drive must contain a file system the installation program can mount:
 ext2, ext3, ext4, vfat, or xfs.
*   --biospart= - BIOS partition to install from.
*   --partition= - Partition to install from.
*   --dir= - Directory containing the variant directory of the installation
 tree, or the ISO image of the full installation DVD.
```
install
harddrive --partition=hbd2 --dir=/tmp/install-tree
```

Install from a disk image instead of packages. The image can be the squashfs.img
 file from a live ISO image, a compressed tar file (.tar, .tbz, .tgz, .txz, 
 .tar.bz2, .tar.gz, or .tar.xz), or any file system that the installation media
 can mount. Supported file systems are ext2, ext3, ext4, vfat, and xfs.
*   --url= - The location to install from. Supported protocols are HTTP, HTTPS,
 FTP, and file.
*   --proxy= - Specify an HTTP, HTTPS, or FTP proxy to use while performing the
 installation.
*   --checksum= - An optional argument with the SHA256 checksum of the image
 file, used for verification.
*   --noverifyssl - Disable SSL verification when connecting to an HTTPS server.
```
install
liveimg --url=file:///images/install/squashfs.img --checksum=03825f567f17705100de3308a20354b4d81ac9d8bed4bb4692b2381045e56197 --noverifyssl
```

Install from the NFS server specified.
*   --server= - Server from which to install (host name or IP).
*   --dir= - Directory containing the variant directory of the installation tree.
*   --opts= - Mount options to use for mounting the NFS export. (optional)

Install from an installation tree on a remote server using FTP, HTTP, or HTTPS.
*   --url= - The location to install from. Supported protocols are HTTP, HTTPS,
 FTP, and file.
*   --mirrorlist= - The mirror URL to install from.
*   --proxy= - Specify an HTTP, HTTPS, or FTP proxy to use while performing
 the installation.
*   --noverifyssl - Disable SSL verification when connecting to an HTTPS server.
```
install
url --url http://server/path
```

### Upgrade
```
upgrade
```
## Boot Loader Options
## Partition Information
## Network Configuration
## Authentication
## Firewall Configuration
```
firewall --enabled --http --ftp --ssh
```
## Display Configuration
## Package Selection
## Pre-Installation Script
## Post-Installation Script










## Mount ISO
```
# mount -o loop CentOS7.iso /media
```
## HTTP
Run the following commands then use a browser to navigate to http://localhost/inst.
```
# yum install httpd
# mkdir /var/www/html/inst
# mkdir /var/www/html/ks
# cp -a /media/. /var/www/html/inst/
# cp /root/anaconda-ks.cfg /var/www/html/ks/ks1.cfg
# chcon -R --reference=/var/www/html /var/www/html/inst
# firewall-cmd --permanent --add-service=http
# firewall-cmd --reload
# systemctl restart httpd
```
## FTP
Run the following commands then use a browser to navigate to ftp://localhost/pub/inst.
```
# yum install vsftpd
# mkdir /var/ftp/pub/inst
# mkdir /var/ftp/pub/ks
# cp -a /media/. /var/ftp/pub/inst
# cp /root/anaconda-ks.cfg /var/ftp/pub/ks/ks1.cfg
# chcon -R -t public_content_t /var/ftp/
# firewall-cmd --permanent --add-service=ftp
# firewall-cmd --reload
# systemctl restart vsftpd
```
