# 05_lists_tuples.py
# will rename script as follows:
# 11_data_types-lists_tuples.py
# lesson covers r=the following:
# lists () / arrays - defined inside [] amd tuples defined in ()
# usage of the type() command to determine the type of a variable
# type(students) below will return <class 'str'>, you can do a print(type(student)) and <class 'str'> will be displayed
# run type(variable) to get the variable type, to see printed in a script, print(type(variable))
# old habits: print ( type ( variable ) ) - spaces used for clarity between
# old habits: variables named according to usage, for instance r_in or radius_in would be used instead of radius
# constants named with constant_name_c and output or returned variables named extra _r. this is not necessary
# this should be rum im a shell

print("lists/arrays amd tuples")
print("-------")
print("strings")
# string
print("students defined as a string - no () or [] or {} needed or used")
students = "Jim, Frank, Jones"
print(students)
type(students)
print(type(students))  # <class 'str'>
print(len(students)) # 17
# strings are immutable - can not be modified after created/defined

print("---")
# list / array
# redefine students as a list - use [] to do so
print("list / array")
print("redefine students as a list - use [] to do so")
students = ["Jim", "Framk", "Jones"]
print(students)
type(students)
print(type(students)) # <class 'list'>
len(students)
print(" len( students ) # 3", len(students) , "returned 3") # 3

print("---")
# tuples - immutable, values never change, you can't add or remove tuple elements after defined/created
# tuples - immutable, values never change, you can't add or remove tuple elements after defined/created
print("tuples - immutable, values never change, you can't add or remove tuple elements once they are created/defined")
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
print(months)
type(months)
print(type(months)) # <class 'tuple'>
print(len(months)) # 3
# pass the index of a tuple will return the value of index specified in [] - months[3] will return April
months[0] # Januaru
print("the line, months[0] will return", months[0]) # January
print(months[0]) # January
print(months[1]) # February
print(months[2]) # March
print(months[3]) # April
print("months[ 3 ]", months[ 3 ], "should return April")
# etc
# print(months[13]) # will generate an IndexError: tuple index out of range, there are only 12 values in our tuple
# print(months[14]) # will generate an IndexError: tuple index out of range, there are only 12 values in our tuple

print("---")
# investigate the proper [] usage
print("name at position 0 is" , students[0])  # Jim
print("name at position 1 is" , students[1])  # Frank
print("name at position 2 is" , students[2])  # Jones
# print("name at position 3 is" , students[3]) names only at 0, 1 and 2, passing in 3 will cause IndexError: list index out of range
print("name at position :2 is" , students[:2])  # ['Jim', 'Framk']
print("name at position :3 is" , students[:3])  # ['Jim', 'Framk', 'Jones']
print("name at position 2:3 is" , students[2:3])  # ['Jones']

print("---")
# array position and methods examples
print("array position and methods examples")
students
print(students)
print(type(students))

print(students[0]) # Jim
# change a item in the students list
print("change a item in the students list")
print("notice the usage of () vs []")
# notice the usage of () vs []
# students(0)= "Vinnie" # will generate error SyntaxError: can't assign to function call, do not use ()
students[0] = "Vinnie" # will generate error SyntaxError: can't assign to function call, remember, strings are immutable
print("now, display the students list")
print(students)
# or
print("command issued is print(students), none will be at the end of the statement" , print(students))
print("Jim is now Vinnie and length of students is still 3")
print(len(students))  # 3

print("---")
# try to add or change an item in a tuple
print("try to add or change an item in a tuple")
# months[0] = "Hanuary" # and error is generated, TypeError: 'tuple' object does not support item assignment, tuples are immutable
print(months) # January not changed to Hanuary

# add a students in a list using the append function
# function call parameters are usally enclosed in ()
print(len(students))  # 3
print("add a students to a list using the append function, check the student list length before and after")

students.append("Toby")
print(len(students))  # 4
print(students)

# insert into the list, insert function has 2 parameters, position, value (0,"Ted")
# examine the list
print("len(students) is", len(students))  # 4
print(students)

students.insert(0, "Ted")
print("len(students) is", len(students))  # 5, Ted added to first position in list
print(students)


# remove a list element using pop() method
print("len(students) is", len(students))  # 5
print(students)
print("students.pop()", students.pop())  # remove the last item from the list
print("len(students) is", len(students))  # 4
print(students) # the last item has been removed and the length has decreased by 1
# remove a list element using pop(2) method
print("students.pop(2)", students.pop(2)) # the item jn the third position has been removed and the length has decreased by 1
print(students) #
print("len(students) is", len(students))  # someone was deleted from tne list

# remove method a specific item
print("students.remove('Vinnie')", students.remove('Vinnie')) # the item jn the third position has been removed and the length has decreased by 1
print(students) #
print("len(students) is", len(students))  #

print("---")
# combine 2 lists
print("len(students) is", len(students))  #
students2 = ["John", "Paul", "Ringo", "George", "Billy Preston"]
print(students2)
print("len(students2) is", len(students2))  #
combined_students = students + students2
print("combined_students:", combined_students)
print("len(combined_students) is", len(combined_students))  #

# sort later
# print("combined_students.sort():",combined_students.sort())


# three of these don't always work to comment multiple lines'''
# students[0]
# students[-1]
# students[:2]
# students[2:3]
# '''

