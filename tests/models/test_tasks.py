from app.models.tasks import Task
from app import create_app, db

def setup_module(module):
    print("Creating the APP")
    app = create_app('testing')
    app.app_context().push()

def setup_function(function):
    print("Setup Function")
    db.create_all()

def teardown_function(function):
    print("Teardown Function")
    db.session.rollback()
    db.drop_all()

def test_create_task():
    task = Task("Task Description", "IT")
    task.create()

    all_tasks = Task.query.all()

    assert len(all_tasks) == 1
    first_task = all_tasks[0]
    assert first_task.description == "Task Description"
    assert first_task.department == "IT"


def test_update_task():
    task = Task("Task Description for Update", "People")
    task.create()

    task_to_update = Task.query.filter_by(id=1).first()

    task_to_update.description = "Task Changed"
    task_to_update.department = "New Department"
    task_to_update.update()

    updated_task = Task.query.filter_by(id=1).first()
    assert updated_task.description == "Task Changed"
    assert updated_task.department == "New Department"


def test_delete_task():
    task = Task("Task Description for Update", "People")
    task.create()

    task_to_delete = Task.query.filter_by(id=1).first()

    task_to_delete.delete()
    deleted_task = Task.query.filter_by(id=1).first()

    assert deleted_task is None

