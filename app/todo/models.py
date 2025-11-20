from app import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, default=False) # False = Active, True = Complete

    def __repr__(self):
        return f"Todo('{self.title}', '{self.status}')"