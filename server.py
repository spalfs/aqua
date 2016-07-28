#!/usr/bin/python3

from flask import Flask, render_template
from graphs import createGraphs
app = Flask(__name__)

@app.route('/')
def index():
    status = False
    graphs = createGraphs()
    return render_template('index.html', status = status, layout = "now", graphs = graphs)

@app.route('/recent.html')
def recent():
    status = False
    return render_template('index.html', status = status, layout = "recent")

@app.route('/all.html')
def all():
    status = False
    return render_template('index.html', status = status, layout = "all")

@app.route('/roomtemp.html')
def roomtemp():
    status = False
    return render_template('roomtemp.html', status = status)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
