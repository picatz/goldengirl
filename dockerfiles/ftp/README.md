```
# change to this directory
sudo docker build -t ftp .
sudo docker run -itd -p 21:21 ftp
sudo python test.py 0.0.0.0 21 root picat /example wiggle
```
