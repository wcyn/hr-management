from marshmallow import Schema, fields

from app.models.tasks import Task
from app.controllers import format_error_message

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
    tasks = Task.query.all()
    return tasks_schema.dump(tasks)

def handle_post_task(task_data):
    task_data, errors = task_schema.loads(task_data)
    if errors:
        return format_error_message(errors)

    task = Task(description=task_data.get("description"),
                department=task_data.get("department"))
    task.create()
    return task_schema.dump(task), 201
