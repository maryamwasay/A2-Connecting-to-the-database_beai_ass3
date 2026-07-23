from flask import Blueprint, request, jsonify
from services.task_service import TaskService

task_routes = Blueprint("task_routes", __name__)


@task_routes.route("/tasks", methods=["GET"])
def get_all_tasks():
    tasks = TaskService.get_all_tasks()

    return jsonify([task.to_dict() for task in tasks]), 200


@task_routes.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = TaskService.get_task_by_id(task_id)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task.to_dict()), 200


@task_routes.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be JSON"}), 400

    task, error = TaskService.create_task(data)

    if error:
        return jsonify({"error": error}), 400

    return jsonify(task.to_dict()), 201


@task_routes.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be JSON"}), 400

    task, error = TaskService.update_task(task_id, data)

    if error == "Task not found.":
        return jsonify({"error": error}), 404

    if error:
        return jsonify({"error": error}), 400

    return jsonify(task.to_dict()), 200


@task_routes.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    deleted = TaskService.delete_task(task_id)

    if not deleted:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({"message": "Task deleted successfully"}), 200
