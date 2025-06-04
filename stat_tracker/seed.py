from stat_tracker.db import Session
from stat_tracker.player import Player
from stat_tracker.match import Match
from stat_tracker.rank import Rank

def seed():
    session = Session()


    if not session.query(Player).filter_by(email="wraith@example.com").first():
        player1 = Player(username="WraithMain", email="wraith@example.com")
        session.add(player1)

    if not session.query(Player).filter_by(email="octane@example.com").first():
        player2 = Player(username="OctaneBoost", email="octane@example.com")
        session.add(player2)

    session.commit()

   
    session.close()
    print("🌱 Database seeded successfully.")
