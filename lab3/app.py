from flask import Flask, render_template
import os
import platform
from flask import request
from datetime import datetime

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
