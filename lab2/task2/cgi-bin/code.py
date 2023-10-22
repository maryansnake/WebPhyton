#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import http.cookies
import os

cgitb.enable()

form = cgi.FieldStorage()

delete_cookies = form.getvalue("delete_cookies")
if delete_cookies:
    print("Set-Cookie: form_counter=0")
    form_counter_from_cookie = 0
else:
    cookies = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))

    form_counter = int(cookies.get("form_counter", "0").value)
    form_counter += 1

    cookies["form_counter"] = form_counter

    print("Set-Cookie: form_counter={}".format(form_counter))

    form_counter_from_cookie = int(cookies.get("form_counter", "0").value)

print("Content-type: text/html\n")

def get_form_value(field_name):
    if field_name in form:
        return form[field_name].value
    else:
        return None

print("<html>")
print("<head>")
print("<title>Result</title>")
print("</head>")
print("<body>")

print("<h2>result: </h2>")
print("<p><strong>language: </strong> {0}</p>".format(get_form_value("programming_language")))
print("<p><strong>level: </strong> {0}</p>".format(get_form_value("experience_level")))

like_python = get_form_value("like_python")
if like_python:
    print("<p><strong>you are Python enjoyer! :D</strong></p>")
else:
    print("<p><strong>you are not Python enjoyer :(</strong></p>")

print("<p><strong>form count: </strong> {0}</p>".format(form_counter_from_cookie))

print('<form action="/cgi-bin/code.py" method="post">')
print('<input type="hidden" name="delete_cookies" value="true">')
print('<input type="submit" value="delete cookies">')
print('</form>')

print("</body>")
print("</html>")
