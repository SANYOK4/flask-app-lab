from app import db
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

# 1. Таблиця зв'язку (Association Table) має бути оголошена перед класами, що її використовують
post_tags = db.Table(
    'post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(db.String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(db.String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(100), nullable=False)
    
    posts: Mapped[list["Post"]] = relationship(back_populates="user", cascade="all, delete-orphan")

class Tag(db.Model):
    __tablename__ = 'tags'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(50), unique=True, nullable=False)
    
    # Зв'язок з постами
    posts: Mapped[list["Post"]] = relationship(secondary=post_tags, back_populates="tags")

class Post(db.Model):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), default='default.jpg')
    created = db.Column(db.DateTime, default=datetime.now)
    type = db.Column(db.String(50), default='Other')
    enabled = db.Column(db.Boolean, default=True)

    # Зовнішній ключ (One-to-Many)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    # Зв'язок з User
    user: Mapped["User"] = relationship(back_populates="posts")

    # Зв'язок з Tags (Many-to-Many) - додаємо сюди, а не в окремий клас
    tags: Mapped[list["Tag"]] = relationship(secondary=post_tags, back_populates="posts")

    def __repr__(self):
        return f"Post('{self.title}', '{self.created}')"