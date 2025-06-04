# Apex Stat Tracker

Apex Stat Tracker is a Python CLI application for managing and tracking Apex Legends player statistics. It uses SQLAlchemy ORM and a SQLite database for persistent storage.

---

## Features

- Add, list, and remove **Players**
- Record and manage **Matches**
- Assign and update **Ranks** for players
- Seed the database with sample data
- Modular, clean codebase

---

## Project Structure

```
apex_stat_tracker/
├── stat_tracker/
│   ├── __init__.py
│   ├── cli.py
│   ├── create_tables.py
│   ├── db.py
│   ├── match.py
│   ├── player.py
│   ├── rank.py
│   └── seed.py
├── .env
├── .env.example
├── .gitignore
├── README.md
└── run.py
```

---

## Getting Started

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd apex_stat_tracker
```

### 2. Install Dependencies

It is recommended to use [pipenv](https://pipenv.pypa.io/en/latest/) for dependency management:

```sh
pipenv install
```

Or, if you use pip:

```sh
pip install sqlalchemy python-dotenv
```

### 3. Set Up Environment Variables

Copy the example environment file and edit if needed:

```sh
cp .env.example .env
```

Ensure your `.env` contains:

```
DATABASE_URL=sqlite:///apex_stats.db
```

### 4. Create Database Tables

```sh
pipenv shell
python stat_tracker/create_tables.py
```

### 5. (Optional) Seed Sample Data

```sh
python -m stat_tracker.seed
```

### 6. Run the Application

```sh
python run.py
```

---

## Usage

Follow the CLI prompts to:

- Add new players
- Record matches
- Assign or update ranks
- View stats and manage data

---

## Troubleshooting

- Ensure all dependencies are installed.
- If you get import errors, check that all files exist in the `stat_tracker/` directory.
- If the database is not created, run `python stat_tracker/create_tables.py`.
- If you get `No module named ...`, ensure you are running commands from the project root and your environment is activated (`pipenv shell`).
- If you change models, re-run `create_tables.py` (may need to delete `apex_stats.db` for a fresh start).

---

## License

MIT License