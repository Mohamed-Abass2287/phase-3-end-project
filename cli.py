from lib.models import SessionLocal
from lib.models.player import Player
from lib.models.maze import Room

def main():
    session = SessionLocal()
    current_room = 1
    
    print("Welcome to Maze Quest!")
    player_name = input("Enter your name: ")
    
    player = Player(name=player_name)
    session.add(player)
    session.commit()
    
    while True:
        room = session.query(Room).filter_by(id=current_room).first()
        print(f"\n{room.description}")
        print("Exits:", ", ".join(room.exits.keys()))
        
        command = input("> ").lower().strip()
        
        if command in room.exits:
            current_room = room.exits[command]
        elif command == "quit":
            break
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()