# x04_circle_area.py
# see https://www.mathsisfun.com/geometry/circle-area.html to test your results
# will rename script as follows:
# 04_circle_area.py
# Note
# This script matches lesson 10 - Exercise - Numbers

# Area = pi * r squared
# Circumference = 2 * pi * r
# or even better 2 * math.pi * r

# r_in = radius
# this uses the math.pi, the correct method is to import the math library of functions
# see x04_circle_area.py

# import the math function library

import math

r_in = float( input("Enter the Radius? ") )  # r_in is radius that is passed in for calculations
area = math.pi * ( r_in ** 2 )
circumference = 2 * math.pi * r_in

print("The area of a circle with a radius of" , r_in , " is" , round(area, 2) , "and the circumference is" , round(circumference, 2) )

print("The circle radius passed in is", r_in )
print("FYI: The circle diameter (radius * 2) is", r_in * 2 )
print("The area of the circle is", area )
print("The area of the circle is", round(area, 2) )
print("The circumference of the circle is", circumference )
print("The circumference of the circle is", round(circumference, 2) )