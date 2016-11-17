# -*- coding: utf-8 -*-
# Description: example netdata python.d module
# Author: Pawel Krupa (paulfantom)

import os
import random
from base import SimpleService
from socket import socket, AF_INET, SOCK_STREAM, gethostname

NAME = os.path.basename(__file__).replace(".chart.py", "")

# default module values
# update_every = 4
priority = 90000
retries = 60

charts = []
charts.append(("aqua.roomTemperature",'','A random number','random number','random','random','line'))
charts.append(("aqua.roomHumidity",'','A random number','random number','random','random','line'))
charts.append(("aqua.tankTemperature",'','A random number','random number','random','random','line'))
charts.append(("aqua.tankLevel",'','A random number','random number','random','random','line'))
charts.append(("aqua.rightLight",'','A random number','random number','random','random','line'))
charts.append(("aqua.leftLight",'','A random number','random number','random','random','line'))
charts.append(("aqua.tankLight",'','A random number','random number','random','random','line'))
charts.append(("aqua.roomLight",'','A random number','random number','random','random','line'))
charts.append(("aqua.tankpH",'','A random number','random number','random','random','line'))

class Service(SimpleService):
    def __init__(self, configuration=None, name=None):
        super(self.__class__,self).__init__(configuration=configuration, name=name)
        self.s = socket(AF_INET, SOCK_STREAM)
        self.s.bind((gethostname(),6000))
        self.s.listen(5)

    def check(self):
        return True

    def create(self):
        for c in charts:
            self.chart(c[0],c[1],c[2],c[3],c[4],c[5],c[6],self.priority,self.update_every)
            self.dimension("Value")
            self.commit()
        return True

    def update(self, interval):
        con, add = self.s.accept()
        data = con.recv(256)
        if(data):
            data = str(data)
            data = data.replace("b","")
            data = data.replace("'","")
            data = data.replace('"','')
            data = data.split(",")
            fdata = []
        for d in data:
            fdata.append(float(d))

        i = 0
        for c in charts:
            self.begin(c[0], interval)
            self.set("Value", fdata[i])
            self.end()
            self.commit()
            i = i + 1

        return True
