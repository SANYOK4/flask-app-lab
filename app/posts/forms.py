from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    
    # Випадаючий список типів
    type = SelectField('Type', choices=[
        ('News', 'News'), 
        ('Publication', 'Publication'), 
        ('Other', 'Other')
    ])
    
    enabled = BooleanField('Enabled', default=True)
    submit = SubmitField('Save Post')