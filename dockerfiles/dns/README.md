```
# change into this directory
go get github.com/miekg/dns
go build dns.go 
sudo docker build -t dns .
 sudo docker run -itd -p 53:5353/udp dns
dig @localhost test.service
```
