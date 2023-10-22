#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import cgitb

cgitb.enable()

print("Content-type: text/html\n")

form = cgi.FieldStorage()

def get_form_value(field_name):
    if field_name in form:
        return form[field_name].value
    else:
        return None

programming_language = get_form_value("programming_language")
experience_level = get_form_value("experience_level")
like_python = get_form_value("like_python")

print("<html>")
print("<head>")
print("<title>Result</title>")
print("</head>")
print("<body>")

print("<h2>Result:</h2>")
print("<p><strong>language: </strong> {0}</p>".format(programming_language))
print("<p><strong>level:</strong> {0}</p>".format(experience_level))

if like_python:
    print("<p><strong>you are Python enjoyer! :D</strong></p>")
else:
    print("<p><strong>you are not Python enjoyer :(</strong></p>")

print("</body>")
print("</html>")
