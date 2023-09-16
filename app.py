# #!/usr/bin/env python3
import os
import click
from flask import Flask,render_template,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from models import Game,Player,GameHistory

basedir = os.path.abspath(os.path.dirname(__file__))
score = {"p1score":0,"p2score":0}
gamenum=0

app = Flask(__name__,template_folder='templates')
app.debug=True
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)




@app.route('/',methods=["GET","POST"])
def pong():
    game1 = Game(gameid = gamenum,);
    return render_template("pong.html")

@app.route('/process',methods=['POST'])
def scoreboard():
    data = request.get_json()
    if(data["player1win"]==1):
        score["p1score"]+=1
    else:
        score["p2score"]+=1
    gamenum+=1
    return jsonify(score)




### the below code is problematic because we cant import mlmodels package here 
### sort this out later.

# from markupsafe import escape
# from mlmodel.models import linregmultiplevariables
# from mlmodel.util import selecttable
# import numpy as np
# import pandas as pd  
# @app.route('/seaborndatasets',methods=["GET","POST"])
# def hello():
#     print("hello runs")
#     data = 0
#     if request.method == "POST":
#         data = request.form["data1"]
#     table  = selecttable(int(data))
#     output = {
#                 "table":table[0],
#                 "tableheading":table[1], 
#                 "data1":data,
#                 "datasetlist": table[2]
#              }
#     return render_template("home.html", output = output)


