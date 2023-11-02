from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, TextAreaField
from wtforms.validators import InputRequired

class FeedbackForm(FlaskForm):
    question1 = RadioField('Питання 1', choices=[('JavaScript', 'JavaScript'), ('Python', 'Python'), ('Java', 'Java')], validators=[InputRequired()])
    question2 = RadioField('Питання 2', choices=[('Менше 1 року', 'Менше 1 року'), ('1-3 роки', '1-3 роки'), ('Більше 3 років', 'Більше 3 років')], validators=[InputRequired()])
    question3 = TextAreaField('Питання 3')
