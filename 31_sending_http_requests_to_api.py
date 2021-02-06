# 31_sending_http_requests_to_api.py

# printing stuff to google -> python print w3schools
# https://www.w3schools.com/python/ref_func_print.asp or https://www.w3schools.com/python/python_string_formatting.asp
# https://www.w3schools.com/python/default.asp - good python tutorial and related info
# import the requests module, we need it to make a request to url
# to find good samples google -> request api python quiz
# the one used here is from -> https://opentdb.com/ - https://opentdb.com/api_config.php - just make a few sections and generate the url
# try this one https://opentdb.com/api.php?amount=5&category=22&difficulty=medium&type=multiple


import requests
# see https://requests.readthedocs.io/en/master/ and https://www.w3schools.com/python/module_requests.asp for more info on the requests module
# or just google python requests module

r = requests.get("https://opentdb.com/api.php?amount=3&category=10&difficulty=medium&type=multiple")
r.status_code
r.text # 200 = Ok, 403 = Forbidden, 404 = Not Found

type(r)
print("type(r): ", type(r))

# import the json module, we will need it go grab content from the request
import json
# see https://docs.python.org/3/library/json.html and https://www.w3schools.com/python/python_json.asp for more info on the json module
# or just google python json module, this will convert the response into a dictionary - dict

question = json.loads(r.text)

type(r)
print("type(question): ", type(question))
# type(question):  <class 'dict'>

import pprint
# see https://docs.python.org/3/library/pprint.html and https://www.tutorialspoint.com/pprint-module-data-pretty-printer for more info on the json module
# or just google python pprint module
pprint.pprint(question)
type(question)  # type(question):  <class 'dict'>

# based on the output of the bracket [, we know that this is a list
# to get something from the list, we know that the list in in a dict {
# to get the first thing in the results list, we get the category as follows
# question['results'][0]'category']

# print("question['results'][0]'category']: ", question['results'][0]'category'])
# question['results'][0]'correct_answer']
# question['results'][0]'category']
# question['results'][0]'incorrect_answers']
# question['results'][0]'question']
# question['results'][0]'type']


## question['results'][0]['category']

# next, we will create a quiz, ask the question and get the answer

# json.dump

# make a dictionary
# convert a python dictionary using json ...

# make dict named person with two keys name and age
# make a variable named person_json
# next create the json document using function json.dumps(person)

person = {'Name':'John','Age':30} # this is a dict

person_json = json.dumps(person)  # converted to json

person_json  # show the json document

print(person_json)

type(person_json) # verify that it is json - str

print("type(person_json): ", type(person_json))
