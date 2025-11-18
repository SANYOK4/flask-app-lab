from flask import Flask
# 1. Спочатку ніяких імпортів views тут не повинно бути!

app = Flask(__name__)
app.config.from_object('config') # Або app.config.from_pyfile('../config.py')

# 2. Тільки ПІСЛЯ створення app ми імпортуємо та реєструємо блюпринти
from .users.views import users_bp

app.register_blueprint(users_bp, url_prefix='/users')