from app import db
from datetime import datetime


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    
    grades = db.relationship('Grade', backref='subject', lazy=True)

    def __repr__(self):
        return self.name

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=False)  # Бал (наприклад, 85)
    comment = db.Column(db.String(200))            # Опис/коментар
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # Прив'язка до користувача

    def __repr__(self):
        return f"Grade({self.value}, {self.date_posted})"