from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)


class TaskUpdate(BaseModel):
    title: str = Field(..., min_length=1)
    done: bool


class TaskResponse(BaseModel):
    id: int
    title: str
    done: bool


class ErrorResponse(BaseModel):
    error: str