from lib.models import Base, SessionLocal, engine
from lib.helper import create_initial_maze

def seed_database():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    create_initial_maze(session)
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()