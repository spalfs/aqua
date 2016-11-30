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
charts.append(("aqua.Temperature",'','','degrees (F)','random','random','area'))
charts.append(("aqua.Humidity",'','','percent','random','random','line'))
charts.append(("aqua.tankLevel",'','','out of 1200','random','random','line'))
charts.append(("aqua.Light",'','','out of 1200','random','random','line'))
charts.append(("aqua.tankpH",'','','ppi','random','random','line'))

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
            if(c[0]=="aqua.Temperature"):
                self.dimension("Room","Room","absolute","1","1000")
                self.commit()
                self.dimension("Water","Water","absolute","1","1000")
                self.commit()
            elif(c[0]=="aqua.Humidity"):
                self.dimension("Humidity","Humidity","absolute","1","1000")
                self.commit()
            elif(c[0]=="aqua.tankLevel"):
                self.dimension("Level")
                self.commit()
            elif(c[0]=="aqua.Light"):
                self.dimension("Left")
                self.commit()
                self.dimension("Right")
                self.commit()
                self.dimension("Tank")
                self.commit()
                self.dimension("Room")
                self.commit()
            elif(c[0]=="aqua.tankpH"):
                self.dimension("pH","pH","absolute","1","1000")
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

        for c in charts:
            self.begin(c[0], interval)
            if(c[0]=="aqua.Temperature"):
                self.set("Room", fdata[0]*1000)
                self.set("Water", fdata[2]*1000)
                self.end()
                self.commit()
            elif(c[0]=="aqua.Humidity"):
                self.set("Humidity", fdata[1]*1000)
                self.end()
                self.commit()
            elif(c[0]=="aqua.tankLevel"):
                self.set("Level", fdata[3])
                self.end()
                self.commit()
            elif(c[0]=="aqua.Light"):
                self.set("Left", fdata[5])
                self.set("Right", fdata[4])
                self.set("Tank", fdata[6])
                self.set("Room", fdata[7])
                self.end()
                self.commit()
            elif(c[0]=="aqua.tankpH"):
                self.set("pH", fdata[8]*1000)
                self.end()
                self.commit()

        return True
