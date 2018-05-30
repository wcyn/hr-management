import os

from app import create_app
app = create_app(os.getenv('APP_ENV'))

@app.route('/')
def hello():
    return "Hello"