import sqlite3
import os

# Database file path
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tasks.db")


def get_connection():
    """
    Create and return a SQLite connection.
    Rows are returned as dictionaries.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    """
    Create the tasks table if it doesn't exist
    and insert sample data only on the first run.
    """

    conn = get_connection()
    cursor = conn.cursor()

    # Create tasks table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT 0
        )
    """)

    # Check whether table already contains data
    cursor.execute("SELECT COUNT(*) FROM tasks")
    count = cursor.fetchone()[0]

    # Insert sample tasks only if table is empty
    if count == 0:
        sample_tasks = [
            ("Learn Python", 0),
            ("Build CRUD API", 0),
            ("Practice SQLite", 1)
        ]

        cursor.executemany(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            sample_tasks
        )

    conn.commit()
    conn.close()
