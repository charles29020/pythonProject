# 32_working_with_json.py

# printing stuff to google -> python print w3schools
# https://www.w3schools.com/python/ref_func_print.asp or https://www.w3schools.com/python/python_string_formatting.asp
# https://www.w3schools.com/python/default.asp - good python tutorial and related info
# import the requests module, we need it to make a request to url
# to find good samples google -> request api python quiz
# the one used here is from -> https://opentdb.com/ - https://opentdb.com/api_config.php - just make a few sections and generate the url
# try this one https://opentdb.com/api.php?amount=5&category=22&difficulty=medium&type=multiple


# request are typically returned in json
# get some sample data from -> https://opentdb.com/api_config.php
# import of all modules to be used in a program can be imported at the top of the script
# import modules requests, json and pprint

import requests
# see https://requests.readthedocs.io/en/master/ and https://www.w3schools.com/python/module_requests.asp for more info on the requests module
# or just google python requests module

# import the json module, we will need it go grab content from the request
import json

import pprint
# see https://docs.python.org/3/library/pprint.html and https://www.tutorialspoint.com/pprint-module-data-pretty-printer for more info on the json module


import requests
# see https://requests.readthedocs.io/en/master/ and https://www.w3schools.com/python/module_requests.asp for more info on the requests module
# or just google python requests module

r = requests.get("https://opentdb.com/api.php?amount=3&category=10&difficulty=medium&type=multiple")
r.status_code
r.text # 200 = Ok, 403 = Forbidden, 404 = Not Found

type(r)
print("type(r): ", type(r))


# see https://docs.python.org/3/library/json.html and https://www.w3schools.com/python/python_json.asp for more info on the json module
# or just google python json module, this will convert the response into a dictionary - dict

question = json.loads(r.text)

type(r)
print("type(question): ", type(question))
# type(question):  <class 'dict'>


# or just google python pprint module
pprint.pprint(question)
type(question)  # type(question):  <class 'dict'>

## question['results'][0]['category']





