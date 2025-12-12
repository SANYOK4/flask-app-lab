from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime

# Допоміжна модель (Предмет)
class Subject(db.Model):
    __tablename__ = "subjects"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(50), unique=True, nullable=False)
    
    # Зв'язок: Один предмет має багато оцінок
    grades: Mapped[list["Grade"]] = relationship(back_populates="subject")

    def __repr__(self):
        return self.name

# Основна модель (Оцінка)
class Grade(db.Model):
    __tablename__ = "grades"
    id: Mapped[int] = mapped_column(primary_key=True)
    student_name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    score: Mapped[int] = mapped_column(nullable=False) # Оцінка (0-100)
    date_created = db.Column(db.DateTime, default=datetime.now)
    
    # Зовнішній ключ на Предмет
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    
    # Зв'язок назад
    subject: Mapped["Subject"] = relationship(back_populates="grades")