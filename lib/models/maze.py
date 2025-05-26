from sqlalchemy import Column, Integer, String, JSON
from . import Base

class Room(Base):
    __tablename__ = "rooms"
    
    id = Column(Integer, primary_key=True)
    description = Column(String)
    exits = Column(JSON)
    items = Column(JSON)

class Maze(Base):
    __tablename__ = "mazes"
    
    id = Column(Integer, primary_key=True)
    start_room = Column(Integer)
    exit_room = Column(Integer)