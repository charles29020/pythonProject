# 27_time.py

# Unix epoch January 01, 1970 at 00:00:00
# 01/01/1971 00:00:00
# https://www.epochconverter.com/

import time as t

# 1 day = 86400
num_secs_in_day = 86400

print("-------")
lt = t.localtime()  # <class 'time.struct_time'>
print("type(lt): ", type(lt))

local_time_now = t.localtime()

time_now = t.time()

print("-------")
print("Time Now: ", time_now)

# year_now = t.tm_year
# month_now = t.time.

print("-------")
print(local_time_now)

# time.struct_time ( tm_year=2021, tm_mon=2, tm_mday=10, tm_hour=20, tm_min=25, tm_sec=4, tm_wday=2, tm_yday=41, tm_isdst=0 )
print("-------")
print("Local Time Now (local_time_now): ", str(local_time_now.tm_hour) + ":" + str(local_time_now.tm_min) + ":" + str(local_time_now.tm_sec) )


# seven days from today
seven_days_from_now = 0.0

seven_days_from_now = time_now + ( num_secs_in_day * 7 ) 

print("-------")
print("Seven Days Froim Now: ", seven_days_from_now )

t.localtime(seven_days_from_now)
print("t.localtime(seven_days_from_now): ", t.localtime(seven_days_from_now) )

dday = t.localtime(seven_days_from_now) 
print("dday: ", dday)

print("-------")
dday_str = str(dday.tm_mon) + "/" + str(dday.tm_mday) + "/" + str(dday.tm_year)

print("D-Day: ", dday_str)

valid_answer = False

while valid_answer == False:
    my_special_day = int( input("Enter the number of days from today: ") )

    try:
        my_special_day = int(my_special_day)
        # if ( user_answer >= 0 and user_answer <= number_of_answers ): # or user_answer <= 0 ):# or user_answer == input(): # or user_answer == "":  what if user accidentally does not enter an answer
        ###if (user_answer >= 1 or user_answer <= number_of_answers):
        if my_special_day < 0:
            print("Invalid Answer, you entered", my_special_day, " range is 1 to ", 1111111 )
            # print("You entered ", my_special_day)
        else:
            valid_answer = True
    except:
        print("Invalid answer. Use only numbers. You entered ", my_special_day)
               ### continue
               # user_answer = int(-1)

# num_secs_in_day = 86400
my_special_date = time_now = t.time() + ( my_special_day * num_secs_in_day)

print("My Special Days From Today is", my_special_day) # , " and that date is ", str(my_special_date.tm_mon) + "/" + str(my_special_date.tm_mday) + "/" + str(my_special_date.tm_year) )

# readable_7_days_from_now = str(seven_days_from_now.tm_hour) + ":" + str(seven_days_from_now.tm_min) + ":" + str(seven_days_from_now.tm_sec)

# print("Readable Seven Days from today: " , readable_7_days_from_now )


