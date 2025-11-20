import sqlite3
from pathlib import Path

DB_PATH = Path("project.db")  # file database


def get_connection():
    """Membuat koneksi SQLite."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # hasil bisa diakses seperti dictionary
    return conn


def get_db():
    """Alias untuk kompatibilitas."""
    return get_connection()


def init_db():
    conn = get_db()
    c = conn.cursor()

    # Table transaksi
    c.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT
        )
    """)

    # Table kategori
    c.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    """)

    conn.commit()
    conn.close()
