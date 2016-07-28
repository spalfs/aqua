#!/usr/bin/python3

from flask import Flask, render_template
from scripts import createGraphs, createSystemGraphs, getIP
app = Flask(__name__)

ip = getIP("wlan0")

@app.route('/')
def index():
    status = False
    graphs = createGraphs()
    return render_template('current.html', status = status, layout = "now", graphs = graphs, ip = ip)

@app.route('/recent.html')
def recent():
    status = False
    graphs = createGraphs()
    systemGraphs = createSystemGraphs()
    return render_template('recent.html', status = status, layout = "recent", graphs = graphs, systemGraphs = systemGraphs, ip = ip)

@app.route('/all.html')
def all():
    status = False
    return render_template('all.html', status = status, layout = "all", ip = ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
