# 30_request.py
# script command work best in a console

import requests

r = requests.get("https://www.google.com/")

r.status_code
print("r.status_code: ", r.status_code)  # r.status_code:  200
# status_code value are 200 = Ok, 403 = Forbidden, 404 = Not Found

type(r)
print("type(r): ", type(r))  # type(r):  <class 'requests.models.Response'>

r.headers

r.headers["Date"]

r.text
