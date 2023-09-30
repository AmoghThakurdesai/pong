from models import * 
from app import app,db

GameRecord1 = GameRecord(
    p1score = 0,p2score = 0,player1id=1,player2id=2
)

Game1 = Game(
    p1score = 0, p2score=0,gameid=1
)

Player1 = Player(id = 1,username = 1)
Player2 = Player(id = 2,username = 2)
Player1.set_password("12345")
Player2.set_password("12345")


with app.app_context():
    db.session.add(Game1)
    db.session.add(GameRecord1)
    db.session.add(Player1)
    db.session.add(Player2)
    db.session.commit()