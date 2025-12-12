from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# --- Імпорти Blueprint'ів ---
from .users.views import users_bp
from .todo.views import todo_bp
from .products.views import products_bp
from .posts.views import posts_bp
from .grades.views import grades_bp  # <--- 1. ДОДАЛИ ЦЕЙ РЯДОК

# --- Реєстрація Blueprint'ів ---
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(todo_bp, url_prefix='/todo')
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(posts_bp, url_prefix='/posts')
app.register_blueprint(grades_bp, url_prefix='/grades') # <--- 2. ДОДАЛИ ЦЕЙ РЯДОК