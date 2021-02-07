# 12_exercise_lists_and_tuples.py

# add a testing flag so that I don't have to see my little test prints
# I don't need the datetime or math modules imported
# import datetime
# inport math

people_list = ["Matthew","Mark","Luke","John"]

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
print("len(months): ", len(months) )
your_birthday = input("What is your birthday in DD-MM-YYYY format? ")
print("Your_birthday is", your_birthday)

# print(int(your_birthday[2] ) )
index = int(your_birthday[3:5] ) -1
birth_month = months[index]
print("index = ", index)
# answer for birth month
print("You were born in", birth_month)

print ("-------")
print(months[0])
print(months[1])
print(months[10])
print(months[11])

## month_num = int(your_birthday[4:6])
## print(month_num)
# birth_month = 'December'

# months[0:month_num - 1]
####### print("You were born in the month of" , months [index -1] ) # [birth_month])

### print("You were born in the month of" , months[month_num - 1:])


print("-------")

# print the people_list first
print(people_list)

# ask for my name to add to the list
my_name = input("What is your name? ")

# append my name to the people_list
people_list.append(my_name)

# print the updated people_list that should include my name
print("people_list:", people_list)