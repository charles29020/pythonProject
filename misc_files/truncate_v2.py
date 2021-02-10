# truncate_v2.py

import math 

num1 = float( input("Emter the first number (num1): ") )
num2 = float( input("Emter the first number (num2): ") )
x = int(-1)
y = int(-1)

# 
# def truncate_float(value, digits_after_point=2):
#     pow_10 = 10 ** digits_after_point
#     return (float(int(value * pow_10))) / pow_10

# def tf(value, digits_after_point=0):
#     if mod(2.1/2) == 0:
#         x = int(2)
#         print(x)
#     elif
#         x = float(x)
                    
        
#     return (float(int(value * pow_10))) / pow_10

# ***

# truncate_float(1.14333, 2)
# 1.14

# truncate_float(1.14777, 2)
# 1.14


# truncate_float(1.14777, 4)
# >>> 1.1477

# truncate_float(367.0)
# idk

# if num1 == 2.2:
y = int( math.floor( num1 ) )

# if num2 == 4.0:
x = int( math.floor( num2 ) )

    
print("-------")
print('num1 x: ', x)
print('num2 y: ', y)
print('num1: ' , num1)
print('num2: ' , num2)
print("-------")
