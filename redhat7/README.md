# Virtualization
## Packages
### Install Group Packages
```
# yum group install "Virtualization Tools" \
                    "Virtualization Hypervisor" \
                    "Virtualization Client"
```
## Kernel Modules
### Determine Kernel Modules Are Loaded
Associated kernel modules must be loaded before KVM can work.  If the KVM modules 
 are properly loaded, you'll see one of the following outputs based on your 
 hardware configuration.
#### Intel Hardware
```
# lsmod | grep kvm

Module    Size    Used by
kvm_intel 12345   0
kvm       12345   1 kvm_intel
```
#### AMD Hardware
```
# lsmod | grep kvm

Module    Size    Used by
kvm_amd   12345   0
kvm       12345   1 kvm_amd  
```
### Load Modules
To make sure the hardware is suitable, make sure the **vmx** (Intel) or **svm**
 (AMD) flags are loaded.
```
# cat /proc/cpuinfo | grep 'vmx\|svm'
```
If neither flag is found, you may need some additional configuration in the
 system BIOS or UEFI menu.
If one of the flags exists, load the module based on the hardware.
#### Intel Hardware
```
# modprobe kvm_intel
```
#### AMD Hardware
```
# modprobe kvm_amd
```
## Manage Image Locations
Virtual images are stored in **/var/lib/libvirt/images** and can take up a lot of 
 space. To control where the images are stored, we can link a new path to the
 default location and retain the default SELinux settings.
```
# mkdir /path/to/dir/KVM
# semanage fcontext -a -t virt_image_t '/path/to/dir/KVM(/.*)?'
# restorecon /path/to/dir/KVM
# rmdir /var/lib/libvirt/images
# ln -s /path/to/dir/KVM /var/lib/libvirt/images
```
## Virtual Shell
### Virtual Storage
### Virtual Networking
Virtual networking in KVM uses **libvirt**. Libvirt uses the concept of a 
 virtual network switch and shows up as a network interface. A default switch
 named **virbr0** is created when the libvirt daemon is first installed and 
 started.
You can use **ifconfig** or **ip** commands to view the virbr0 device. 
#### ifconfig
```
# ifconfig virbr0
 virbr0    Link encap:Ethernet  HWaddr 1A:D4:92:CF:FD:17  
           inet addr:192.168.122.1  Bcast:192.168.122.255  Mask:255.255.255.0
           UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
           RX packets:0 errors:0 dropped:0 overruns:0 frame:0
           TX packets:11 errors:0 dropped:0 overruns:0 carrier:0
           collisions:0 txqueuelen:0 
           RX bytes:0 (0.0 b)  TX bytes:3097 (3.0 KiB)
```
#### ip
```
# ip addr show virbr0
3: virbr0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN 
    link/ether 1a:d4:92:cf:fd:17 brd ff:ff:ff:ff:ff:ff
    inet 192.168.122.1/24 brd 192.168.122.255 scope global virbr0
```
