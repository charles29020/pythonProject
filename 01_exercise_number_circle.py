# 01_exercise_number_circle.py
# will rename as follows
# 10_exercise_number_circle.py
# Also
# See script 04_circle_area.py. In that script, I utilize the math module (import math).

# Create a program to calculate the area and circumference of a circle. Ask for the radius.

# Area = pi * r squared
# Circumference = 2 * pi * r

# r = radius
# this uses an actual value for pi, the correct method is to import the math library of functions
# see x04_circle_area.py

pi = 3.14 # pi is 3.14
r_in = float( input("Enter the Radius? ") )  # r_in is radius that is passed in for calculations
area = pi * r_in **2

print ("In a circle where the radius is", r_in , " the area is" , area)

circum = 2 * pi * r_in

print("The circumference is" , circum)

# Also
# See script 04_circle_area.py. In that script, I utilize the math module (import math).