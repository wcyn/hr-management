import pytest

from app import create_app, db
from app.models.tasks import Task


app = create_app('testing')
app.app_context().push()

def setup_module(module):
    pass

def setup_function(function):
    db.create_all()
    tasks = [Task('Get Laptop', 'IT'),
             Task('Get Office Space', 'Facilities'),
             Task('Get Email', 'IT')]
    for task in tasks:
        task.create()


def teardown_function(function):
    db.session.rollback()
    db.drop_all()

@pytest.fixture
def client():
    client = app.test_client()
    return client



def test_get_all_tasks(client):
    results = client.get('/api/tasks')

    data = results.get_json()
    task_1, task_2, task_3 = data

    assert len(data) == 3
    assert results.status_code == 200

    assert task_1.get("description") == "Get Laptop"
    assert task_1.get("department") == "IT"
    assert task_2.get("description") == "Get Office Space"
    assert task_2.get("department") == "Facilities"
    assert task_3.get("description") == "Get Email"
    assert task_3.get("department") == "IT"

def test_create_new_task(client):
    new_task = {
        "description": "Allocate Space",
        "department": "Facilities"
    }
    result = client.post('/api/tasks', data=new_task)
    task_data = result.get_json()

    assert result.status_code == 201
    assert task_data.get("id") == 4
    assert task_data.get("description") == "Allocate Space"
    assert task_data.get("department") == "Facilities"




def test_delete_task():
    pass

def test_update_task():
    pass