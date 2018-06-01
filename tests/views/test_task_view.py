import pytest

from app import create_app


app = create_app('testing')
app.app_context().push()


mock_tasks_data = [
    {
        "duration_in_days": 3,
        "id": 1,
        "date_created": "2018-06-01T14:31:05.168657+00:00",
        "department": "IT",
        "date_modified": "2018-06-01T14:31:05.168657+00:00",
        "description": "Get Laptop"
    },
    {
        "duration_in_days": 1,
        "id": 2,
        "date_created": "2018-06-01T14:39:15.005623+00:00",
        "department": "Facilities",
        "date_modified": "2018-06-01T14:39:15.005623+00:00",
        "description": "Get Office Space"
    },
    {
        "description": "Get Email",
        "department": "IT",
        "duration_in_days": 4,
        "id": 3,
        "date_created": "2018-06-01T14:29:35.987768+00:00",
        "date_modified": "2018-06-01T14:29:35.987768+00:00"
    }]
mock_task_data = {
        "description": "Get Email",
        "department": "IT",
        "duration_in_days": 4,
        "id": 4,
        "date_created": "2018-06-01T14:29:35.987768+00:00",
        "date_modified": "2018-06-01T14:29:35.987768+00:00"
    }

@pytest.fixture
def client():
    client = app.test_client()
    return client




def test_get_all_tasks(client, mocker):
    mock_controller = mocker.patch("app.views.tasks.get_tasks_json")
    mock_controller.return_value = mock_tasks_data
    results = client.get('/api/tasks')

    data = results.get_json()
    task_1, task_2, task_3 = data

    assert len(data) == 3
    assert results.status_code == 200

    assert task_1.get("description") == "Get Laptop"
    assert task_1.get("department") == "IT"
    assert task_1.get("id") == 1
    assert task_1.get("duration_in_days") == 3
    assert task_2.get("description") == "Get Office Space"
    assert task_2.get("department") == "Facilities"
    assert task_2.get("id") == 2
    assert task_2.get("duration_in_days") == 1
    assert task_3.get("description") == "Get Email"
    assert task_3.get("department") == "IT"
    assert task_3.get("id") == 3
    assert task_3.get("duration_in_days") == 4

def test_create_new_task(client, mocker):
    new_task = {
        "description": "Get Laptop",
        "department": "IT"
    }
    mock_request = mocker.patch("app.views.tasks.request")
    mock_request.get_json.return_value = new_task
    mock_controller = mocker.patch("app.views.tasks.handle_post_task")
    mock_controller.return_value = mock_task_data, 201

    result = client.post('/api/tasks', data=new_task)
    task_data = result.get_json()

    assert task_data.get("id") == 4
    assert task_data.get("description") == "Get Email"
    assert task_data.get("department") == "IT"
    assert result.status_code == 201

def test_delete_task():
    pass

def test_update_task():
    pass