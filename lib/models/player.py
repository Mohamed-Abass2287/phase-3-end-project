from sqlalchemy import Column, Integer, String
from . import Base

class Player(Base):
    __tablename__ = "players"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    health = Column(Integer, default=100)
    inventory = Column(String, default="[]")
    current_room = Column(Integer, default=1)

    def add_item(self, item):
        items = eval(self.inventory)
        items.append(item)
        self.inventory = str(items)