from flask import Blueprint, render_template, redirect, url_for
from app import db
from .models import Todo
from .forms import TodoForm

todo_bp = Blueprint('todo', __name__, template_folder='templates')

@todo_bp.route('/', methods=['GET', 'POST'])
def index():
    form = TodoForm()
    
    # Додавання
    if form.validate_on_submit():
        new_todo = Todo(title=form.title.data)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('todo.index'))

    # Вивід списку
    todos = Todo.query.all()
    return render_template('todo/todo.html', todos=todos, form=form)

@todo_bp.route('/update/<int:id>')
def update(id):
    todo = Todo.query.get_or_404(id)
    todo.status = not todo.status  # Змінюємо статус на протилежний
    db.session.commit()
    return redirect(url_for('todo.index'))

@todo_bp.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('todo.index'))