# 33_exercise_requests_and_json_pt1.py

# Create a game with one question and run until tbe user enters quit
# generate the url from https://opentdb.com/api_config.php
# get the requests, json, pprint, random and html modules

# python shuffle array
# look in stack overflow for the correct technique
# use this url generated from trivia quiz site
# line break is "\n"
# pip install html
# https://opentdb.com/api.php?amount=1

import requests
import json
import pprint
import random
import html

import matplotlib.pyplot as plt
import numpy as np

score_correct = 0
score_incorrect = 0

a_val = int
b_val = int

a_list = []
print("a_list(type(a_list): ", type(a_list))
b_list = []
print("b_list(type(b_list): ", type(b_list))

url = "https://opentdb.com/api.php?amount=1"
endGame = ""

while endGame != "quit":
    r = requests.get(url)
    if (r.status_code != 200):
        endGame = input("Sorry, there was a problem retrieving the question. Press enter to try again or type 'quit' to quit")
    else:
        answer_number = 1
        valid_answer = False
        data = json.loads(r.text)
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)

        print(html.unescape(question) + "\n")
        print("correct answer: " + html.unescape(correct_answer) + "\n")
        print("len(answers): ", len(answers))
        number_of_answers = len(answers)
        number_of_answers = int(number_of_answers)

        for answer in answers:
             # print((question + "\n"))
             # print(answer_number))  + " - "  + html.unescape(question) )
             print(str(answer_number) + " - " + html.unescape(answer) + "\n" )
             answer_number += 1

        while valid_answer == False:
            # input("Enter your answer")
            user_answer = input("\nWhich # is correct? ")

            # try:
            #     user_input = input()  # raw_input in Python 2.x
            #     if not user_input:
            #         raise ValueError('empty string')
            # except ValueError as e:
            #     print(e)

            try:
                user_answer = int(user_answer)
                # if ( user_answer >= 0 and user_answer <= number_of_answers ): # or user_answer <= 0 ):# or user_answer == input(): # or user_answer == "":  what if user accidentally does not enter an answer
                ###if (user_answer >= 1 or user_answer <= number_of_answers):
                if user_answer > len(answers) or user_answer <= 0:
                    print("Invalid Answer, you entered", user_answer, " range is 1 to ", number_of_answers )
                   # print("You entered ", user_answer)
                else:
                    valid_answer = True
            except:
                print("Invalid answer. Use only numbers. You entered ", user_answer)
               ### continue
               # user_answer = int(-1)

        user_answer = answers[int(user_answer) - 1 ]

        if user_answer == correct_answer:
            score_correct += 1
            print("\nCongratulations! You answered correctly! The correct answer was: " + str(answer_number - 1) + " - " + html.unescape(correct_answer) )
        else:
            score_incorrect += 1
            print("Sorry, " + html.unescape(user_answer) + " is incorrect. The correct answer is: " + str(answer_number - 1) + " - " + html.unescape(correct_answer))


        print("\n###########################")
        print("Your score is:")
        print("Correct Answers: " + str(score_correct))
        print("Incorrect Answers: " + str(score_incorrect))
        print("###########################")  # no new line

        a_val = score_correct
        b_val = score_incorrect

        print("--Lists Before--")
        print(a_list)
        print("a_list(type(a_list): ", type(a_list))
        print(b_list)
        print("b_list(type(b_list): ", type(b_list))
        # a_list = a_list.append(a_val)
        # b_list = b_list.append(b_val)

        a_list.append(a_val)
        b_list.append(b_val)

        print("--Vals--")
        print("a_val: ", a_val)
        print("b_val: ", b_val)

        print("--Lists After--")
        print(a_list)
        print(b_list)

        # a_list = a_list.append(score_correct)
        # b_list = b_list.append(score_incorrect)

        x = [1,2,3,4]
        y = [1500,1200,1100,1800]

        print("a_list")
        print(a_list)

        print("b_list")
        print(b_list)

        # print(x)
        # print(y)

        # plt.plot(a_list, b_list)

        x = a_list
        y = b_list

        print("len of x", len(x))
        if len(x) > 4:
            plt.plot(x, y)
            plt.show()

        

        endGame = input("\nPress enter to play again or type 'quit' to end the game. Any other keyed in value will cause the game to cobtinue. ").lower()

      #  if endGame != None:
        #     continue
        # else:
        #     print("Don't just press the enter key!")

    print("\nThanks for playing!")

# What if the user accidentally presses the enter key at the end of the program (endGame input statement) or during any answers (input statements)?

