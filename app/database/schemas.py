from sqlalchemy import Column, String, Integer, Float, TIMESTAMP, JSON
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    email = Column(String, nullable=True)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    
    
class Tracks(Base):
    __tablename__ = "tracks"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    artist = Column(Integer, ForeignKey("users.id"))
    duration = Column(Float)
    
    
class Playlists(Base):
    __tablename__ = "playlists"
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    owner = Column(Integer, ForeignKey("users.id"))


class PlaylistsLikes(Base):
    __tablename__ = "playlists_likes"
    playlist_id = Column(Integer, ForeignKey("playlists.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    
    
class TracksLikes(Base):
    __tablename__ = "tracks_likes"
    track_id = Column(Integer, ForeignKey("tracks.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)

