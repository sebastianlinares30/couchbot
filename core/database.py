import sqlite3
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
database_path = base_dir / 'database' / 'bot_user.db'

def get_connection():
    return sqlite3.connect(database_path)