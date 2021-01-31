# 16_exercise_data_types_booleans.py

import math # just in case
# set your age (as variable constant) and conpare jt to a users age and print whether the \
# user is older, younger or the same age
# instructors age is 32, I'll use that as my age constant
# age = 32
# add the date function to this script so that I wouldn't have a static age, it should be calulated

age = 32
users_age = int(input(" What is your age? ") )
age_diff = int

# print the ages, each on a separate line
print( "Age (instructors): ", age )
print( "Users Age Entered: " , users_age)
age_diff = abs(age - users_age)  # absolute value in case age_diff is negative - use the a abs(num) method

print( "The age difference in years is", age_diff , "years.")
# print( "Age difference in years is ", abs(age_diff) )

if age < users_age:
    # older - instructors age is less than the age entered
    print ("You are older than the instructor.")
elif age == users_age:
    # the ages are the same
    print("Your ages are the same.")
else:
    # younger - instructors age is greater than the age entered
    print("You are younger than the instructor.")
