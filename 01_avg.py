# 01_avg.py - calculate the average of 2 numbers and explore data types
# lessons 3, 4, 5 and 6 combined

# lesson 3 - Statements
# lesson 4 - Variables
# lesson 5 - The Input Function
# lesson 6 - Exercise - Km to Miles Converter
# in python, you can make long lines shorter by using the \ character
# google this -> python make long lines shorter
# there are several solutions, for this code, I chose the \ character

# ask user for his/her name
me = input("Who are you? ")
print('hi ' + me)

# get the average of 2 numbers
# ask user for the 2 numbers
number1 = float ( input("input number1: ") )
number2 = float ( input("input number2: ") )

# print the numbers and average in various ways
print("type of number1 variable is " , type(number1) , " and type of me variable is", type(me))
print("let's average the numbers", number1, "and", number2)
print('the average of', number1 , 'and',  number2 , 'is', (number1+number2) / 2)

print("-------") # dashes to show a separation in the code
# Create a program that ask the user for a number of Kilometers,
# converts it to Miles and prints the result.
# 1 Mile = 1.609334 Km

km_converion_factor_c = 1.609334
km_in = float ( input("How many kilometers (999.99) to be converted to miles? ") )

miles = float(0.0)  # set this float to zero point zero (0.0)

print("type of km_converion_factor_c variable is " , type(km_converion_factor_c) , " and type of miles_in variable is", type(miles) \
      , "and type of miles is", type(miles) )

miles = km_in / km_converion_factor_c

print("kilometers to be converted are" , km_in , " = " , miles , "Miles")

# miles rounded down to 2 decimal places - round(number, decimal places) - in this case, round(miles, 2)
print("kilometers to be converted are" , km_in , " = " , round(miles, 2) , "Miles")
