import os
from sqlalchemy import create_engine, MetaData
from models import Base,Player,GameRecord,Game

basedir = os.path.abspath(os.path.dirname(__file__))
database_url = 'sqlite:///' + os.path.join(basedir, 'database.db')
engine = create_engine(database_url)
Base.metadata.bind = engine
Base.metadata.create_all(engine)




# class Game(Base):
#     """
#     returns history of scores for a particular game
#     """
#     __tablename__ = 'game'
#     recordid = Column(
#         Integer,
#         unique=True,
#         primary_key=True,
#         autoincrement=True
#     )
#     gameid = Column(
#         Integer,
#         ForeignKey("gamerecord.gameid")
#     )
#     p1score = Column(
#         Integer,
#         unique=False,
#         nullable=True
#     )
#     p2score = Column(
#         Integer,
#         unique=False,
#         nullable=True
#     )
    
    # class GameRecord(Base):
    # __tablename__ = 'gamerecord'
    # gameid = Column(
    #     Integer,
    #     unique=True,
    #     autoincrement=True,
    #     primary_key=True
    #     )
    # p1score = Column(
    #     Integer,
    #     unique=False, 
    #     nullable=False, 
    #     )
    # p2score = Column(
    #     Integer,
    #     unique=False, 
    #     nullable=False
    #     )
    # player1id = Column(
    #     Integer,
    #     ForeignKey("player.id"),
    #     unique=False, 
    #     nullable = False
    #     )
    # player2id = Column(
    #     Integer,
    #     ForeignKey("player.playerid"),
    #     unique=False, 
    #     nullable = False
    # )
    
    # created_at = Column(
    #     DateTime(timezone=True),
    #     server_default=func.now()
    #     )
    # def __repr__(self):
    #     return f"Game {self.gameid}"

# Player1 = Player(playerid = 1,username = "A")
# Player1.set_password("12345") 

# Player2 = Player(playerid = 2,username = "B")
# Player2.set_password("12345")

# with app.app_context():
#     db.session.add(Player1)
#     db.session.add(Player2)
#     db.session.commit()