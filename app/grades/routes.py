from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import current_user, login_required
from app import db
from app.grades import grades_bp
from app.grades.models import Grade, Subject
from app.grades.forms import GradeForm

@grades_bp.route("/", methods=['GET'])
@login_required
def list_grades():
    search_query = request.args.get('q', '')
    sort_by = request.args.get('sort', 'date')
    
    query = Grade.query.filter_by(user_id=current_user.id)
    
    if search_query:
        query = query.join(Subject).filter(
            (Subject.name.contains(search_query)) | 
            (Grade.comment.contains(search_query))
        )
    
    if sort_by == 'value':
        query = query.order_by(Grade.value.desc())
    else:
        query = query.order_by(Grade.date_posted.desc())
        
    grades = query.all()
    return render_template('grades/list.html', grades=grades, search_query=search_query)

@grades_bp.route("/new", methods=['GET', 'POST'])
@login_required
def create_grade():
    form = GradeForm()
    form.subject_id.choices = [(s.id, s.name) for s in Subject.query.all()]
    
    if form.validate_on_submit():
        grade = Grade(
            value=form.value.data,
            comment=form.comment.data,
            subject_id=form.subject_id.data,
            user_id=current_user.id
        )
        db.session.add(grade)
        db.session.commit()
        flash('Оцінку додано!', 'success')
        return redirect(url_for('grades.list_grades'))
        
    return render_template('grades/form.html', form=form, title='New Grade')

@grades_bp.route("/<int:grade_id>/update", methods=['GET', 'POST'])
@login_required
def update_grade(grade_id):
    grade = Grade.query.get_or_404(grade_id)
    if grade.user_id != current_user.id:
        abort(403)
        
    form = GradeForm()
    form.subject_id.choices = [(s.id, s.name) for s in Subject.query.all()]
    
    if form.validate_on_submit():
        grade.value = form.value.data
        grade.comment = form.comment.data
        grade.subject_id = form.subject_id.data
        db.session.commit()
        flash('Оцінку оновлено!', 'success')
        return redirect(url_for('grades.list_grades'))
        
    elif request.method == 'GET':
        form.value.data = grade.value
        form.comment.data = grade.comment
        form.subject_id.data = grade.subject_id
        
    return render_template('grades/form.html', form=form, title='Update Grade')

@grades_bp.route("/<int:grade_id>/delete", methods=['POST'])
@login_required
def delete_grade(grade_id):
    grade = Grade.query.get_or_404(grade_id)
    if grade.user_id != current_user.id:
        abort(403)
        
    db.session.delete(grade)
    db.session.commit()
    flash('Оцінку видалено!', 'success')
    return redirect(url_for('grades.list_grades'))