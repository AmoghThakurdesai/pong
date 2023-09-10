#!/usr/bin/env python3

from flask import Flask,abort,render_template,request
from markupsafe import escape
from mlmodel.models import linregmultiplevariables
from mlmodel.util import selecttable
import numpy as np
import pandas as pd

app = Flask(__name__, template_folder='templates')

@app.route('/',methods=["GET","POST"])
@app.route('/seaborndatasets',methods=["GET","POST"])
def hello():
    data = 0
    if request.method == "POST":
        data = request.form["data1"]
    table  = selecttable(int(data))
    output = {
                "table":table[0],
                "tableheading":table[1], 
                "data1":data,
                "datasetlist": table[2]
             }
    return render_template("home.html", output = output)

@app.route('/pong/',methods=['GET','POST'])
def pong():
    return render_template("pong.html")
