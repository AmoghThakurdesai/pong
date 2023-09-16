import os
from sqlalchemy import create_engine, MetaData
from models import Base,Player
from app import db,app

basedir = os.path.abspath(os.path.dirname(__file__))
database_url = 'sqlite:///' + os.path.join(basedir, 'database.db')
engine = create_engine(database_url)
Base.metadata.bind = engine
Base.metadata.create_all(engine)

Player1 = Player(playerid = 1,username = "A")
Player1.set_password("12345") 

Player2 = Player(playerid = 2,username = "B")
Player2.set_password("12345")

with app.app_context():
    db.session.add(Player1)
    db.session.add(Player2)
    db.session.commit()