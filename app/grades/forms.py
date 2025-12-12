from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class GradeForm(FlaskForm):
    student_name = StringField('Student Name', validators=[DataRequired()])
    
    score = IntegerField('Score', validators=[DataRequired(), NumberRange(min=0, max=100, message="Оцінка має бути від 0 до 100")])
    
    subject_id = SelectField('Subject', coerce=int)
    
    submit = SubmitField('Save Grade')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from .models import Subject
        try:
            self.subject_id.choices = [(s.id, s.name) for s in Subject.query.order_by(Subject.name).all()]
        except:
            self.subject_id.choices = []