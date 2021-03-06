# Configure an iSCSI Target and Initiator

## Server Configuration - iSCSI Target

### Definitions
* SCSI (small computer system interface) - A set of standards for physically
 connecting and transferring data between computers and peripheral devices.
* iSCSI (internet SCSI) - A set of SCSI standards but uses ethernet connectors
 and cables as its physical transport, but can run over any physical transport
 capable of tranporting IP.
* TPG (target portal group) - A set of network portals within an iSCSI node over
 which an iSCSI session is conducted.
* LUN (logical unit number) - A number used to identify a logincal unit, which
 is a device addressed by the SCSI protocol or Storage Area Network (SAN) 
 protocols which encapsulate SCSI, such as Fibre Channel or iSCSI.
* ACL (access control lists) - Permissions attached to an object that specify
 which users are granted access and which operations are allowed to be performed
 by said users to that object.
* CHAP (challenge-handshake authentication protocol) - CHAP provides protection
 against replay attacks by the peer through the use of an incrementally changing
 identifier and of a variable challenge-value.

### Required Packages

#### targetcli

```
# dnf info targetcli

Name         : targetcli
Version      : 2.1.fb49
Release      : 1.el8
Arch         : noarch
Size         : 217 k
Source       : targetcli-2.1.fb49-1.el8.src.rpm
Repo         : @System
From repo    : AppStream
Summary      : An administration shell for storage targets
URL          : https://fedorahosted.org/targetcli-fb/
License      : ASL 2.0
Description  : An administration shell for configuring iSCSI, FCoE, and other
             : SCSI targets, using the TCM/LIO kernel target subsystem. FCoE
             : users will also need to install and use fcoe-utils.

# dnf repoquery -l targetcli | grep "^/etc\|^/usr/bin"
/etc/target
/etc/target/backup
/usr/bin/targetcli
```

#### firewalld

```
# dnf info firewalld

Name         : firewalld
Version      : 0.6.3
Release      : 7.el8
Arch         : noarch
Size         : 1.9 M
Source       : firewalld-0.6.3-7.el8.src.rpm
Repo         : @System
From repo    : anaconda
Summary      : A firewall daemon with D-Bus interface providing a dynamic firewall
URL          : http://www.firewalld.org
License      : GPLv2+
Description  : firewalld is a firewall service daemon that provides a dynamic customizable
             : firewall with a D-Bus interface.

# dnf repoquery -l firewalld | grep "^/etc\|^/usr/bin"
/etc/firewalld
/etc/firewalld/firewalld.conf
/etc/firewalld/helpers
/etc/firewalld/icmptypes
/etc/firewalld/ipsets
/etc/firewalld/lockdown-whitelist.xml
/etc/firewalld/services
/etc/firewalld/zones
/etc/modprobe.d/firewalld-sysctls.conf
/etc/sysconfig/firewalld
/usr/bin/firewall-cmd
/usr/bin/firewall-offline-cmd
```

### Configure Server

Download the **targetcli** and **firewalld** packages. Afterwards go ahead and
 enable the services.

```
# dnf install targetcli firewalld
# systemctl enable target
# systemctl enable firewalld
```

We need to configure either a storage mount which can be either a 
 _FILEIO backstore_ or a _block-level storage_. In this example, we will use the
 BLOCKIO storage type. First, we need to determine what device we will use. In 
 this example, I have a second drive located at _/dev/xvdg_ that is about 1 GB in size.

```
# fdisk -l
Disk /dev/xvda: 10.7 GB, 10737418240 bytes, 20971520 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: gpt
# Start End Size Type Name
 1 2048 4095 1M BIOS boot parti
 2 4096 20971486 10G Microsoft basic
Disk /dev/xvdg: 1073 MB, 1073741824 bytes, 2097152 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```

Now we will work through the target command line interface to prepare our device.

```
# targetcli
/> help
...
COMMAND SYNTAX
==============
Commands are built using the following syntax:

[TARGET_PATH] COMMAND_NAME [OPTIONS]

The TARGET_PATH indicates the path to run the command from.
If ommited, the command will be run from your current path.

The OPTIONS depend on the command. Please use help
COMMAND to get more information.


AVAILABLE COMMANDS
==================
The following commands are available in the
current path:

  - bookmarks action [bookmark] 
  - cd [path] 
  - clearconfig [confirm] 
  - exit 
  - get [group] [parameter...] 
  - help [topic] 
  - ls [path] [depth] 
  - pwd 
  - refresh 
  - restoreconfig [savefile] [clear_existing] 
  - saveconfig [savefile] 
  - sessions [action] [sid] 
  - set [group] [parameter=value...] 
  - status 
  - version 
/>
```

As you can see, the command syntax always starts with our path followed by the
 command we want to run. You can use `ls` and `cd` in the target command line 
 interface prompt.

