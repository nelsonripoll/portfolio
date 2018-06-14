Install gcc to build from projects from source

```
yum install gcc
```

## NGINX

### Install prerequisites

#### PCRE (Perl Compatible Regular Expressions)

PCRE is required regular expressions support and the ngx\_http\_rewrite\_module. 

Install pcre and pcre2 and their respective libraries for the http rewrite module.
```
yum install pcre pcre-static pcre2 pcre2-static
```

#### ZLib

Zlib is a cross-platform, lossless data-compression library used for the http\_zip\_module to compress the responses of an HTTP server.

Install zlib and its libraries.
```
yum install zlib zlib-static
```

### Nginx Source

Get the nginx source.
```
wget http://nginx.org/download/nginx-1.10.1.tar.gz
tar -xzf nginx-1.10.1.tar.gz
cd nginx-1.10.1
```

### Configure

```
./configure
```

#### Options

By default, log files are located at /usr/local/nginx/logs. The log paths can be changed in the nginx.conf file or during configuration.
```
./configure --http-log-path=*name* --error-log-path=*name*
```

By default, user and group for the server worker processes is not set. The username and group can be set in the nginx.conf file or during configuration.
```
./configure --user=*name* --group=*name*
```


#### Modules

If you have the source to the PCRE library, provide the path to be compiled with nginx.
```
./configure --with-pcre=/path/to/pcre/source
```

If you do not want to have the server redirect requers and change URI of requests, disable the ngx\_http\_rewrite\_module.
```
./configure --without-http_rewrite_module
```

If you do not want to compress the server responses, disable the ngx\_http\_gzip\_module.
```
./configure --without-http_gzip_module
```

If you want to use the HTTPS protocol on the server, enable the ngx\_http\_ssl\_module.
```
./configure --with-http_ssl_module
```

All options and modules have to be set in the same configure command before installing.
```
./configure --with-http_ssl_module \
            --http-log-path=/var/log/nginx/access.log \
            --error-log-path=/var/log/nginx/error.log \
            --user=www \
            --group=www
		
```

### Install

```
make
sudo make install
```
