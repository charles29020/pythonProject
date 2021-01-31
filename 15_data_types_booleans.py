# 15_data_types_booleans.py
# Udemy lesson notes and examples
# Booleans data type and different number types (int and float)
# True or False - no quotes
# float values that are really integers will be converted
# import the math library, this will allow the math.floor command to remove the .0 from num1 and num2 when printed

import math

# define the integer variables
n1 = int
n2 = int

# define the different float variables
num1 = float( input("Enter the first number: ") )
num2 = float( input("Enter the second number: ") )

n1 = int( math.floor(num1) )  # this int( math.floor() will make tbe floted values to be printed without the .0
n2 = int( math.floor(num2) )  # this int( math.floor() will make tbe floted values to be printed without the .0

print( "num1: ", num1 )
print( "num2: ", num2 )

print( "n1: ", n1 )
print( "n2: ", n2 )

# this if statement to compare the numbers entered as input values
# the colon must be entered at the end of if, elif and else statements
# for each if option, the  comparison results are printed with different print parameters

if ( num1 > num2 ):

    print( "num1:" , num1 , "is greater than num2:" , num2 )
    print( num1, "is greater than ", num2 )
    print( "num1 is greater than num2" )
    print( "num1 > num2" )
    print ( n1 , '>' ,  n2 )

elif (num1 == num2):

    print( num1 , " is equal to" , num2 )
    print( "num1 is equal num2" )
    print( num1 , " == " , num2 )
    print( "num1 = num2" )
    print ( n1 , '==' , n2 )

else:

    print( "num1:" , num1 , "is less than num2:" , num2 )
    print( "num1:", round(num1), "is less than num2:", round(num2) )
    print( num1 , "is less than " , num2 )
    print( "num1 is less than num2" )
    print( "num1 < num2" )
    print ( n1 , '<' , n2 )
