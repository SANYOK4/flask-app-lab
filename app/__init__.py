from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Імпорти блюпринтів
from .users.views import users_bp
from .todo.views import todo_bp
from .products.views import products_bp  # <--- 1. ДОДАЙ ЦЕЙ РЯДОК (ІМПОРТ)

# Реєстрація
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(todo_bp, url_prefix='/todo')
app.register_blueprint(products_bp, url_prefix='/products') # <--- 2. І ЦЕЙ (РЕЄСТРАЦІЯ)