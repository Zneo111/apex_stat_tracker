# 🎮 Apex Legends Stat Tracker CLI

A comprehensive Command Line Interface (CLI) application for tracking Apex Legends player statistics, built with Python and SQLAlchemy ORM.

## 🎯 Project Requirements Met

1. **CLI Application**
   - Interactive menu-driven interface
   - Real-world problem solution (game statistics tracking)
   - Clean code structure with best practices

2. **SQLAlchemy ORM Database**
   - 3 Related Tables:
     - Players (core entity)
     - Matches (tracks game performance)
     - Ranks (tracks player rankings)
   - Proper relationships and cascading

3. **Virtual Environment**
   - Managed with Pipenv
   - Dependencies isolated and tracked

4. **Package Structure**
   ```
   apex_stat_tracker/
   ├── stat_tracker/           # Main package
   │   ├── __init__.py
   │   ├── cli.py             # CLI functions
   │   ├── db.py              # Database configuration
   │   ├── models/            # SQLAlchemy models
   │   │   ├── player.py
   │   │   ├── match.py
   │   │   └── rank.py
   │   └── seed.py            # Database seeding
   └── run.py                 # Application entry point
   ```

5. **Data Structures Used**
   - Lists: For query results and display
   - Dictionaries: For data mapping
   - SQLAlchemy ORM models

## 🚀 Features

- Player Management
  - Add new players
  - List all players
  - Remove players
  - Track player statistics

- Match Tracking
  - Record match results
  - Update match details
  - View match history
  - Delete match records

- Rank System
  - Assign player ranks
  - Track rank progression
  - Update rank points

## ⚙️ Installation

1. **Clone Repository**
   ```bash
   git clone <repository-url>
   cd apex_stat_tracker
   ```

2. **Set Up Virtual Environment**
   ```bash
   # Install pipenv if not already installed
   pip install pipenv

   # Install dependencies
   pipenv install

   # Activate virtual environment
   pipenv shell
   ```

3. **Configure Environment**
   ```bash
   cp .env.example .env
   ```

4. **Initialize Database**
   ```bash
   python stat_tracker/create_tables.py
   ```

## 🎮 Usage

1. **Start Application**
   ```bash
   python run.py
   ```

2. **Main Menu Options**
   - Seed Database (1)
   - List Players (2)
   - Manage Matches (3)
   - Manage Ranks (4)
   - Add Player (5)
   - Remove Player (6)
   - Exit (0)

## 🛠️ Technical Details

### Dependencies
- SQLAlchemy
- python-dotenv
- Other dependencies in Pipfile

### Database Schema
```sql
Players
  - id (PK)
  - username
  - email

Matches
  - id (PK)
  - player_id (FK)
  - game_mode
  - kills
  - deaths
  - score
  - date_played

Ranks
  - id (PK)
  - player_id (FK)
  - rank_name
  - rank_points
```

## 🔧 Troubleshooting

- **Import Errors**: Ensure virtual environment is activated
- **Database Issues**: Delete `apex_stats.db` and recreate tables
- **Module Errors**: Check project structure and imports

## 👥 Contributing

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Submit pull request

## 📝 License

MIT License
