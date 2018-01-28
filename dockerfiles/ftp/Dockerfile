FROM python:2.7

RUN pip install pyftpdlib

COPY ftp-server.py /ftp-server.py

EXPOSE 21

CMD [ "python", "./ftp-server.py" ]
