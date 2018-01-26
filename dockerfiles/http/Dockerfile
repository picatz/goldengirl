FROM centos:centos7

RUN yum -y update \
    && yum -y install httpd \
    && yum -y clean all

COPY httpd-foreground /usr/local/bin/
COPY etc-httpd/ /etc/httpd/
COPY var-www-html/ /var/www/html/

RUN chmod +x /usr/local/bin/httpd-foreground

EXPOSE 80 

CMD ["httpd-foreground"]
