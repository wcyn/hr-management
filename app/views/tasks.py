from flask_restful import Resource
from flask import request

from app.models.tasks import Task
from app.controllers.tasks import get_tasks_json


class Tasks(Resource):
    def get(self):
        return get_tasks_json()

    def post(self):
        task_data = request.get_json()
        task = Task(description=task_data.get("description"),
                    department=task_data.get("department"))
        task.create()

        task_data = {
            'id': task.id,
            'description': task.description,
            'department': task.department
        }

        return task_data