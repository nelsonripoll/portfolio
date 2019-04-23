# CentOS 7 / Nginx / PHP 7.1
This container is meant to run php web applications on CentOS 7 using Nginx
 and PHP 7.1. There is a non-root user **admin** with sudo privileges and 
 belongs to the **nginx** group. Nginx and PHP-FPM are not daemonized and will 
 be executed in the foreground using Supervisor.

## Run From Registry
```bash
docker pull nelsonripoll/centos7-nginx-php71

docker run  --detach                          \
            --tty                             \
            --interactive                     \
            --name centos7-nginx-php71        \
            nelsonripoll/centos7-nginx-php71  \
            su - admin
```

## Build & Run From Dockerfile
```bash
git clone https://github.com/nelsonripoll/docker.git

cd docker/centos7-nginx-php71

docker build --rm=true -t centos7-nginx-php71 .

docker run  --detach                    \
            --tty                       \
            --interactive               \
            --name centos7-nginx-php71  \
            centos7-nginx-php71
```

## Test Container
Grab the container's IP address and navigate to it using a browser. You should
 see Nginx's default page.

```bash
docker exec centos7-nginx-php71 hostname -i
```

## What next?
You can add a PHP project to **/usr/share/nginx** and replace
 **/etc/nginx/sites-enabled/default.conf** with your project's own Nginx
 configuration. Make sure your project is owned by the **nginx** group.

## Stop & Remove Container
```bash
docker stop centos7-nginx-php71

docker rm centos7-nginx-php71
```
