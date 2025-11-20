import os

class Config:
    # ... інші налаштування ...
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key'
    # --- ДОДАЙ ЦІ ДВА РЯДКИ ---
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False