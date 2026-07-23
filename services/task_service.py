from repositories.task_repository import TaskRepository


class TaskService:
    """
    Handles business logic for tasks.
    """

    @staticmethod
    def get_all_tasks():
        return TaskRepository.get_all_tasks()

    @staticmethod
    def get_task_by_id(task_id):
        return TaskRepository.get_task_by_id(task_id)

    @staticmethod
    def create_task(data):
        """
        Create a new task after validation.
        """

        title = data.get("title")

        if not title or not title.strip():
            return None, "Title is required."

        task = TaskRepository.create_task(title.strip())

        return task, None

    @staticmethod
    def update_task(task_id, data):
        """
        Update an existing task.
        """

        existing_task = TaskRepository.get_task_by_id(task_id)

        if existing_task is None:
            return None, "Task not found."

        title = data.get("title", existing_task.title)
        done = data.get("done", existing_task.done)

        if not title or not str(title).strip():
            return None, "Title is required."

        updated_task = TaskRepository.update_task(
            task_id,
            str(title).strip(),
            bool(done)
        )

        return updated_task, None

    @staticmethod
    def delete_task(task_id):
        """
        Delete a task.
        """

        existing_task = TaskRepository.get_task_by_id(task_id)

        if existing_task is None:
            return False

        return TaskRepository.delete_task(task_id)
