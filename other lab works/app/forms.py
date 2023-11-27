from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SelectField, SubmitField, EmailField
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
from wtforms.validators import Length

from app.models import User


class TodoForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    status = SelectField('Status', choices=[(0, 'Todo'), (1, 'In Progress'), (2, 'Done')], coerce=int, default=0)


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=14)])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Register')

    def validate_email(self, field):
        user = User.query.filter(User.email == field.data).first()
        if user:
            raise ValidationError("User with same email exists")

    def validate_username(self, field):
        user = User.query.filter(User.username == field.data).first()
        if user:
            raise ValidationError("User with same username exists")


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')
