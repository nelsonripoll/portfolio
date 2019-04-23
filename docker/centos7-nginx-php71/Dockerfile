FROM        centos:7
MAINTAINER  nelsonripoll

RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
    rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm

RUN yum -y -q update && \
    yum -y -q install sudo git rsync nginx php71w php71w-common php71w-cli \ 
    php71w-fpm php71w-intl php71w-ldap php71w-mbstring php71w-mysqlnd \ 
    php71w-pecl-xdebug php71w-pdo php71w-soap php71w-xml supervisor && \
    yum clean all

RUN useradd -m -G nginx -s /bin/bash admin && \
    echo "admin ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/admin && \
    chmod 0440 /etc/sudoers.d/admin

RUN if [ ! -d /etc/nginx/sites-enabled ]; then mkdir /etc/nginx/sites-enabled; fi

COPY etc /etc

COPY install-composer.sh ./

RUN ./install-composer.sh && rm install-composer.sh

COPY composer-cakephp3x.sh /usr/share/nginx/composer-cakephp3x.sh 
COPY composer-update.sh    /usr/share/nginx/composer-update.sh 
COPY fix-permissions.sh    /usr/share/nginx/fix-permissions.sh

EXPOSE 22 80

CMD ["/usr/bin/supervisord"]
