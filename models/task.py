class Task:
    """
    Represents a Task object.
    """

    def __init__(self, id, title, done):
        self.id = id
        self.title = title
        self.done = bool(done)

    def to_dict(self):
        """
        Convert the Task object into a dictionary
        so it can be returned as JSON.
        """
        return {
            "id": self.id,
            "title": self.title,
            "done": self.done
        }

    @classmethod
    def from_row(cls, row):
        """
        Create a Task object from a SQLite row.
        """
        return cls(
            id=row["id"],
            title=row["title"],
            done=row["done"]
        )
