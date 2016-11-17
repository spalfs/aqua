#!/usr/bin/python3

import serial
from time import sleep, time

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
    r = r.split(',')
    r[0] = r[0].replace("b'","")
    r[8] = r[8].replace("\\r","")
    r[8] = r[8].replace("\\n","")
    r[8] = r[8].replace("'","")

    print(r)
