# 26_functions.py

# functions
# conversions
# https://www.mathsisfun.com/temperature-conversion.html


# fahrenheit to celsius formula
# (32°F − 32) × 5/9 = 0°C
# F = (9/5 × °C) + 32
# °F to °C	Deduct 32, then multiply by 5, then divide by 9
# F=(9/5)C+32

def fahr2celcius(fahr):
    celsius = (5 * (fahr - 32) ) / 9
    return celsius

print(fahr2celcius(212))

# celsius to fahrenheit formula
# (0°C × 9/5) + 32 = 32°F
# °C to °F	Divide by 5, then multiply by 9, then add 32

# Fahrenheit to Kelvin Method #2
# TK = (TF + 459.67) x 5/9
#


