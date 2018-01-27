FROM centos:7 

COPY dns /dns

RUN chmod +x /dns

EXPOSE 5353/udp

CMD ["./dns"]
