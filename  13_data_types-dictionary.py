# 13_data_types-dictionary.py

# dictionaries are mutable - they can be modified after definition/creation
# Dictionaries are started with curly brackets as a key - value pair separated with a colon :.
# like the following:
# {"first_name":"John"}

person = {"first_name":"Glynis", "last_name":"Peters", "birth_year":1965, "country_of_birth":"United States"}
type(person)
print("type(person): ", type(person) )
print(person)
person["first_name"]
print('person["first_name"]: ', person["first_name"])
