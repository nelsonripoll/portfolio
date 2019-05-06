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
The **virt-install** is a command line tool used for creating KVM, Xen, or Linux
 container guests using the **libvirt** hypervisor management library. Most
 options are not required. Minimum requirements are **--name**, **--memory**,
 guest storage (**--disk** or **--filesystem**), and an install option.

### Common Options 
| Switch            | Description                                                 |
| ----------------- | ----------------------------------------------------------- |
| --connect         | Connect to a non-default hypervisor.                        |
| --name            | Sets the name for the VM.                                   |
| --vcpus           | Configures the number of virtual CPUs.                      |
| --memory          | Memory to allocate for the guest, in MiB.                   |
| --disk            | Defines the virtual disk.                                   |
| --location        | Specifies the directory or URL with the installation files. |
| --graphics        | Specifies the graphical display settings of the guest.      |
| --extra-args      | Includes extra data, such as the URL of a Kickstart file.   |
#### --connect
Connect to a non-default hypervisor. If this isn't specified, libvirt will try 
 and choose the most suitable default.

Some valid options here are:
##### qemu:///system
For creating KVM and QEMU guests to be run by the system libvirtd instance.
 This is the default mode that virt-manager uses, and what most KVM users want.
```
virt-install --connect qemu:///system [OPTIONS]...
```
##### qemu:///session
For creating KVM and QEMU guests for libvirtd running as the regular user.
```
virt-install --connect qemu:///session [OPTIONS]...
```
##### xen:///
For connecting to Xen.
```
virt-install --connect xen:/// [OPTIONS]...
```
##### lxc:///
For creating linux containers.
```
virt-install --connect lxc:/// [OPTIONS]...
```
#### --name
Name of the new guest virtual machine instance. This must be unique amongst all 
 guests known to the hypervisor on the connection, including those not currently 
 active. To re- define an existing guest, use the virsh(1) tool to shut it down 
 ('virsh shutdown') & delete ('virsh undefine') it prior to running "virt-install".
#### --vcpus
Number of virtual cpus to configure for the guest. If 'maxvcpus' is specified, 
 the guest will be able to hotplug up to MAX vcpus while the guest is running, 
 but will startup with VCPUS.

CPU topology can additionally be specified with sockets, cores, and threads. If 
 values are omitted, the rest will be autofilled preferring sockets over cores 
 over threads.  

'cpuset' sets which physical cpus the guest can use. "CPUSET" is a comma separated 
 list of numbers, which can also be specified in ranges or cpus to exclude.

Example:
```
  0,2,3,5     : Use processors 0,2,3 and 5
  1-5,^3,8    : Use processors 1,2,4,5 and 8
```
If the value 'auto' is passed, virt-install attempts to automatically determine 
 an optimal cpu pinning using NUMA data, if available.

Use --vcpus=? to see a list of all available sub options. Complete details at 
 [libvirt.org](http://libvirt.org/formatdomain.html#elementsCPUAllocation)

#### --memory
#### --disk
#### --location
#### --graphics
#### --extra-args
