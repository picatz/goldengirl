```
# change to this directory
go get github.com/emersion/go-imap/...
go build imap
sudo docker build -t imaps .
sudo docker run -itd -p 993:993 imaps
medusa -s -R 1 -h 0.0.0.0 -n 993 -u picat -p picat -M imap -m AUTH:LOGIN
```
