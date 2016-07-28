class graph():
    def __init__(self,title,data,units,color):
        self.title = title
        self.data  = data
        self.units = units
        self.color = color

def createGraphs():
    graphs = list()

    graphs.append(graph("Room Temperature", "aqua.basic", "degrees (F)", "#ff5555"))
    graphs.append(graph("Room Humidity", "aqua.basic", "percent", "#55ffaa"))
    graphs.append(graph("Room Lighting", "aqua.basic", "percent", "#5555ff"))

    return graphs

