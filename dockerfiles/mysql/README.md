```shell
# change to this directory
sudo docker build -t mysql . 
sudo docker run -itd -p 3306:3306 mysql
mysql -h 127.0.0.1 -u root -p
```
