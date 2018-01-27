```
# change to this directory
sudo docker build -t smtp .
sudo docker run -itd -p 25:25 smtp
```

```python
[vagrant@goldengirl tmail]$ python
Python 2.7.5 (default, Aug  4 2017, 00:39:18) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-16)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import smtplib
>>> server = smtplib.SMTP("0.0.0.0", 25)
>>> server.ehlo()
(250, 'picat.com\nPIPELINING\nSIZE 10240000\nVRFY\nETRN\nSTARTTLS\nAUTH PLAIN LOGIN CRAM-MD5 DIGEST-MD5 NTLM\nAUTH=PLAIN LOGIN CRAM-MD5 DIGEST-MD5 NTLM\nENHANCEDSTATUSCODES\n8BITMIME\nDSN')
>>> server.login("picat", "password")
(235, '2.7.0 Authentication successful')
>>> exit()
```
