from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt  # <--- ОСЬ ЦЕЙ ІМПОРТ ВИ ПРОПУСТИЛИ
from sqlalchemy import MetaData
import config

# 1. Визначаємо правила іменування для БД
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

# 2. Створюємо додаток
app = Flask(__name__)
app.config.from_object('config.Config')

# 3. Ініціалізуємо розширення
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)  # Ініціалізація шифрування паролів

login_manager = LoginManager(app)
login_manager.login_view = 'users.login' # Якщо не залогінений -> йдемо сюди
login_manager.login_message_category = 'info'

# 4. Імпорт моделі User та функція завантаження (для LoginManager)
# Переконайтесь, що файл app/users/models.py існує!
from app.users.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# 5. Імпорт інших моделей (щоб міграції їх бачили)
from app.products import models
from app.grades import models 

# 6. Імпорт та реєстрація Блюпринтів
from .users.views import users_bp
from .todo.views import todo_bp
from .products.views import products_bp
from .posts.views import posts_bp
from app.grades import grades_bp 

app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(todo_bp, url_prefix='/todo')
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(posts_bp, url_prefix='/posts')
app.register_blueprint(grades_bp, url_prefix='/grades')