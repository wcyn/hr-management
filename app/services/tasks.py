from app.models.tasks import Task

def get_tasks_from_database():
    return Task.query.all()

def create_new_task(task_data):
    task = Task(description=task_data.get("description"),
                department=task_data.get("department"))
    other_fields = ['duration_in_days']
    for field in other_fields:
        if field in task_data:
            setattr(task, field, task_data.get(field))
    task.create()
    return task

def get_task_details_from_db(task_id):
    task = Task.query.filter_by(id=task_id).first()
    return task

def update_task_data_in_db(task, task_data):
    for key, value in task_data.items():
        setattr(task, key, value)
    task.update()
    return task