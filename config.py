import os

class Config:
    # ... інші налаштування ...
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'