#!/usr/bin/env python3

from flask import Flask,abort,render_template,request
from flask_sqlalchemy import SQLAlchemy

from markupsafe import escape
from mlmodel.models import linregmultiplevariables
from mlmodel.util import selecttable
import numpy as np
import pandas as pd

app = Flask(__name__, template_folder='templates')
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Game(db.Model):
    gameid = db.Column(db.Integer,primary_key=True)
    p1score = db.Column(db.Integer,unique=False, nullable=False)
    p2score = db.Column(db.Integer,unique=False, nullable=False)
   
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

@app.route('/',methods=["GET","POST"])
def pong():
    return render_template("pong.html")
