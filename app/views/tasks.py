import json

from flask_restful import Resource
from flask import request

from app.controllers.tasks import get_tasks_json, handle_post_task


class Tasks(Resource):
    def get(self):
        return get_tasks_json()

    def post(self):
        task_data = json.dumps(request.get_json())
        result = handle_post_task(task_data)
        return result
