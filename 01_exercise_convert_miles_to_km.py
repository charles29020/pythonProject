# 01_exercise_convert_miles_to_km.py
# convert miles to km

km_converion_factor_c = 1.609334

miles_in = float ( input("How many kms (999.99)do you want to convert to miles? ") )

converted_kms = float(0.0)  # set this float to zero point zero (0.0)

print("type of km_converion_factor_c variable is " , type(km_converion_factor_c) , " and type of miles_in variable is", type(miles_in))

converted_kms = miles_in * km_converion_factor_c

print("miles_in is " , miles_in , " is" , converted_kms , "km")