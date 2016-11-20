import subprocess

class dimension():
    def __init__(self,title):
        self.title = title

class graph():
    def __init__(self,title,data,units,color,dimensions):
        self.title = title
        self.data  = data
        self.units = units
        self.color = color
        self.dimensions = dimensions

def createGraphs():
    graphs = list()

    d = []
    d.append(dimension("Room"))
    d.append(dimension("Water"))
    graphs.append(graph("Temperature", "aqua.Temperature", "degrees (F)", "", d))

    d = []
    d.append(dimension("Humidity"))
    graphs.append(graph("Humidity", "aqua.Humidity", "percent", "#55ffaa", d))

    d = []
    d.append(dimension("Left"))
    d.append(dimension("Right"))
    d.append(dimension("Tank"))
    d.append(dimension("Room"))
    graphs.append(graph("Lighting", "aqua.Light", "percent", "", d))

    d = []
    d.append(dimension("pH"))
    graphs.append(graph("pH", "aqua.tankpH", "ppi", "#ffaa55", d))

    d = []
    d.append(dimension("Level"))
    graphs.append(graph("Water Level", "aqua.tankLevel", "inches", "#aaff55", d))

    return graphs

def createSystemGraphs():
    graphs = list()

    d = []
    graphs.append(graph("CPU Utilization", "system.cpu"," "," ",d))
    graphs.append(graph("System Load", "system.load"," "," ",d))
    graphs.append(graph("Disk I/O", "system.io"," "," ",d))
    graphs.append(graph("System Memory", "system.ram"," "," ",d))

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

