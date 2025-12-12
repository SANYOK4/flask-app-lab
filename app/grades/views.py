from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from .models import Grade, Subject
from .forms import GradeForm

grades_bp = Blueprint('grades', __name__, template_folder='templates')

@grades_bp.route('/', methods=['GET'])
def index():
    grades = Grade.query.order_by(Grade.date_created.desc()).all()
    return render_template('grades/index.html', grades=grades)

# Сторінка створення оцінки
@grades_bp.route('/create', methods=['GET', 'POST'])
def create():
    form = GradeForm()
    
    if form.validate_on_submit():
        grade = Grade(
            student_name=form.student_name.data,
            score=form.score.data,
            subject_id=form.subject_id.data
        )
        db.session.add(grade)
        db.session.commit()
        flash("Оцінку успішно додано!", "success")
        return redirect(url_for('grades.index'))
    
    return render_template('grades/create.html', form=form)