# 14_exercise_dictionary.py

# Exercise: Dictionaries
# Create a program with a predefined dictionary for a person. Include
# the following information: name, gender, age, address and phone.
#
# Ask the user what information he want's to know about the person
# (example: "name"), then print the value associated to that key or
# display a message in case the key is not found.

person = {"name":"Glynis M. Peters","first_name":"Glynis", "last_name":"Peters", "gender":"female","age":54,"address":"367 Bellerive Dr","phone":8645738737,"birth_year":1965, "country_of_birth":"United States"}
# show me the keys next
print (    "Value : %s" % person.keys()  , "zzz"  )
key_out = input("What key do you want to retrieve? ").lower()  # to ensure that the entered key is in lower case, use the .lower() method
val_out = person.get(key_out, "That key does not exist in person!")
print("For key,", key_out, "the value is",  val_out) # , "was retrieved.")

# type(person)
# print("type(person): ", type(person) )
# print(person)
# person["name"]
# person["first_name"]
# print('person["first_name"]: ', person["first_name"])





