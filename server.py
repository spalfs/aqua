#!/usr/bin/python3

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    status = False
    return render_template('index.html', status = status)

@app.route('/recent.html')
def recent():
    status = False
    return render_template('recent.html', status = status)

@app.route('/all.html')
def all():
    status = False
    return render_template('all.html', status = status)

if __name__ == '__main__':
    app.run(debug=True)
