from flask import Blueprint, render_template, request, redirect, url_for, flash, session

users_bp = Blueprint('users', __name__, template_folder='templates')

# Твої старі роути (hi, admin) залишаються тут...

@users_bp.route("/login", methods=["GET", "POST"])
def login():
    # Якщо користувач вже увійшов - кидаємо його в профіль
    if "username" in session:
        return redirect(url_for("users.profile"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Проста перевірка (імітація бази даних)
        if username == "user" and password == "pass":
            # Зберігаємо користувача в сесію
            session["username"] = username
            flash("Ви успішно увійшли!", "success")
            return redirect(url_for("users.profile"))
        else:
            flash("Невірний логін або пароль", "error")

    return render_template("users/login.html")

@users_bp.route("/profile")
def profile():
    # Перевіряємо, чи є користувач у сесії
    if "username" not in session:
        flash("Будь ласка, увійдіть для доступу до профілю", "warning")
        return redirect(url_for("users.login"))

    return render_template("users/profile.html", username=session["username"])

@users_bp.route("/logout")
def logout():
    # Видаляємо користувача з сесії
    session.pop("username", None)
    flash("Ви вийшли з системи", "info")
    return redirect(url_for("users.login"))