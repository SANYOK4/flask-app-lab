from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, NumberRange

class GradeForm(FlaskForm):
    # SelectField для вибору предмета (динамічно наповнимо у routes)
    subject_id = SelectField('Предмет', coerce=int, validators=[DataRequired()])
    
    value = IntegerField('Оцінка (бали)', validators=[
        DataRequired(), 
        NumberRange(min=0, max=100, message="Оцінка від 0 до 100")
    ])
    
    comment = TextAreaField('Коментар')
    submit = SubmitField('Зберегти')