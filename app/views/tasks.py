import json

from flask_restful import Resource, abort
from flask import request

from app.controllers.tasks import get_tasks_json, handle_post_task, task_schema
from app.models.tasks import Task

def abort_if_task_not_exists(task_id):
    task = Task.query.filter_by(id=task_id).first()
    if not task:
        return abort(404, message="Task with id {} does not exist.".format(task_id))
    return task

class Tasks(Resource):
    def get(self):
        return get_tasks_json()

    def post(self):
        task_data = json.dumps(request.get_json())
        result = handle_post_task(task_data)
        return result


class Task_Details(Resource):
    def get(self, task_id):
        task = abort_if_task_not_exists(task_id)
        return task_schema.dump(task)
