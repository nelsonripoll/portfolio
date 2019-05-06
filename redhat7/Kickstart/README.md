# Kickstart
## Mount ISO
```
# mount -o loop CentOS7.iso /media
```
## HTTP
Run the following commands then use a browser to navigate to http://192.168.122.1/inst.
```
# yum install httpd
# mkdir /var/www/html/inst
# mkdir /var/www/html/ks
# cp -a /media/. /var/www/html/inst/
# cp /root/anaconda-ks.cfg /var/www/html/ks/ks1.cfg
# chcon -R --reference=/var/www/html /var/www/html/inst
# firewall-cmd --permanent --add-service=http
# firewall-cmd --reload
# systemctl restart httpd
```
## FTP
Run the following commands then use a browser to navigate to ftp://192.168.122.1/pub/inst.
```
# yum install vsftpd
# mkdir /var/ftp/pub/inst
# mkdir /var/ftp/pub/ks
# cp -a /media/. /var/ftp/pub/inst
# cp /root/anaconda-ks.cfg /var/ftp/pub/ks/ks1.cfg
# chcon -R -t public_content_t /var/ftp/
# firewall-cmd --permanent --add-service=ftp
# firewall-cmd --reload
# systemctl restart vsftpd
```
