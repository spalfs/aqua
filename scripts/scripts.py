import sqlite3
from datetime import datetime, timedelta
import subprocess
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt


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

def insert(d):
    d = str(d)
    d = d.replace("b","")
    d = d.replace("'","")
    d = d.split(",")
    d = list(map(float,d))
    conn = sqlite3.connect('/mnt/data.db')
    c = conn.cursor()

    try:
        c.execute('''CREATE TABLE data
        (date TEXT,
        time  TEXT,
        rtemp REAL,
        humid REAL,
        wtemp REAL,
        wlevl INTEGER,
        rlite INTEGER,
        llite INTEGER,
        blite INTEGER,
        tlite INTEGER,
        ph    REAL)''')

    except:
        print("data.db already created")

    dnow = datetime.now().date()
    tnow = datetime.now().time()

    c.execute('''INSERT INTO data VALUES
            ('%s',  '%s',   %f,   %f,   %f,   %d,   %d,   %d,   %d,   %d,   %f)''' % (
              dnow, tnow, d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8]))

    conn.commit()
    conn.close()

def plot(data,begin,end):

    if(len(data)==0):
        return 1

    data = str(data).replace("'","")
    data = data.replace("[","")
    data = data.replace("]","")

    conn = sqlite3.connect('/mnt/data.db')
    c = conn.cursor()

    xALL = [()]
    yALL = [()]

    dbegin = datetime.strptime(begin,"%Y-%m-%d").date()
    dend   = datetime.strptime(end,  "%Y-%m-%d").date()

    while(dbegin != (dend + timedelta(days=1))):
        c.execute("SELECT time, date FROM data WHERE date LIKE '%%%s%%'" % (dbegin))
        xALL = xALL + c.fetchall()
        c.execute("SELECT %s FROM data WHERE date LIKE '%%%s%%'" % (data,dbegin))
        yALL = yALL + c.fetchall()
        dbegin = dbegin + timedelta(days=1)

    conn.close()

    xALL = xALL[1:]
    yALL = yALL[1:]

    x = []
    for i in xALL:
        x.append(i[1]+" "+i[0])


    fig, ax = plt.subplots(1)
    fig.autofmt_xdate()

    xALL = mpl.dates.datestr2num(x)

    data = data.split(',')
    for i in range(len(data)):
        ny = [z[i] for z in yALL]
        plt.plot_date(xALL,ny,label=data[i],linestyle='-')

    plt.legend()
    plt.gca().xaxis.set_major_formatter(mpl.dates.DateFormatter("%m/%d \n %H:%M"))
    plt.draw()

    plt.savefig('/home/pi/Desktop/aqua/static/plot_bmh.png',bbox_inches='tight')

def getUniqueDates():
    conn = sqlite3.connect('/mnt/data.db')
    c = conn.cursor()

    c.execute("SELECT DISTINCT date FROM data")
    x = c.fetchall()
    conn.close()
    xL = []
    for i in x:
        xL.append((i[0],i[0]))

    return xL
