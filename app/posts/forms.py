from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    
    # Додаємо пропущене поле type
    type = SelectField('Category', choices=[('Tech', 'Tech'), ('LifeStyle', 'LifeStyle'), ('Other', 'Other')], default='Other')

    author_id = SelectField("Author", coerce=int)
    tags = SelectMultipleField("Tags", coerce=int)
    
    enabled = BooleanField('Enabled', default=True)
    submit = SubmitField('Save Post')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from app.models import User, Tag 
        self.author_id.choices = [(user.id, user.username) for user in User.query.order_by(User.id).all()]
        self.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by(Tag.name).all()]