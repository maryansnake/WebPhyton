from flask import render_template
import os
import platform
from flask import request, flash, redirect, url_for
from datetime import datetime

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.forms import FeedbackForm
from app import app

app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
db = SQLAlchemy(app)


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question1 = db.Column(db.String(100))
    question2 = db.Column(db.String(100))
    question3 = db.Column(db.Text)


migrate = Migrate(app, db)


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    operating_system = os.uname()
    user_agent = request.headers.get('User-Agent')
    time_now = datetime.now()
    data = {
        "operating_system": operating_system,
        "user_agent": user_agent,
        "time_now": time_now,
    }
    form = FeedbackForm()
    if form.validate_on_submit():
        feedback = Feedback(
            question1=form.question1.data,
            question2=form.question2.data,
            question3=form.question3.data
        )
        db.session.add(feedback)
        db.session.commit()
        flash('Ваш відгук був успішно збережений', 'success')
        return redirect(url_for('survey'))
    feedback_list = Feedback.query.all()
    return render_template('survey.html', data=data, form=form, feedback_list=feedback_list)


@app.route('/')
def home():
    operating_system = os.uname()
    user_agent = request.headers.get('User-Agent')
    time_now = datetime.now()
    data = {
        "operating_system": operating_system,
        "user_agent": user_agent,
        "time_now": time_now,
    }
    return render_template('page1.html', data=data)


@app.route('/page2')
def page2():
    operating_system = os.uname()
    user_agent = request.headers.get('User-Agent')
    time_now = datetime.now()
    data = {
        "operating_system": operating_system,
        "user_agent": user_agent,
        "time_now": time_now,
    }
    return render_template('page2.html', data=data)


@app.route('/page3')
def page3():
    operating_system = os.uname()
    user_agent = request.headers.get('User-Agent')
    time_now = datetime.now()
    data = {
        "operating_system": operating_system,
        "user_agent": user_agent,
        "time_now": time_now,
    }
    return render_template('page3.html', data=data)


@app.route("/page4", methods=["GET"])
def page4():
    operating_system = os.uname()
    user_agent = request.headers.get('User-Agent')
    time_now = datetime.now()
    data = {
        "operating_system": operating_system,
        "user_agent": user_agent,
        "time_now": time_now,
    }
    skills = ["Photo takin", "Music playin", "c++ manual testin"]
    skill = request.args.get("skill", None)

    return render_template("page4.html", data=data, skills=skills, skill=skill, skills_len=len(skills))
