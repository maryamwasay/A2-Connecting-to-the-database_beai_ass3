from flask import Flask

from database.database import initialize_database
from routes.task_routes import task_routes


def create_app():
    """
    Application factory.
    Creates and configures the Flask application.
    """

    app = Flask(__name__)

    # Initialize the SQLite database
    initialize_database()

    # Register API routes
    app.register_blueprint(task_routes)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)