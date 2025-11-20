from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, Regexp

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(), 
        Length(min=4, max=10, message="Пароль має бути від 4 до 10 символів")
    ])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(), 
        Length(min=4, max=10, message="Ім'я має бути від 4 до 10 символів")
    ])
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    # Валідація телефону
    phone = StringField('Phone', validators=[
        DataRequired(),
        Regexp(r'^\+380\d{9}$', message="Формат: +380xxxxxxxxx")
    ])
    
    subject = SelectField('Subject', choices=[
        ('bug', 'Report a Bug'),
        ('feature', 'Feature Request'),
        ('other', 'Other')
    ])
    
    message = TextAreaField('Message', validators=[
        DataRequired(),
        Length(max=500, message="Повідомлення не більше 500 символів")
    ])
    
    submit = SubmitField('Send')