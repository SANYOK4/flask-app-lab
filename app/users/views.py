from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from app.users.models import User
from app.users.forms import RegistrationForm, LoginForm, UpdateAccountForm

# Створюємо Blueprint
users_bp = Blueprint('users', __name__)

# --- РЕЄСТРАЦІЯ ---
@users_bp.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('products.get_all_products')) # Або інша головна сторінка
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Ваш акаунт створено! Тепер ви можете увійти', 'success')
        return redirect(url_for('users.login'))
        
    return render_template('users/register.html', title='Register', form=form)

# --- ЛОГІН (ВХІД) ---
@users_bp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.profile'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            
            # === ВАЖЛИВО: ОБРОБКА ПАРАМЕТРА NEXT ===
            # Це дозволяє повернутися на сторінку grades, якщо вас перекинуло звідти
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('users.profile'))
            
        else:
            flash('Вхід не вдався. Перевірте email та пароль', 'danger')
            
    return render_template('users/login.html', title='Login', form=form)

# --- ВИХІД ---
@users_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('users.login')) # Або на головну

# --- ПРОФІЛЬ ---
@users_bp.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        # Тут можна додати логіку зміни фото, якщо потрібно
        db.session.commit()
        flash('Ваш акаунт оновлено!', 'success')
        return redirect(url_for('users.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('users/profile.html', title='Account', image_file=image_file, form=form)