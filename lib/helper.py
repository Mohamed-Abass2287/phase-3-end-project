from .models.player import Player
from .models.maze import Maze, Room

def create_initial_maze(session):
    # Create starting room
    start_room = Room(
        description="A cold stone chamber with damp walls",
        exits={"north": 2},
        items=["torch"]
    )
    
    # Create exit room
    exit_room = Room(
        description="A bright chamber with an exit portal",
        exits={"south": 1},
        items=["key"]
    )
    
    maze = Maze(start_room=1, exit_room=2)
    
    session.add_all([start_room, exit_room, maze])
    session.commit()