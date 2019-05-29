# Docker

[Docker](https://www.docker.com/)

[Docker Hub](https://hub.docker.com/)

## Virtual Machines vs Docker Containers
Docker containers are not virtual machine.

### Virtual Machines 
Virtual Machines isolate and test entire systems.

#### Layers
Infrastructure - Desktop, Laptop, dedicated server running in a datacenter, or a virtual
 private server you are running in the cloud.

Host Operating System - Windows, OS X, or Linux.

Hypervisor - Type 1: Direct Link to the Infrastructure (HyperKit for OS X, Hyper-V, 
 for Windows, KVM for Linux). Type 2: Runs as an app on the host operating system
 (VirtualBox, VMWare).

Guest Operating Systems - Windows, OS X, or Linux. All controlled by the hypervisor.
 Each guest operating system would need its own harddrive, cpu, memory, and
 other resources.

Binaries and Libraries - Each guest operating system would need its own copy
 of binaries and libraries for the applications that need to run.

Application - Source code that needs to be ran inside the guest operating system.

### Docker Containers 
Docker containers isolate and deliver applications.

#### Layers
Infrastructure - Desktop, Laptop, dedicated server running in a datacenter, or a virtual
 private server you are running in the cloud.

Host Operating System - Windows, OS X, or Linux.

Docker Daemon - Replaces the hypervisor. Service that runs in the background
 on the host operating system and manages everything required to run and interact
 with docker containers.

Binaries and Libraries - Binaries and libraries needed for the applications that 
 need to run. Gets built into docker images instead of a guest operating system
 then docker daemon runs the images.

Application - Source code that needs to be ran inside the docker image.
