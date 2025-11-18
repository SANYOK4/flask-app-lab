from flask import Blueprint, render_template, request, url_for, redirect

# Створюємо блюпринт. template_folder вказує, де шукати шаблони саме для цього модуля
users_bp = Blueprint('users', __name__, template_folder='templates')

@users_bp.route("/hi/<string:name>")
def greetings(name):
    name = name.upper()
    age = request.args.get("age", None, int)
    return render_template("users/hi.html", name=name, age=age)

@users_bp.route("/admin")
def admin():
    # Зверни увагу: 'users.greetings' - ми додаємо префікс назви блюпринта
    return redirect(url_for('users.greetings', name='Administrator', age=45))