from flask import Blueprint, render_template, redirect, url_for, flash, request # <--- Перевір, чи є тут request
from app import db
from .models import Post
from .forms import PostForm

posts_bp = Blueprint('posts', __name__, template_folder='templates')

@posts_bp.route('/', methods=['GET', 'POST'])
def index():
    posts = Post.query.order_by(Post.created.desc()).all()
    return render_template('posts/index.html', posts=posts)

@posts_bp.route('/create', methods=['GET', 'POST'])
def create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            text=form.text.data,
            type=form.type.data,
            enabled=form.enabled.data
        )
        db.session.add(post)
        db.session.commit()
        flash("Пост успішно створено!", "success")
        return redirect(url_for('posts.index'))
    
    return render_template('posts/create.html', form=form, title="Create Post")

@posts_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    post = Post.query.get_or_404(id)
    form = PostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.text = form.text.data
        post.type = form.type.data
        post.enabled = form.enabled.data
        db.session.commit()
        flash("Пост оновлено!", "success")
        return redirect(url_for('posts.index'))
    
    # --- ОСЬ ТУТ БУЛА ПОМИЛКА ---
    # Ми перевіряємо, чи це GET запит (просто відкриття сторінки)
    if request.method == 'GET':
        form.title.data = post.title
        form.text.data = post.text
        form.type.data = post.type
        form.enabled.data = post.enabled
    # ---------------------------

    return render_template('posts/create.html', form=form, title="Update Post")

@posts_bp.route('/delete/<int:id>')
def delete(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash("Пост видалено!", "info")
    return redirect(url_for('posts.index'))