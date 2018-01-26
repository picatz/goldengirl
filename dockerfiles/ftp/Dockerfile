FROM centos:centos7

RUN yum -y update \
        && yum -y install pure-ftpd \
        && yum -y clean all \
        && rm /etc/pure-ftpd/pure-ftpd.conf

COPY pure-ftpd.conf /etc/pure-ftpd/

RUN systemctl start pure-ftpd.service \
        && groupadd default \
        && useradd -g default default \
        && mkdir /home/ftp \
        && pure-pw useradd defaultvuser -u default -d /home/ftp/defaultvuser \
        && mkdir /home/ftp/defaultvuser \
        && chown -R default.default /home/ftp/defaultvuser \
        && pure-pw mkdb

EXPOSE 21
