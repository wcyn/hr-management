# HR Management System
A HR Managment app for successful Candidates

## How to run the app
- Clone the repos into your virtual environment
- Run:
```
pip install -r requirements.txt
```
- Export these variables by running the following:
```
export FLASK_APP='run.py'
```
```
export DATABASE_URL='postgres://localhost/my_database'
```
```
export APP_ENV='development'
```

Ensure to create your database

- Run Alembic to initialize the database
```
python manage.py db init
```

- Make migrations
```
python manage.py db migrate
```
- Finally, upgrade the database
```
python manage.py db upgrade
```

Run the application:

```
flask run
```