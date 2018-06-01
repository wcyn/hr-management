from app.services.tasks import get_tasks_from_database, create_new_task, get_task_details_from_db

def test_get_tasks_from_database(mocker):
    mock_task_1 = mocker.Mock(description='Task 1', department='IT')
    mock_task_2 = mocker.Mock(description='Task 2', department='Facilities')

    mock_model = mocker.patch("app.services.tasks.Task")
    mock_model.query.all.return_value = [mock_task_1, mock_task_2]

    tasks = get_tasks_from_database()
    mock_model.query.all.assert_called_once_with()
    assert len(tasks) == 2
    task_1, task_2 = tasks
    assert task_1.description == 'Task 1'
    assert task_1.department == 'IT'
    assert task_2.description == 'Task 2'
    assert task_2.department == 'Facilities'


def test_create_new_task(mocker, monkeypatch):
    new_task = {
        'description': 'Task 1',
        'department': 'IT'
    }
    mock_task = mocker.Mock()
    mock_model = mocker.patch("app.services.tasks.Task")
    monkeypatch.setattr(mock_task, 'description', 'Task 1')
    monkeypatch.setattr(mock_task, 'department', 'IT')
    mock_model.return_value = mock_task

    task = create_new_task(new_task)
    mock_model.assert_called_once_with(department='IT', description='Task 1')
    mock_task.create.assert_called_once_with()
    assert task.description == 'Task 1'
    assert task.department == 'IT'

def test_get_task_details_from_db(mocker, monkeypatch):
    mock_task = mocker.Mock()
    mock_model = mocker.patch("app.services.tasks.Task")
    monkeypatch.setattr(mock_task, 'description', 'Task 1')
    monkeypatch.setattr(mock_task, 'department', 'IT')
    monkeypatch.setattr(mock_task, 'id', 1)
    mock_model.query.filter_by(id=1).first.return_value = mock_task

    task = get_task_details_from_db(1)
    mock_model.query.filter_by(id=1).first.assert_called_once_with()
    assert task.description == 'Task 1'
    assert task.department == 'IT'
