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
## VM Storage
### Manage Image Locations
Virtual images are stored in '/var/lib/libvirt/images' and can take up a lot of 
 space. To control where the images are stored, we can link a new path to the
 default location and retain the default SELinux settings.

```
# mkdir /path/to/dir/KVM
# semanage fcontext -a -t virt_image_t '/path/to/dir/KVM(/.*)?'
# restorecon /path/to/dir/KVM
# rmdir /var/lib/libvirt/images
# ln -s /path/to/dir/KVM /var/lib/libvirt/images
```
