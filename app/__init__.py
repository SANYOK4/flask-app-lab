from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

app = Flask(__name__)
app.config.from_object('config.Config')

# 1. СПОЧАТКУ створюємо базу даних
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 2. ТІЛЬКИ ТЕПЕР імпортуємо блюпринти
# (Бо всередині views.py використовується змінна db, яку ми створили вище)
from .users.views import users_bp
from .todo.views import todo_bp
from .products.views import products_bp
from .posts.views import posts_bp

# 3. Реєструємо їх
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(todo_bp, url_prefix='/todo')
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(posts_bp, url_prefix='/posts')