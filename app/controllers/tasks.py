from marshmallow import Schema, fields
from flask_restful import abort

from app.controllers import format_error_message
from app.services.tasks import (get_tasks_from_database, create_new_task, get_task_details_from_db,
                                update_task_data_in_db)
from app.models.tasks import Task

def abort_if_task_not_exists(task_id):
    task = get_task_details_from_db(task_id)
    if not task:
        return abort(404, message="Task with id {} does not exist.".format(task_id))
    return task

class TaskSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    description = fields.String(required=True, )
    date_created = fields.DateTime(dump_only=True)
    date_modified = fields.DateTime(dump_only=True)
    duration_in_days = fields.Integer()
    department = fields.String(required=True)

tasks_schema = TaskSchema(many=True)
task_schema = TaskSchema()

def get_tasks_json():
    tasks = get_tasks_from_database()
    return tasks_schema.dump(tasks)

def handle_post_task(task_data):
    task_data, errors = task_schema.loads(task_data)
    if errors:
        return format_error_message(errors)
    task = create_new_task(task_data)

    return task_schema.dump(task), 201

def get_json_task_details(task_id):
    task = abort_if_task_not_exists(task_id)
    task, errors = task_schema.dump(task)
    if errors:
        return format_error_message(errors, message="Unable to fetch the requested task")
    return task

def update_task_details(task_id, task_data):
    task = abort_if_task_not_exists(task_id)
    task_data, error = task_schema.loads(task_data)
    if error:
        return error
    task = update_task_data_in_db(task, task_data)
    return task_schema.dump(task)