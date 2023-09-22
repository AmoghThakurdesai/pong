# #!/usr/bin/env python3
import os
import click
from flask import Flask,render_template,request,jsonify,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from models import GameRecord,Player,Game,Base
from flask_migrate import Migrate
from dbinit import engine
from sqlalchemy import Table
from flask_login import LoginManager, login_user

file = open("../secret_key.txt","r")
secretkey = file.read()
basedir = os.path.abspath(os.path.dirname(__file__))
score = {"p1score":0,"p2score":0}


# TODO: set up flask sqlalchemy secret key in file and import it here 
app = Flask(__name__,template_folder='templates')
app.debug=True
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = secretkey


login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)
@login_manager.user_loader
def load_user(username):
    return Player.get(username)
db = SQLAlchemy(app)
with app.app_context(): 
    from models import *   
    gamenum = db.session.query(GameRecord).order_by(GameRecord.gameid.desc()).first()
    if gamenum:
        gamenum = gamenum.gameid
        gamenum+=1
    table = Table("game", Base.metadata, autoload_with=engine)
    with engine.begin() as connection:
        connection.execute(table.delete())




migrate = Migrate(app,db)
# game = GameRecord(gameid = gamenum,player1score = 0,player2score = 0,player1id=1,player2id=1)


@app.route('/pong',methods=["GET","POST"])
def pong():
    headers = Game.__table__.columns.keys()
    rows = db.session.execute(db.select(Game))
    if rows:
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
    if rowsgamerecord:
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


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def login_process():
    username = request.form.get("username")
    password = request.form.get("password")
    
    player = db.session.scalars(db.select(Player).filter_by(username = username)).one()
    print()
    print()
    print()
    print(player.id,player.password,player.username)
    print()
    print()
    print()
    print()
    if not player:
        if not player.verify_password(password):
            flash("Please check your login details and try again")
            return redirect(url_for("login"))

    login_user(player,remember=True)
    return redirect(url_for("profile"))

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/signup",methods=["POST"])
def signup_process():
    username=request.form.get("username")
    password = request.form.get("password")
    
    player = db.session.execute(db.select(Player).filter_by(username = username)).first()
    if player:
        flash("Username already exists")
        return redirect(url_for("signup"))
    
    new_player = Player(
        username = username
        ) 
    new_player.set_password(password)
    db.session.add(new_player)
    db.session.commit()

    return redirect(url_for("pong"))

@app.route("/logout")
def logout():
    return "Logout"

file.close()
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


