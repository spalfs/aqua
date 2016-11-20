#!/usr/bin/python3

from flask import Flask, render_template
from scripts.scripts import createGraphs, createSystemGraphs, getIP
app = Flask(__name__)

ip = getIP("wlan0")

@app.route('/')
def index():
    graphs = createGraphs()
    return render_template('current.html', layout = "now", graphs = graphs, ip = ip)

@app.route('/recent.html')
def recent():
    graphs = createGraphs()
    systemGraphs = createSystemGraphs()
    return render_template('recent.html', layout = "recent", graphs = graphs, systemGraphs = systemGraphs, ip = ip)

@app.route('/all.html')
def all():
    return render_template('all.html', layout = "all", ip = ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
