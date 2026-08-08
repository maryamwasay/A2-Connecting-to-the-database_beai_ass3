from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Test task"
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert "id" in data
    assert data["title"] == "Test task"
    assert data["done"] is False


def test_get_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Task to retrieve"
        },
    )

    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id


def test_get_unknown_task():
    response = client.get("/tasks/999999")

    assert response.status_code == 404


def test_update_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Old title"
        },
    )

    task_id = create_response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "New title",
            "done": True
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == task_id
    assert data["title"] == "New title"
    assert data["done"] is True


def test_delete_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Task to delete"
        },
    )

    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 204

    get_response = client.get(f"/tasks/{task_id}")

    assert get_response.status_code == 404
