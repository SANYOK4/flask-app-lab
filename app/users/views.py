from flask import Blueprint, render_template, request, redirect, url_for, flash, session, make_response
from .forms import LoginForm, ContactForm

users_bp = Blueprint('users', __name__, template_folder='templates')

@users_bp.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f"Повідомлення від {form.name.data} успішно надіслано!", "success")
        return redirect(url_for("users.contact"))
    
    return render_template("users/contact.html", form=form)

@users_bp.route("/login", methods=["GET", "POST"])
def login():
    if "username" in session:
        return redirect(url_for("users.profile"))

    form = LoginForm()
    
    if form.validate_on_submit(): 
        # Зверни увагу: тут нові дані для входу (user@example.com)
        if form.email.data == "user@example.com" and form.password.data == "pass123":
            session["username"] = form.email.data
            flash("Ви успішно увійшли!", "success")
            
            if form.remember.data:
                flash("Ми вас запам'ятали (demo)", "info")
                
            return redirect(url_for("users.profile"))
        else:
            flash("Невірний логін або пароль", "error")

    return render_template("users/login.html", form=form)

@users_bp.route("/profile")
def profile():
    if "username" not in session:
        flash("Будь ласка, увійдіть", "warning")
        return redirect(url_for("users.login"))
    
    return render_template("users/profile.html", 
                           username=session["username"], 
                           cookies=request.cookies)


@users_bp.route("/cookie/add", methods=["POST"])
def add_cookie():
    if "username" not in session: return redirect(url_for("users.login"))

    key = request.form.get("key")
    value = request.form.get("value")
    age = request.form.get("age")

    resp = make_response(redirect(url_for("users.profile")))
    
    resp.set_cookie(key, value, max_age=int(age))
    flash(f"Куку '{key}' успішно додано!", "success")
    return resp

@users_bp.route("/cookie/delete", methods=["POST"])
def delete_cookie():
    if "username" not in session: return redirect(url_for("users.login"))

    key = request.form.get("key")
    
    resp = make_response(redirect(url_for("users.profile")))
    
    resp.set_cookie(key, '', expires=0)
    flash(f"Куку '{key}' видалено.", "info")
    return resp

@users_bp.route("/cookie/delete_all", methods=["POST"])
def delete_all_cookies():
    if "username" not in session: return redirect(url_for("users.login"))
    
    resp = make_response(redirect(url_for("users.profile")))
    
    cookies = request.cookies
    for key in cookies:
        if key != "session":
            resp.set_cookie(key, '', expires=0)
            
    flash("Всі куки видалено!", "warning")
    return resp
    
@users_bp.route("/logout")
def logout():
    session.pop("username", None)
    flash("Ви вийшли з системи", "info")
    return redirect(url_for("users.login"))

@users_bp.route("/set_theme/<string:theme_name>")
def set_theme(theme_name):
    resp = make_response(redirect(request.referrer or url_for('users.profile')))
    
    if theme_name in ['dark', 'light']:
        resp.set_cookie('theme', theme_name, max_age=30*24*60*60)
        flash(f"Тему змінено на {theme_name}", "success")
    
    return resp