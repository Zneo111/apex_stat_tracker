from stat_tracker.db import Session
from stat_tracker.player import Player
from stat_tracker.match import Match
from stat_tracker.rank import Rank
from datetime import datetime

def add_player_cli():
    username = input("Enter username: ")
    email = input("Enter email: ")

    session = Session()
    existing_player = session.query(Player).filter_by(email=email).first()
    if existing_player:
        print(f"Player with email {email} already exists.")
        session.close()
        return

    player = Player(username=username, email=email)
    session.add(player)
    session.flush()

    rank_name = input("Enter rank name: ")
    rank_points = int(input("Enter rank points: "))
    rank = Rank(player_id=player.id, rank_name=rank_name, rank_points=rank_points)
    session.add(rank)

    print("\nAdd first match:")
    game_mode = input("Game mode: ")
    kills = int(input("Kills: "))
    deaths = int(input("Deaths: "))
    score = int(input("Score: "))

    date_played = datetime.now().replace(microsecond=0)
    match = Match(player_id=player.id, game_mode=game_mode, kills=kills, deaths=deaths, score=score, date_played=date_played)
    session.add(match)

    session.commit()
    print("✅ Player, rank, and match added.")
    session.close()

if __name__ == "__main__":
    add_player_cli()

