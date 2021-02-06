# 13_data_types-dictionary.py

# see -> https://www.tutorialspoint.com/python/
# see dictionary hints at https://www.tutorialspoint.com/python/dictionary_has_key.htm
# dictionaries are mutable - they can be modified after definition/creation
# Dictionaries are started with curly brackets as a key - value pair separated with a colon :.
# like the following:
# {"first_name":"John"}
# all keys are in lower case, when seeking a key use the .lower() method at the end of you input call

person = {"first_name":"Glynis", "last_name":"Peters", "birth_year":1965, "country_of_birth":"United States"}
print("-------------")
print("Hint from -> https://www.tutorialspoint.com/python/dictionary_has_key.htm")
print('command is -> print "Value : %s" % person.keys() ')
print('"Value : %s" % person.keys()')
print ("Value : %s" % person.keys() )
print("-------------")
type(person)
print("type(person): ", type(person) )
print(person)
person["first_name"]
print('person["first_name"]: ', person["first_name"])
print("-------------")
print("Hint from -> https://www.tutorialspoint.com/python/dictionary_has_key.htm")
print('command is -> print "Value : %s" % person.keys() ')
print('"Value : %s" % person.keys()')
print (    "Value : %s" % person.keys()  , "zzz"  )
print("-------------")
