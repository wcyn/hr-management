from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
    duration_in_days = db.Column(db.Integer, default=1)
    # TODO: Create Department Model
    department = db.Column(db.String(255), nullable=False)

    def __init__(self, description, department):
        self.description = description
        self.department = department

    def create(self):
        db.session.add(self)
        db.session.commit()


    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Task: {}>".format(self.description)