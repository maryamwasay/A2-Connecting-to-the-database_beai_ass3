from database.database import get_connection
from models.task import Task


class TaskRepository:
    """
    Handles all database operations for tasks.
    """

    @staticmethod
    def get_all_tasks():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks")

        rows = cursor.fetchall()

        conn.close()

        return [Task.from_row(row) for row in rows]

    @staticmethod
    def get_task_by_id(task_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM tasks WHERE id = ?",
            (task_id,)
        )

        row = cursor.fetchone()

        conn.close()

        if row:
            return Task.from_row(row)

        return None

    @staticmethod
    def create_task(title):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            (title, False)
        )

        conn.commit()

        task_id = cursor.lastrowid

        conn.close()

        return Task(task_id, title, False)

    @staticmethod
    def update_task(task_id, title, done):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE tasks
            SET title = ?, done = ?
            WHERE id = ?
            """,
            (title, done, task_id)
        )

        conn.commit()

        affected_rows = cursor.rowcount

        conn.close()

        if affected_rows == 0:
            return None

        return Task(task_id, title, done)

    @staticmethod
    def delete_task(task_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

        conn.commit()

        affected_rows = cursor.rowcount

        conn.close()

        return affected_rows > 0
