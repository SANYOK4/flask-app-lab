from flask import Blueprint

# 1. Створюємо блюпринт
grades_bp = Blueprint('grades', __name__, template_folder='templates')

# 2. Імпортуємо маршрути (щоб вони зареєструвалися в блюпринті)
from . import routes