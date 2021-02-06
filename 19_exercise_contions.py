# 19_exercise_contions.py

'''
Exercise: conditions
Create a program to calculate the BMI (bodt mass index) of a person.
Ask the user for his height in meters and is weight in kg.

BMI = weight / (height * height)
Weight in Kg
Height in Meters

BMI = (weight / (height * height)) * 703
Weight in Pounds
Height in Inches
1 foot = 12 inches

Print the BMI and the classification from the table below:

Less than or equal to 18.5: Underweight
Greater than 18.5 or less than or equal to 24.9: Normal weight
Grater than 24.9 or less than or equal to 29.9: Overweight
Grater than or equal to 30: Obesity

Do in metric system and also print US system values.

Importing the math x would be a nice touch.

1 kilogram [kg]	1,000 g	arrow	2.2046 lb

1 Pound (lb) is equal to 0.45359237 kilogram (kg).
To convert pounds to kg, multiply the pound value by 0.45359237 or divide by 2.2046226218.

The length in meters is equal to the inches multiplied by 0.0254.

lb to kg
1 lb = 0.45359237 kilogram (kg)

155  * 0.45359237

1 in = 0.0254 m

'''

# calculate BMI

import math

# m_type = "metric"


# 1 inch = 0.0254 m
# 12 inches = 0.0254 * 12
# 5 ft 8 in
# ( 12 * 5 ) + 8 = inches


ft = float( input ( "How tall in ft are you? " ) )
inches = float( input ( "How many inches? " ) )
height_inches = ( ( ft * 12 ) + inches )
print( "height_inches: ", height_inches )

height_in_m = ( height_inches * 0.0254 )
print("height_in_m: ", height_in_m )

wt_in_lbs = float( input ( "How much do you weigh? " ) )
print("wt_in_lbs: ", wt_in_lbs)

wt_in_kg = wt_in_lbs * 0.45359237
print("wt_in_kg: ", wt_in_kg )


# BMI = weight / (height * height)
BMI_M = wt_in_kg / ( height_in_m * height_in_m )
print( "BMI_M: ", round( BMI_M, 1 ) )

# BMI = (weight / (height * height)) * 703
BMI_I = ( wt_in_lbs / ( height_inches * height_inches ) ) * 703
print( "BMI_I: ", round(BMI_I, 1 ) )

# matb.pow(BMI_T, 2) is really BMI_T * BMI_T (BMI_T squared)
BMI_T = wt_in_kg / ( math.pow(height_in_m,2)  )
print( "BMI_T ( math.pow(height_in_m,2 ): ", round( BMI_T, 1 ) )

# BMI Classification
# Less than or equal to 18.5: Underweight
if ( BMI_M <= 18.5 ):
    classification = "Underweight!"
    print("Classification is Underweight")
    print("Underweight!")
# Greater than 18.5 or less than or equal to 24.9: Normal weight
elif ( BMI_M > 18.5 ) and ( BMI_M <= 24.9 ):
    classification = "Normal weight!"
    print("Classification is Normal weight!")
    print("Normal weight!")
# Grater than 24.9 or less than or equal to 29.9: Overweight
elif ( BMI_M > 24.9 ) and ( BMI_M <= 29.9 ):
    classification = "Overweight!"
    print("Classification is Overweight")
    print("Overweight!")
# Grater than or equal to 30: Obesity
elif ( BMI_M >= 30.0):
    classification = "Obesity!"
    print("Classification is Obesity")
    print("Obesity!")

