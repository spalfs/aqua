#!/usr/bin/python3

from socket import socket, AF_INET, SOCK_STREAM, gethostname
from time import sleep

s = socket(AF_INET,SOCK_STREAM)
s.bind((gethostname(),6000))
s.listen(5)

while True:
    connection, address = s.accept()
    data = connection.recv(256)
    if(data):
        data = str(data)
        data = data.replace("b","")
        data = data.replace("'","")
        data = data.replace('"','')
        data = data.split(",")
        fdata = []
        for d in data:
            fdata.append(float(d))

        print(fdata)
