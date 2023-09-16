from passlib.hash import bcrypt_sha256
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine,ForeignKey,func
from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def hash_password(password):
    # Generate a salted hash of the password
    return bcrypt_sha256.hash(password)

class Game(Base):
    __tablename__ = 'game'
    gameid = Column(
        Integer,
        unique=True,
        autoincrement=True,
        )
    p1score = Column(
        Integer,unique=False, 
        nullable=False, 
        primary_key=True,
        )
    p2score = Column(
        Integer,
        unique=False, 
        nullable=False
        )
    player1id = Column(
        Integer,
        ForeignKey("player.playerid"),
        unique=False, 
        nullable = False
        )
    player2id = Column(
        Integer,
        ForeignKey("player.playerid"),
        unique=False, 
        nullable = False
    )
    
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
        )
    def __repr__(self):
        return f"Game {self.gameid}"

class Player(Base):

    __tablename__ = 'player'
    playerid = Column(
        Integer,
        unique=True, 
        nullable = True,
        autoincrement=True,
        primary_key=True,
    )
    username = Column(
        Integer,
        unique=False, 
        nullable = False
    )
    password = Column(
        String,
        unique=False,
        nullable= False
    )

    def verify_password(self):
    # Verify the input password against the stored hash
        input_password = input()
        return bcrypt_sha256.verify(input_password, self.password)

    def set_password(self,password):
        self.password = hash_password(password)
    
class GameHistory(Base):
    """
    returns history of scores for a particular game
    """
    __tablename__ = 'gamehistory'
    recordid = Column(
        Integer,
        unique=True,
        primary_key=True
    )
    gameid = Column(
        Integer,
        ForeignKey("game.gameid")
    )
    p1score = Column(
        Integer,
        unique=False,
        nullable=True
    )
    p2score = Column(
        Integer,
        unique=False,
        nullable=True
    )
    