```
/> ls
o- / ......................................................................................................................... [...]
  o- backstores .............................................................................................................. [...]
  | o- block .................................................................................................. [Storage Objects: 0]
  | o- fileio ................................................................................................. [Storage Objects: 0]
  | o- pscsi .................................................................................................. [Storage Objects: 0]
  | o- ramdisk ................................................................................................ [Storage Objects: 0]
  o- iscsi ............................................................................................................ [Targets: 0]
  o- loopback ......................................................................................................... [Targets: 0]
```

Now we are going to create the first block in the storage device. 

```
/> backstores/block/ create testblock1 /dev/xvdg
Created block storage object testblock1 using /deg/xvdg
```

This creates a new storage object at `/dev/xvdg` by the name of _testblock1_.

Now we use the iSCSI command to create a qualified name. iSCSI qualified names
 are how target disks are referred to when using iSCSI.

According to RTC 3270, section 3.2.6.3.1, the name should start with "iqn."
 followed by a date code, in yyyy-mm format. After the date, there should be a
 "." and then the reversed domain name of the name authority creating this
 iSCSI name. Afterwards, an optional ":" prefix followed by any string within
 the character set and length boundaries that the owner of the domain name deems
 appropriate. This may contain product types, serial numbers, host identifiers, 
 or software keys. With the exception of the colon prefix, the owner can assign
 everything after the reversed domain name as desired.

In this example, our qualified name will be "iqn." followed by the month we
 created the device, "2020-01" followed by a "." and our reversed domain
 "com.mylabserver". The last bit will be just the name of the device we created.

```
/> iscsi/ create iqn.2020-01.com.mylabserver:t1
Created target iqn.2020-01.com.mylabserver:t1.
Created TPG 1.
Global pref auto_add_default_portal=true
Created default portal listening on all IPs (0.0.0.0), port 3260.
```

To review the created target group, change directory into the new target disk.
 I believe TPG stands for "target portal group". As you can see, this target
 group is listening on port 3260. After we're done, we need to configure the
 firewall to open port 3260.

```
/> cd iscsi/iqn.2020-01.com.mylabserver:t1/tpg1
/iscsi/iqn.2020-01.com.mylabserver:t1/tpg1> ls
o- tpg1 ......................................... [no-gen-acls, no-auth]
 o- acls .................................................... [ACLs: 0]
 o- luns .................................................... [LUNs: 0]
 o- portals .............................................. [Portals: 1]
 o- 0.0.0.0:3260 ./............................................. [OK]
```

Now we create a LUN, or device associated with the mountable disk. Ensure that
 you are referring to the block using the name we originally gave it.

```
/iscsi/iqn.2020-01.com.mylabserver:t1/tpg1> luns/ create /backstores/block/testblock1
Created LUN 0
```

The server needs to know how to refer to this via the clients. This can be done
 by referring to the IQN, and is called the _initiator name_. We can also move to
 the ACL's IQN directory and provide a username and password for the client to 
 authenticate itself. The password is stored in plaintext in the **/etc/**
 directory so ensure it is not used for any other service. Once we have set the
 authenticate we can exit the `targetcli` program. This process will generate a
 JSON file in the **/etc/target** directory.

```
/iscsi/iqn.2020-01.com.mylabserver:t1/tpg1> acls/ create iqn.2020-01.com.mylabserver:client
Created Node ACL for iqn.2020-01.com.mylabserver:client
Created mapped LUN 0.
/iscsi/iqn.2020-01.com.mylabserver:t1/tpg1> cd acls/iqn.2020-01.com.mylabserver:client/
/iscsi/iqn.2020-01.com.mylabserver:client> set auth userid=lunuser
Parameter userid is now 'lunuser'.
/iscsi/iqn.2020-01.com.mylabserver:client> set auth password=password
Parameter password is now 'password'.
/iscsi/iqn.2020-01.com.mylabserver:client> exit
Global pref auto_save_on_exit=true
Last 10 configs saved in /etc/target/backup.
Configuration saved to /etc/target/saveconfig.json
```

The last thing we should do is open up port 3260 on the firewall and start the 
 target and firewall services.

```
# systemctl start target
# systemctl start firewalld
# firewall-cmd --permanent --add-port=3260/tcp
# firewall-cmd --reload
```


## Client Configuration - iSCSI Initiator

### Required Packages

#### iscsi-initiator-utils

