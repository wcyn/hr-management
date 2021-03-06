import json

from flask_restful import Resource
from flask import request

from app.controllers.tasks import (get_tasks_json, handle_post_task, get_json_task_details,
    abort_if_task_not_exists, task_schema, update_task_details)
from app.models.tasks import Task


class Tasks(Resource):
    def get(self):
        return get_tasks_json()

    def post(self):
        task_data = json.dumps(request.get_json())
        result = handle_post_task(task_data)
        return result


class Task_Details(Resource):
    def get(self, task_id):
        result = get_json_task_details(task_id)
        return result

    def put(self, task_id):
        task_data = json.dumps(request.get_json())
        result = update_task_details(task_id, task_data)
        return result
