from flask import Blueprint, render_template, request, redirect, url_for, flash, session, make_response

users_bp = Blueprint('users', __name__, template_folder='templates')


@users_bp.route("/login", methods=["GET", "POST"])
def login():
    if "username" in session:
        return redirect(url_for("users.profile"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "user" and password == "pass":
            session["username"] = username
            flash("Ви успішно увійшли!", "success")
            return redirect(url_for("users.profile"))
        else:
            flash("Невірний логін або пароль", "error")

    return render_template("users/login.html")


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