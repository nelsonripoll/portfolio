# NGINX

## CentOS 7
### Install prerequisites
Installing nginx from source requires a c/c++ compiler.
```
yum install gcc
```

#### PCRE (Perl Compatible Regular Expressions)
PCRE is used for regular expressions and is required for ngx\_http\_rewrite\_module. 

Install pcre and pcre2 and their respective libraries for the http rewrite module.
```
yum install pcre pcre-static pcre2 pcre2-static
```

#### ZLib
Zlib is a data-compression library used for the http\_zip\_module to compress the responses of a HTTP server.

Install zlib and its libraries.
```
yum install zlib zlib-static
```

## Configure & Install
Get the nginx tarball and unpack it.
```
wget http://nginx.org/download/nginx-1.10.1.tar.gz
tar -xzf nginx-1.10.1.tar.gz
cd nginx-1.10.1
```

Run the configure script to build the relationship and generate the makefile.
```
./configure
```

### Options
By default, log files are located at /usr/local/nginx/logs. The log paths can be changed in the nginx.conf file or during configuration.
```
./configure --http-log-path=*name* --error-log-path=*name*
```

By default, user and group for the server worker processes is not set. The username and group can be set in the nginx.conf file or during configuration. The user and group must exist or nginx will not run.
```
./configure --user=*name* --group=*name*
```


### Modules
If you have the source to the PCRE library, provide the path to be compiled with nginx.
```
./configure --with-pcre=/path/to/pcre/source
```

If you do not want to have the server redirect or change the URI of requests, disable the ngx\_http\_rewrite\_module.
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
Install with make.
```
make
sudo make install
```
