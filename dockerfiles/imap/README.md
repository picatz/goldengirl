```
# change to this directory
go get github.com/emersion/go-imap/...
go build imap
sudo docker build -t imap .
sudo docker run -itd -p 143:143 imap
medusa -R 1 -h 0.0.0.0 -n 143 -u picat -p picat -M imap -m AUTH:LOGIN
```
