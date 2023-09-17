# #!/usr/bin/env python3
import os
import click
from flask import Flask,render_template,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from models import GameRecord,Player,Game,Base
from flask_migrate import Migrate
from dbinit import engine
from sqlalchemy import Table

basedir = os.path.abspath(os.path.dirname(__file__))
score = {"p1score":0,"p2score":0}


app = Flask(__name__,template_folder='templates')
app.debug=True
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
with app.app_context():    
    gamenum = db.session.query(GameRecord).order_by(GameRecord.gameid.desc()).first().gameid
    table = Table("game", Base.metadata, autoload_with=engine)
    with engine.begin() as connection:
        connection.execute(table.delete())
gamenum+=1
migrate = Migrate(app,db)
# game = GameRecord(gameid = gamenum,player1score = 0,player2score = 0,player1id=1,player2id=1)


@app.route('/',methods=["GET","POST"])
def pong():
    headers = Game.__table__.columns.keys()
    rows = db.session.query(Game).all()
    rows = [
        [
        record.recordid,
        record.gameid, 
        record.p1score, 
        record.p2score
        ] 
        for record in rows
        ]
    
    headergamerecord = GameRecord.__table__.columns.keys()
    rowsgamerecord = db.session.query(GameRecord).all()
    rowsgamerecord = [
        [
        record.gameid, 
        record.p1score, 
        record.p2score,
        record.player1id,
        record.player2id,
        record.created_at
        ] 
        for record in rowsgamerecord
    ]
    print(rows,headers)
    return render_template(
        "pong.html",
        headers=headers,
        rows=rows,
        headergamerecord = headergamerecord,
        rowsgamerecord = rowsgamerecord
    )

@app.route('/process',methods=['POST'])
def scoreboard():
    data = request.get_json()
    global gamenum
    if(data["player1win"]==1):
        score["p1score"]+=1
    else:
        score["p2score"]+=1
    game = Game(
        gameid = gamenum,
        p1score = score["p1score"],
        p2score = score["p2score"],
        )
    db.session.add(game)
    db.session.commit()
    return jsonify(score)

@app.route('/newgame',methods=['GET'])
def newgame():
    global gamenum
    gamenum = db.session.query(Game).order_by(Game.gameid.desc()).first().gameid
    gamerecord = GameRecord(
        gameid = gamenum,
        p1score = score["p1score"],
        p2score = score["p2score"],
        player1id=1,
        player2id=2
        )
    gamenum+=1
    score["p1score"] = 0
    score["p2score"] = 0
    db.session.add(gamerecord)
    db.session.commit()
    
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


