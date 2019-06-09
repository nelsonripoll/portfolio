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

## Running Docker
Docker has two sets of commands: regular commands and management commands. As of
 Docker 1.13, regular commands have been grouped logically into management commands.

By running ```docker --help```, you can see a list of management commands and
 the original commands.

```
# docker --help

Usage:	docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default "/Users/nelsonripoll/.docker")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default "/Users/nelsonripoll/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default "/Users/nelsonripoll/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default "/Users/nelsonripoll/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  ...

Commands:
  ...
```

The ```docker run``` command is now part of the container management command.

```
# docker container run hello-world 

Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
1b930d010525: Pull complete
Digest: sha256:0e11c388b664df8a27a901dce21eb89f11d8292f7fca1b3e3c4321bf7897bffe
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

To see the commands that belong to each management command, run ```docker [management command] --help```.

```
docker system --help

Usage:	docker system COMMAND

Manage Docker

Commands:
  df          Show docker disk usage
  events      Get real time events from the server
  info        Display system-wide information
  prune       Remove unused data

Run 'docker system COMMAND --help' for more information on a command.
```
