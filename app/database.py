import sqlite3
from pathlib import Path


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SQLite database file
DATABASE_PATH = BASE_DIR / "tasks.db"


def get_connection():
    """
    Create and return a connection to the SQLite database.
    """
    connection = sqlite3.connect(DATABASE_PATH)

    # Allows rows to behave like dictionaries
    connection.row_factory = sqlite3.Row

    return connection


def init_db():
    """
    Create the tasks table if it does not exist.
    Seed three example tasks only when the table is empty.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        # Create table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                done INTEGER NOT NULL DEFAULT 0
            )
            """
        )

        # Check whether the table already contains tasks
        cursor.execute("SELECT COUNT(*) AS count FROM tasks")
        count = cursor.fetchone()["count"]

        # Seed only when the table is empty
        if count == 0:
            seed_tasks = [
                ("Learn FastAPI", 0),
                ("Learn SQLite", 0),
                ("Build database-backed CRUD API", 0),
            ]

            cursor.executemany(
                """
                INSERT INTO tasks (title, done)
                VALUES (?, ?)
                """,
                seed_tasks,
            )

        connection.commit()

    finally:
        connection.close()


def row_to_dict(row):
    """
    Convert a SQLite row into a normal Python dictionary.
    """
    if row is None:
        return None

    return {
        "id": row["id"],
        "title": row["title"],
        "done": bool(row["done"]),
    }