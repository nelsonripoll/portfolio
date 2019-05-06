# Virtualization
[Red Hat - Virtualization Getting Started Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/virtualization_getting_started_guide/index)
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
## Virtual Shell
To connect locally as the root user to the daemon supervising guest virtual
 machines on the KVM hypervisor.
```
# virsh -c qemu:///system
```
To connect locally as a user to the user's set of guest local machines using the
 KVM hypervisor.
```
# virsh -c qemu:///session
```
## virt-install
| Switch            | Description                                                 |
| ----------------- | ----------------------------------------------------------- |
| -n, --name        | Sets the name for the VM.                                   |
| --vcpus           | Configures the number of virtual CPUs.                      |
| -r, --ram         | Configures the amount of RAM in MB.                         |
| --disk            | Defines the virtual disk.                                   |
| -l, --location    | Specifies the directory or URL with the installation files. |
| --graphics        | Specifies the graphical display settings of the guest.      |
| -x, --extra-args= | Includes extra data, such as the URL of a Kickstart file.   |
