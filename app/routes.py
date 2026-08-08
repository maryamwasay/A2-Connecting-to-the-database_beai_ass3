from fastapi import APIRouter, HTTPException, status

from .database import get_connection, row_to_dict
from .models import TaskCreate, TaskUpdate


router = APIRouter()


@router.get("/tasks")
def get_tasks():
    """
    Return all tasks from SQLite.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id, title, done
            FROM tasks
            ORDER BY id
            """
        )

        rows = cursor.fetchall()

        return [row_to_dict(row) for row in rows]

    finally:
        connection.close()


@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    """
    Return one task by ID.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id, title, done
            FROM tasks
            WHERE id = ?
            """,
            (task_id,),
        )

        row = cursor.fetchone()

        if row is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": "Task not found"},
            )

        return row_to_dict(row)

    finally:
        connection.close()


@router.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    """
    Create a new task.
    """

    title = task.title.strip()

    if not title:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": "Title cannot be empty"},
        )

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO tasks (title, done)
            VALUES (?, ?)
            """,
            (title, 0),
        )

        connection.commit()

        new_task_id = cursor.lastrowid

        cursor.execute(
            """
            SELECT id, title, done
            FROM tasks
            WHERE id = ?
            """,
            (new_task_id,),
        )

        row = cursor.fetchone()

        return row_to_dict(row)

    finally:
        connection.close()


@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    """
    Update an existing task.
    """

    title = task.title.strip()

    if not title:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": "Title cannot be empty"},
        )

    connection = get_connection()

    try:
        cursor = connection.cursor()

        # First check whether the task exists
        cursor.execute(
            """
            SELECT id
            FROM tasks
            WHERE id = ?
            """,
            (task_id,),
        )

        existing_task = cursor.fetchone()

        if existing_task is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": "Task not found"},
            )

        # Update task
        cursor.execute(
            """
            UPDATE tasks
            SET title = ?, done = ?
            WHERE id = ?
            """,
            (title, int(task.done), task_id),
        )

        connection.commit()

        # Return updated task
        cursor.execute(
            """
            SELECT id, title, done
            FROM tasks
            WHERE id = ?
            """,
            (task_id,),
        )

        row = cursor.fetchone()

        return row_to_dict(row)

    finally:
        connection.close()


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    """
    Delete a task by ID.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        # Check whether task exists
        cursor.execute(
            """
            SELECT id
            FROM tasks
            WHERE id = ?
            """,
            (task_id,),
        )

        existing_task = cursor.fetchone()

        if existing_task is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": "Task not found"},
            )

        cursor.execute(
            """
            DELETE FROM tasks
            WHERE id = ?
            """,
            (task_id,),
        )

        connection.commit()

        # 204 means no response body
        return None

    finally:
        connection.close()