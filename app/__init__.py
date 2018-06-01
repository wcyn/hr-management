from flask  import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from instance.config import app_config

db = SQLAlchemy()
api = Api()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config.get(config_name))

    from app.views.tasks import Tasks, Task_Details
    db.init_app(app)
    api.add_resource(Tasks, '/api/tasks')
    api.add_resource(Task_Details, '/api/tasks/<task_id>')
    api.init_app(app)

    return app