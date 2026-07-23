import sqlite3

# Connect to the database
connection = sqlite3.connect("tasks.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

# ============================================================
# CREATE (INSERT)
# ============================================================

print("\n========== CREATE ==========\n")

cursor.execute("""
INSERT INTO tasks (title, done)
VALUES (?, ?)
""", ("Learning JavaScript", False))

connection.commit()

print("New task inserted successfully!\n")

# ============================================================
# READ ALL
# ============================================================

print("========== READ ALL ==========\n")

cursor.execute("""
SELECT * FROM tasks
""")

rows = cursor.fetchall()

for row in rows:
    print(dict(row))

# ============================================================
# READ ONE
# ============================================================

print("\n========== READ ONE ==========\n")

cursor.execute("""
SELECT *
FROM tasks
WHERE id = ?
""", (1,))

row = cursor.fetchone()

if row:
    print(dict(row))
else:
    print("Task not found.")

# ============================================================
# UPDATE
# ============================================================

print("\n========== UPDATE ==========\n")

cursor.execute("""
UPDATE tasks
SET title = ?, done = ?
WHERE id = ?
""", ("Learning Python", True, 1))

connection.commit()

print("Task updated successfully!")

cursor.execute("""
SELECT *
FROM tasks
WHERE id = ?
""", (1,))

print(dict(cursor.fetchone()))

# ============================================================
# DELETE
# ============================================================

print("\n========== DELETE ==========\n")

cursor.execute("""
DELETE FROM tasks
WHERE id = ?
""", (2,))

connection.commit()

print("Task with ID 2 deleted.")

# ============================================================
# SEARCH USING LIKE
# ============================================================

print("\n========== SEARCH ==========\n")

cursor.execute("""
SELECT *
FROM tasks
WHERE title LIKE ?
""", ("%Python%",))

rows = cursor.fetchall()

for row in rows:
    print(dict(row))

# ============================================================
# FILTER COMPLETED TASKS
# ============================================================

print("\n========== COMPLETED TASKS ==========\n")

cursor.execute("""
SELECT *
FROM tasks
WHERE done = 1
""")

rows = cursor.fetchall()

for row in rows:
    print(dict(row))

# ============================================================
# SORT ALPHABETICALLY
# ============================================================

print("\n========== SORTED TASKS ==========\n")

cursor.execute("""
SELECT *
FROM tasks
ORDER BY title ASC
""")

rows = cursor.fetchall()

for row in rows:
    print(dict(row))

# ============================================================
# COUNT TASKS
# ============================================================

print("\n========== TASK COUNT ==========\n")

cursor.execute("""
SELECT COUNT(*) AS total
FROM tasks
""")

count = cursor.fetchone()["total"]

print("Total Tasks:", count)

# ============================================================
# CLOSE CONNECTION
# ============================================================

connection.close()

print("\nDatabase connection closed.")