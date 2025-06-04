from stat_tracker.db import engine, Base
from stat_tracker.player import Player
from stat_tracker.match import Match
from stat_tracker.rank import Rank

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully.")

if __name__ == "__main__":
    create_tables()
