from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData
import config

app = Flask(__name__)
app.config.from_object('config.Config')

# 1. Визначаємо правила іменування (Naming Convention)
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

# 2. Створюємо MetaData з цими правилами
metadata = MetaData(naming_convention=convention)

# 3. Ініціалізуємо БД, передаючи metadata
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

# 4. Імпортуємо моделі (щоб міграції їх бачили)
from app.products import models

# 5. Імпортуємо та реєструємо блюпринти
from .users.views import users_bp
from .todo.views import todo_bp
from .products.views import products_bp
from .posts.views import posts_bp

app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(todo_bp, url_prefix='/todo')
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(posts_bp, url_prefix='/posts')