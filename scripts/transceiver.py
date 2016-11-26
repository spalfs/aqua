#!/usr/bin/python3

import serial
from time import sleep, time
from socket import socket, AF_INET, SOCK_STREAM
from scripts import insert

sleep(5)

comms = serial.Serial('/dev/ttyUSB0', 9600, timeout = None)
w = "on"
start = time()
send = True
sleep(5)

while True:
    sleep(0.1);

    timer = time() - start

    if w == "on":
        if (timer > 90):
            start = time()
            w = "off"
            send = True
    else:
        if (timer > 30):
            start = time()
            w = "on"
            send = True

    if(send):
        comms.write(str.encode(w))
        send = False
    else:
        comms.write(str.encode("c"))

    r = str(comms.readline())
    r = r.replace("\\r","")
    r = r.replace("\\n","")

    s = socket(AF_INET,SOCK_STREAM)
    s.connect(("raspberrypi",6000))
    s.sendall(str.encode(r))
    s.close()
    insert(r)

