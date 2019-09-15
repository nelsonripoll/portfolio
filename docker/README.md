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

To see the commands that belong to each management command, run ```docker [management command] --help```.

```
# docker system --help

Usage:	docker system COMMAND

Manage Docker

Commands:
  df          Show docker disk usage
  events      Get real time events from the server
  info        Display system-wide information
  prune       Remove unused data

Run 'docker system COMMAND --help' for more information on a command.
```


### Image Management

We can pull images from a docker registry by running the ```docker image pull```
 command. The default docker registry is [Docker Hub](https://hub.docker.com).

```
# docker image pull --help

Usage:	docker image pull [OPTIONS] NAME[:TAG|@DIGEST]

Pull an image or a repository from a registry

Options:
  -a, --all-tags                Download all tagged images in the repository
      --disable-content-trust   Skip image verification (default true)
```

Pull the [official hello-world image](https://hub.docker.com/_/hello-world):

```
# docker image pull hello-world
```

To view docker images that have been pulled to your system:

```
# docker image ls
```

If I wanted to add this docker image to [my docker hub repo](https://hub.docker.com/u/nelsonripoll),
 I would need to tag it with my docker hub username then push to docker hub. Afterwards,
 the image can be found [here](https://hub.docker.com/r/nelsonripoll/hello-world).

```
# docker image tag hello-world nelsonripoll/hello-world
# docker image push nelsonripoll/hello-world
```

If I wanted to remove the hello-world image tag from my system, I would first need
 to run the ```docker image ls``` command and find the tag I want to remove.

```
# docker image ls
REPOSITORY                 TAG                 IMAGE ID            CREATED             SIZE
hello-world                latest              fce289e99eb9        5 months ago        1.84kB
nelsonripoll/hello-world   latest              fce289e99eb9        5 months ago        1.84kB

# docker image rm nelsonripoll/hello-world
Untagged: nelsonripoll/hello-world:latest

# docker image ls
REPOSITORY                 TAG                 IMAGE ID            CREATED             SIZE
hello-world                latest              fce289e99eb9        5 months ago        1.84kB
```

This will not delete image from my user's repository on docker hub. I can still
 pull the image. In order to remove it completely, I would need to delete the
 repo from the docker hub website.

```
# docker image pull nelsonripoll/hello-world
Using default tag: latest
latest: Pulling from nelsonripoll/hello-world
Digest: sha256:92c7f9c92844bbbb5d0a101b22f7c2a7949e40f8ea90c8b3bc396879d95e899a
Status: Downloaded newer image for nelsonripoll/hello-world:latest

# docker image ls
REPOSITORY                 TAG                 IMAGE ID            CREATED             SIZE
hello-world                latest              fce289e99eb9        5 months ago        1.84kB
nelsonripoll/hello-world   latest              fce289e99eb9        5 months ago        1.84kB
```
