from stat_tracker.db import Session
from stat_tracker.seed import seed
from stat_tracker.player import Player
from stat_tracker.match import Match
from stat_tracker.rank import Rank
from sqlalchemy import or_
from datetime import datetime


def list_players(session):
    players = session.query(Player).all()
    if not players:
        print("No players found.")
        return
    print("\nPlayers:")
    for p in players:
        print(f"ID: {p.id} | Username: {p.username} | Email: {p.email}")
    print()


def list_matches(session):
    matches = session.query(Match).all()
    if not matches:
        print("No matches found.")
        return
    print("\nMatches:")
    for m in matches:
        print(f"ID: {m.id} | Player ID: {m.player_id} | Mode: {m.game_mode} | "
              f"Kills: {m.kills} | Deaths: {m.deaths} | Score: {m.score} | Date: {m.date_played}")
    print()


def list_ranks(session):
    ranks = session.query(Rank).all()
    if not ranks:
        print("No ranks found.")
        return
    print("\nRanks:")
    for r in ranks:
        print(f"ID: {r.id} | Player ID: {r.player_id} | Rank: {r.rank_name} | Points: {r.rank_points}")
    print()


def add_player(session):
    username = input("Enter new player's username: ").strip()
    email = input("Enter new player's email: ").strip()

    existing = session.query(Player).filter(
        or_(Player.email == email, Player.username == username)
    ).first()

    if existing:
        print("Player with that username or email already exists.")
        return

    new_player = Player(username=username, email=email)
    session.add(new_player)
    session.commit()
    print(f"Added player {username} with email {email}.\n")


def remove_player(session):
    list_players(session)
    try:
        player_id = int(input("Enter the ID of the player to remove: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    player = session.query(Player).filter(Player.id == player_id).first()
    if not player:
        print("Player not found.")
        return
    confirm = input(f"Are you sure you want to delete player '{player.username}'? (y/N): ").strip().lower()
    if confirm == 'y':
        session.delete(player)
        session.commit()
        print("Player removed.\n")
    else:
        print("Cancelled.\n")


def select_player(session):
    list_players(session)
    try:
        player_id = int(input("Enter player ID: ").strip())
    except ValueError:
        print("Invalid ID.")
        return None
    player = session.query(Player).filter_by(id=player_id).first()
    if not player:
        print("Player not found.")
        return None
    return player


def select_rank(session):
    list_ranks(session)
    try:
        rank_id = int(input("Enter rank ID: ").strip())
    except ValueError:
        print("Invalid ID.")
        return None
    rank = session.query(Rank).filter_by(id=rank_id).first()
    if not rank:
        print("Rank not found.")
        return None
    return rank


def select_match(session):
    list_matches(session)
    try:
        match_id = int(input("Enter match ID: ").strip())
    except ValueError:
        print("Invalid ID.")
        return None
    match = session.query(Match).filter_by(id=match_id).first()
    if not match:
        print("Match not found.")
        return None
    return match


def manage_ranks(session):
    while True:
        print("\nManage Ranks")
        print("1. List Ranks")
        print("2. Add or Update Rank")
        print("3. Delete Rank")
        print("0. Back")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            list_ranks(session)

        elif choice == "2":
            player = select_player(session)
            if not player:
                continue
            rank_name = input("Enter rank name (e.g. Gold, Platinum): ").strip()
            try:
                rank_points = int(input("Enter rank points: ").strip())
            except ValueError:
                print("Rank points must be a number.")
                continue
            existing_rank = session.query(Rank).filter_by(player_id=player.id).first()
            if existing_rank:
                existing_rank.rank_name = rank_name
                existing_rank.rank_points = rank_points
                print(f"Updated rank for {player.username}.")
            else:
                new_rank = Rank(player_id=player.id, rank_name=rank_name, rank_points=rank_points)
                session.add(new_rank)
                print(f"Added new rank for {player.username}.")
            session.commit()

        elif choice == "3":
            rank = select_rank(session)
            if not rank:
                continue
            confirm = input(f"Delete rank '{rank.rank_name}' for player ID {rank.player_id}? (y/N): ").strip().lower()
            if confirm == "y":
                session.delete(rank)
                session.commit()
                print("Rank deleted.")
            else:
                print("Cancelled.")

        elif choice == "0":
            break

        else:
            print("Invalid option.")


def manage_matches(session):
    while True:
        print("\nManage Matches")
        print("1. List Matches")
        print("2. Add Match")
        print("3. Update Match")
        print("4. Delete Match")
        print("0. Back")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            list_matches(session)

        elif choice == "2":
            player = select_player(session)
            if not player:
                continue
            game_mode = input("Enter game mode (e.g. Ranked, Casual): ").strip()
            try:
                kills = int(input("Enter kills: ").strip())
                deaths = int(input("Enter deaths: ").strip())
                score = int(input("Enter score: ").strip())
            except ValueError:
                print("Kills, deaths, and score must be numbers.")
                continue
            date_str = input("Enter date played (YYYY-MM-DD) or leave empty for today: ").strip()
            if date_str:
                try:
                    date_played = datetime.strptime(date_str, "%Y-%m-%d").date()
                except ValueError:
                    print("Invalid date format.")
                    continue
            else:
                date_played = datetime.today().date()
            new_match = Match(
                player_id=player.id,
                game_mode=game_mode,
                kills=kills,
                deaths=deaths,
                score=score,
                date_played=date_played
            )
            session.add(new_match)
            session.commit()
            print(f"Added match for player {player.username}.")

        elif choice == "3":
            match = select_match(session)
            if not match:
                continue

            game_mode = input(f"Enter new game mode (current: {match.game_mode}): ").strip()
            if game_mode:
                match.game_mode = game_mode

            try:
                kills_input = input(f"Enter kills (current: {match.kills}): ").strip()
                if kills_input:
                    match.kills = int(kills_input)
                deaths_input = input(f"Enter deaths (current: {match.deaths}): ").strip()
                if deaths_input:
                    match.deaths = int(deaths_input)
                score_input = input(f"Enter score (current: {match.score}): ").strip()
                if score_input:
                    match.score = int(score_input)
            except ValueError:
                print("Kills, deaths, and score must be numbers.")
                continue

            date_str = input(f"Enter new date played (YYYY-MM-DD) (current: {match.date_played}): ").strip()
            if date_str:
                try:
                    match.date_played = datetime.strptime(date_str, "%Y-%m-%d").date()
                except ValueError:
                    print("Invalid date format.")
                    continue

            session.commit()
            print("Match updated.")

        elif choice == "4":
            match = select_match(session)
            if not match:
                continue
            confirm = input(f"Delete match ID {match.id}? (y/N): ").strip().lower()
            if confirm == "y":
                session.delete(match)
                session.commit()
                print("Match deleted.")
            else:
                print("Cancelled.")

        elif choice == "0":
            break

        else:
            print("Invalid option.")


def main():
    session = Session()

    while True:
        print("\n🎮 Apex Stat Tracker 🎮")
        print("1. Seed Database")
        print("2. List Players")
        print("3. Manage Matches")
        print("4. Manage Ranks")
        print("5. Add Player")
        print("6. Remove Player")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                seed()
                print("Database seeded successfully.")
            except Exception as e:
                print(f"Error seeding database: {e}")

        elif choice == "2":
            list_players(session)

        elif choice == "3":
            manage_matches(session)

        elif choice == "4":
            manage_ranks(session)

        elif choice == "5":
            add_player(session)

        elif choice == "6":
            remove_player(session)

        elif choice == "0":
            print("Goodbye! Keep The Grind💪")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
