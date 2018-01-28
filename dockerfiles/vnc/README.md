```
# change into this directory
sudo docker build -t vnc .
sudo docker run -itd -p 5901:5901 vnc
medusa -R 1 -h 0.0.0.0 -n 5901 -u picat -p picat -M vnc
```
