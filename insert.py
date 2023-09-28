from models import * 
from app import app,db

GameRecord1 = GameRecord(
    p1score = 0,p2score = 0,player1id=1,player2id=2
)

Game1 = Game(
    p1score = 0, p2score=0,gameid=1
)

with app.app_context():
    db.session.add(Game1)
    db.session.add(GameRecord1)
    db.session.commit()