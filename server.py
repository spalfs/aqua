#!/usr/bin/python3

from flask import Flask, render_template
from flask.ext.wtf import Form
from wtforms import SelectMultipleField, widgets, SubmitField
from scripts.scripts import createGraphs, createSystemGraphs, getIP

SECRET_KEY = 'dev'

app = Flask(__name__)
app.config.from_object(__name__)

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class SimpleForm(Form):
    rField = MultiCheckboxField('Parameters',choices=[("rt","RoomTemp"),("wt","WaterTemp"),("pH","pH"),("wl","Water Level")])

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

@app.route('/all.html',methods=['post','get'])
def all():
    form = SimpleForm()
    if form.validate_on_submit():
        print (form.rField.data)
    else:
        print (form.errors)
    return render_template('all.html', layout = "all", ip = ip, form = form)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
