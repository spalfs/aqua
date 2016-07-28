import subprocess

class graph():
    def __init__(self,title,data,units,color):
        self.title = title
        self.data  = data
        self.units = units
        self.color = color

def createGraphs():
    graphs = list()

    graphs.append(graph("Room Temperature", "example.python_random", "degrees (F)", "#ff5555"))
    graphs.append(graph("Room Humidity", "aqua.basic", "percent", "#55ffaa"))
    graphs.append(graph("Room Lighting", "aqua.basic", "percent", "#5555ff"))
    graphs.append(graph("Tank Temperature", "aqua.basic", "degrees (F)", "#55ffff"))
    graphs.append(graph("Tank pH", "aqua.basic", "ppi", "#ffaa55"))
    graphs.append(graph("Tank Water Level", "aqua.basic", "inches", "#aaff55"))

    return graphs

def createSystemGraphs():
    graphs = list()

    graphs.append(graph("CPU Utilization", "system.cpu"," "," "))
    graphs.append(graph("System Load", "system.load"," "," "))
    graphs.append(graph("Disk I/O", "system.io"," "," "))
    graphs.append(graph("System Memory", "system.ram"," "," "))

    return graphs

def getIP(card):
    proc = subprocess.Popen("/sbin/ifconfig",stdout=subprocess.PIPE)
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        if card in str(line):
            line = proc.stdout.readline()
            line = str(line)
            #im sorry
            ip = line.split(" ")[11][5:]

    return ip

