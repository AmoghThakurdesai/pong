#!/usr/bin/env python3

from flask import Flask,abort,render_template,request
from markupsafe import escape
from mlmodel.newmodel import linreg, selecttable
import numpy as np
import pandas as pd

app = Flask(__name__, template_folder='templates')


@app.route('/',methods=["GET","POST"])
def hello():
    data = 0
    if request.method == "POST":
        data = request.form["data1"]
    table  = selecttable(int(data))
    output = {"table":table[0],
              "tableheading":table[1], 
              "data1":data,
              "datasetlist": table[2]
            }
    return render_template("home.html", output = output)