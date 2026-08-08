from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database import init_db
from .routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Runs when the application starts.
    Creates the database/table and seeds data if necessary.
    """
    init_db()
    yield


app = FastAPI(
    title="FlyRank CRUD API",
    description="FlyRank Week 3 Assignment A2 - SQLite CRUD API",
    version="2.0.0",
    lifespan=lifespan,
)


app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "FlyRank CRUD API is running",
        "database": "SQLite",
    }
