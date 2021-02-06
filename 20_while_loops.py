# 20_while_loops.py

import random  # the random module

# While loops
# x = x + 1 or x += 1, the += increments the variable by 1

x = 0
number = 7

people = []
'''
# the while loop starts here, x is the incrementer
while x < 5:
    person = input("Enter the name of a person: ")
    people.append(person)
    x += 1
    print("x = ", x , people)
'''

'''
# the while loop starts here, it uses the length of the list as a limiter
while len(people) < 5:
    person = input("Enter the name of a person: ")
    people.append(person)
    print(people)
'''

# guessing game

r_number = random.randint(0,10)

guess = int (input("Guess the number that I'm thinking about: ") )

while True:
    if guess == r_number:
        break
    else:
        guess = int (input("Try again! " ) )
print("You guessed it. I was thinking about ", r_number )



