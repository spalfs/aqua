#!/usr/bin/python3

from flask import Flask, render_template
from flask.ext.wtf import FlaskForm
from wtforms import SelectMultipleField, widgets, SubmitField, SelectField
from scripts.scripts import createGraphs, createSystemGraphs, getIP, getUniqueDates, plot

SECRET_KEY = 'dev'

app = Flask(__name__)
app.config.from_object(__name__)

def getFields():
    return [("rtemp,wtemp","Temperature")
           ,("humid","Humidity")
           ,("rlite,llite,blite,tlite","Lighting")
           ,("ph","pH")
           ,("wlevl","Water Level")]

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class SimpleForm(FlaskForm):
    x = getFields()
    rField = MultiCheckboxField('Parameters',choices=x)
    x = getUniqueDates()
    sField = SelectField('Start', choices=x)
    eField = SelectField('End', choices=x)

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
        plot(form.rField.data, form.sField.data, form.eField.data)
        return render_template('all.html', layout = "all", ip = ip, form = form)
    else:
        print (form.errors)
    return render_template('all.html', layout = "all", ip = ip, form = form)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