```
# dnf info iscsi-initiator-utils

Installed Packages
Name         : iscsi-initiator-utils
Version      : 6.2.0.876
Release      : 7.gitf3c8e90.el8
Arch         : x86_64
Size         : 1.8 M
Source       : iscsi-initiator-utils-6.2.0.876-7.gitf3c8e90.el8.src.rpm
Repo         : @System
From repo    : anaconda
Summary      : iSCSI daemon and utility programs
URL          : http://www.open-iscsi.org
License      : GPLv2+
Description  : The iscsi package provides the server daemon for the iSCSI protocol,
             : as well as the utility programs used to manage it. iSCSI is a protocol
             : for distributed disk access using SCSI commands sent over Internet
             : Protocol networks.
```

### Configure Client

```
# yum install -y iscsi-initiator-utils
# cd /etc/iscsi
# echo "InitiatorName=iqn.2020-01.com.mylabserver:client" > initiatorname.iscsi
# sed -i 's/#node.session.auth.authmethod = CHAP/node.session.auth.authmethod = CHAP/' /etc/iscsi/iscsid.conf
# sed -i 's/#node.session.auth.username = username/node.session.auth.username = lunuser/' /etc/iscsi/iscsid.conf 
# sed -i 's/#node.session.auth.password = username/node.session.auth.password = password/' /etc/iscsi/iscsid.conf 
# iscsiadm --mode discovery --type sendtargets --portal 10.0.0.100
10.0.0.100:3260,1 iqn.2020-01.com.mylabserver:t1
# iscsiadm --mode node --target iqn.2020-01.com.mylabserver:t1 --portal 10.0.0.100 --login
Logging in to [iface: default, target: iqn.2020-01.com.mylabserver:t1, portal: 10.0.0.100,3260] (multiple)
Login to [iface: default, target: iqn.2020-01.com.mylabserver:t1, portal: 10.0.0.100,3260] successful.
# lsblk --scsi
NAME HCTL       TYPE VENDOR   MODEL             REV TRAN
sda  2:0:0:0    disk LIO-ORG  testblock1       4.0  iscsi
# lsblk | egrep "NAME|sda"
NAME    MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
sda       8:0    0   1G  0 disk
# mkfs.ext4 /dev/sda
mke2fs 1.42.9 (28-Dec-2013)
/dev/sda is entire device, not just one partition!
Proceed anyway? (y,n) y
Filesystem label=
OS type: Linux
Block size=4096 (log=2)
Fragment size=4096 (log=2)
Stride=0 blocks, Stripe width=32 blocks
65536 inodes, 262144 blocks
13107 blocks (5.00%) reserved for the super user
First data block=0
Maximum filesystem blocks=268435456
8 block groups
32768 blocks per group, 32768 fragments per group
8192 inodes per group
Superblock backups stored on blocks:
	32768, 98304, 163840, 229376

Allocating group tables: done
Writing inode tables: done
Creating journal (8192 blocks): done
Writing superblocks and filesystem accounting information: done

# blkid | grep "/dev/sda"
/dev/sda: UUID="41955f70-d2e2-43b0-9f79-61e9b963bcfa" TYPE="ext4" 
# echo "UUID=41955f70-d2e2-43b0-9f79-61e9b963bcfa /mnt/iscsi ext4 _netdev 0 0" >> /etc/fstab
# mkdir /mnt/iscsi
# mount -a
# cd /mnt/iscsi/
# echo "my first iscsi filesystem" > testfile.txt
# iscsiadm -m session -P 3
iSCSI Transport Class version 2.0-870
version 6.2.0.874-10
Target: iqn.2020-01.com.mylabserver:t1 (non-flash)
	Current Portal: 10.0.0.100:3260,1
	Persistent Portal: 10.0.0.100:3260,1
		**********
		Interface:
		**********
		Iface Name: default
		Iface Transport: tcp
		Iface Initiatorname: iqn.2020-01.com.mylabserver:client
		Iface IPaddress: 10.0.0.101
		Iface HWaddress: <empty>
		Iface Netdev: <empty>
		SID: 1
		iSCSI Connection State: LOGGED IN
		iSCSI Session State: LOGGED_IN
		Internal iscsid Session State: NO CHANGE
		*********
		Timeouts:
		*********
		Recovery Timeout: 120
		Target Reset Timeout: 30
		LUN Reset Timeout: 30
		Abort Timeout: 15
		*****
		CHAP:
		*****
		username: lunuser
		password: ********
		username_in: <empty>
		password_in: ********
		************************
		Negotiated iSCSI params:
		************************
		HeaderDigest: None
		DataDigest: None
		MaxRecvDataSegmentLength: 262144
		MaxXmitDataSegmentLength: 262144
		FirstBurstLength: 65536
		MaxBurstLength: 262144
		ImmediateData: Yes
		InitialR2T: Yes
		MaxOutstandingR2T: 1
		************************
		Attached SCSI devices:
		************************
		Host Number: 2	State: running
		scsi2 Channel 00 Id 0 Lun: 0
			Attached scsi disk sda		State: running
```
