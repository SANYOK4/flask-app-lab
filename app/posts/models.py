from app import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), default='default.jpg')
    created = db.Column(db.DateTime, default=datetime.now)
    type = db.Column(db.String(50), default='Other')
    enabled = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.created}')"