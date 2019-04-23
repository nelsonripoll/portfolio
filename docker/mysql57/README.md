# MySQL 5.7 
This is an exact replica of the official 
 [MySQL 5.7 Dockerfile](https://github.com/docker-library/mysql/blob/6b1dc54320b03b83a89068f49cc796fea0ff6bb4/5.7/Dockerfile)
 but with OpenJDK 7 JRE and Git installed and a different set of MySQL configuration
 files.

## Run From Registry
```bash
docker pull nelsonripoll/mysql57

docker run  --detach              \
            --tty                 \
            --interactive         \
            --name mysql57        \
            nelsonripoll/mysql57  \
```

## Build & Run From Dockerfile
```bash
git clone https://github.com/nelsonripoll/docker.git

cd docker/mysql57

docker build --rm=true -t mysql57 .

docker run  --detach        \
            --tty           \
            --interactive   \
            --name mysql57  \
            mysql57
```

## Stop & Remove Container
```bash
docker stop mysql57

docker rm mysql57
```
