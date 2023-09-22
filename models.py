from passlib.hash import bcrypt_sha256
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import create_engine,ForeignKey,func
from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def hash_password(password):
    # Generate a salted hash of the password
    return bcrypt_sha256.hash(password)

class GameRecord(Base):
    __tablename__ = 'gamerecord'
    gameid = Column(
        Integer,
        unique=True,
        autoincrement=True,
        primary_key=True
        )
    p1score = Column(
        Integer,
        unique=False, 
        nullable=False, 
        )
    p2score = Column(
        Integer,
        unique=False, 
        nullable=False
        )
    player1id = Column(
        Integer,
        ForeignKey("player.id"),
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

class Player(UserMixin,Base):

    __tablename__ = 'player'
    id = Column(
        Integer,
        unique=True, 
        nullable = True,
        autoincrement=True,
        primary_key=True,
    )
    username = Column(
        String,
        unique=False, 
        nullable = False
    )
    password = Column(
        String,
        unique=False,
        nullable= False
    )

    def verify_password(self,password):
    # Verify the input password against the stored hash
        return bcrypt_sha256.verify(password, self.password)

    def set_password(self,password):
        self.password = hash_password(password)
    
class Game(Base):
    """
    returns history of scores for a particular game
    """
    __tablename__ = 'game'
    recordid = Column(
        Integer,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    gameid = Column(
        Integer,
        ForeignKey("gamerecord.gameid")
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
    
