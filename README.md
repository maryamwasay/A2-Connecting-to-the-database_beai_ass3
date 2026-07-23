# A2-Connecting-to-the-database_beai_ass3
# SQLite CRUD API

A simple RESTful CRUD API built with **Python**, **Flask**, and **SQLite**. This project demonstrates how to replace an in-memory data store with a persistent SQLite database while keeping the API unchanged.

---

# Project Objective

The objective of this project is to demonstrate the separation between the API layer and the data layer.

The API endpoints remain exactly the same, but instead of storing tasks in memory, they are now stored in a SQLite database. This allows the data to persist even after the server is restarted.

---

# Technologies Used

- Python 3
- Flask
- SQLite
- sqlite3 (Python Standard Library)

---

# Project Structure

```
sqlite-crud-api/
│
├── database/
│   ├── __init__.py
│   └── database.py
│
├── models/
│   ├── __init__.py
│   └── task.py
│
├── repositories/
│   ├── __init__.py
│   └── task_repository.py
│
├── routes/
│   ├── __init__.py
│   └── task_routes.py
│
├── services/
│   ├── __init__.py
│   └── task_service.py
│
├── images/
│   └── database_viewer.png
│
├── main.py
├── tasks.db
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Why SQLite?

SQLite was chosen because:

- It requires no separate database server.
- It stores all data in a single database file.
- It is lightweight and easy to use.
- It is included with Python through the sqlite3 library.
- It is ideal for small backend applications and learning SQL.

---

# Database Location

The SQLite database is stored in the project root as:

```
tasks.db
```

The application automatically:

- Creates the database if it does not exist.
- Creates the `tasks` table if it does not exist.
- Inserts three sample tasks only when the table is empty.

---

# Features

- Create Tasks
- Read All Tasks
- Read Task by ID
- Update Tasks
- Delete Tasks
- SQLite Database Persistence
- Automatic Database Initialization
- SQL-Based CRUD Operations

---

# API Endpoints

## Get All Tasks

```
GET /tasks
```

Returns all tasks stored in the database.

---

## Get Task by ID

```
GET /tasks/<id>
```

Example:

```
GET /tasks/1
```

Returns a single task.

If the task does not exist:

```
404
{
    "error": "Task not found"
}
```

---

## Create Task

```
POST /tasks
```

Example Request

```json
{
    "title": "Learn SQLite"
}
```

Successful Response

```
201 Created
```

---

## Update Task

```
PUT /tasks/<id>
```

Example

```json
{
    "title": "Practice SQL",
    "done": true
}
```

---

## Delete Task

```
DELETE /tasks/<id>
```

Deletes the specified task.

---

# SQL Queries Used

Example SQL query executed:

```sql
SELECT * FROM tasks;
```

Other SQL queries used in the project include:

```sql
INSERT INTO tasks (title, done)
VALUES (?, ?);
```

```sql
SELECT * FROM tasks;
```

```sql
SELECT * FROM tasks
WHERE id = ?;
```

```sql
UPDATE tasks
SET title = ?, done = ?
WHERE id = ?;
```

```sql
DELETE FROM tasks
WHERE id = ?;
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/sqlite-crud-api.git
```

Move into the project folder:

```bash
cd sqlite-crud-api
```

(Optional) Create a virtual environment:

Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Start the Flask application:

```bash
python main.py
```

The server starts at:

```
http://127.0.0.1:5000
```

When the application starts for the first time, it automatically:

- Creates `tasks.db`
- Creates the `tasks` table
- Inserts three example tasks if the table is empty

---

# Testing

The API was tested using:

- Postman
- SQLite Viewer (VS Code Extension)

The following operations were successfully tested:

- GET
- POST
- PUT
- DELETE

Manual SQL queries were also executed using the SQLite Viewer.

---

# Database Screenshot

Add your SQLite Viewer screenshot below.

```
images/database_viewer.png
```

Example Markdown:

```markdown
![Database Screenshot](images/database_viewer.png)
```

---

# Requirements Satisfied

- SQLite database replaces in-memory storage.
- Data persists after server restarts.
- Database automatically created.
- Table automatically created.
- Three sample tasks inserted only once.
- CRUD operations implemented using SQL queries.
- Unknown IDs return 404.
- Invalid requests return 400.
- Public GitHub repository created.
- README documentation included.

---

# Author

**maryam Wasay**

Backend Development Assignment – SQLite CRUD API
