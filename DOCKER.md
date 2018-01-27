# 🐳 Docker
> We adopted a whale!

Docker is a software technology providing *operating-system-level virtualization* also known as "containers".

## How to Install

You'll find that `docker` is already installed for you on the golden image! No need to install it on your host.

## What is a `Dockerfile`?

Docker allows you to build your own custom containers. The way you to this is by creating a `Dockerfile`.

```dockerfile
FROM centos:7

RUN yum -y --setopt=tsflags=nodocs update && \
    yum -y --setopt=tsflags=nodocs install httpd && \
    yum clean all

EXPOSE 80

# Simple startup script to avoid some issues observed with container restart
ADD run-httpd.sh /run-httpd.sh
RUN chmod -v +x /run-httpd.sh

CMD ["/run-httpd.sh"]
```

* `FROM` tells docker what base image you want to use. We're using a centos 7 variant.
* `RUN` allows you to run some shell commands. Specifically, the example is using `yum` to install stuff.
* `EXPOSE` will allow the docker container to listen on a specific port.
* `ADD` allows you to add files form the host to the docker guest image.
* `CMD` will run the command as the main process for this httpd container, running the server.
