# FlyRank CRUD API - Week 3 Assignment A2

## Overview

This project is the Week 3 Assignment A2 for the FlyRank
Backend Track.

The project takes the CRUD API from Assignment A1 and replaces
the in-memory task storage with a SQLite database.

The API endpoints remain the same while the storage layer is
changed from memory to persistent SQLite storage.

## Technologies

- Python
- FastAPI
- SQLite
- sqlite3
- Pydantic
- Pytest

## Project Structure

```text
flyrank-crud-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── routes.py
│
├── tests/
│   └── test_tasks.py
│
├── ai-version/
│   └── README.md
│
├── .gitignore
├── README.md
└── requirements.txt# AI Version

This folder contains the AI-generated version for the optional
Stage 6 - AI Rematch.

The manually implemented SQLite version in the main `app/`
directory is the primary submission.

The AI version will be generated separately, tested, compared,
and documented in the main README.
