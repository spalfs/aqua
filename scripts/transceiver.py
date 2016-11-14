#!/usr/bin/python3

import serial
from time import sleep, time

comms = serial.Serial('/dev/ttyUSB0', 9600)
w = "on"
start = time()

while True:
        timer = time() - start

    if w == "on":
        if (timer > 90):
            start = time()
            w = "off"
    else:
        if (timer > 30):
            start = time()
            w = "on"

    comms.write(str.encode(w))
    print(str.encode(w))

    sleep(3)

    r = comms.readline()
    r = r.split(',')

    print(r)

