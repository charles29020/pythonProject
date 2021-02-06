# 21_for_loops.py

# for loops

blog_post = ["Hamburger","","First","Second","Third Post",""]

for post in blog_post:
    if post == "":
        continue
    else:
        print(post)
print(len(blog_post))  # returns 6 - placing this line outside of the indent,it only is printed when the looping is done

print("------------------")
# blog_post = ["Hamburger","","First","Second","Third Post",""]
# for post in blog_post:
# if post == "":
#     continue
# else:
#     print(post)

# loop thru mystring and print each character
mystring = "This is it"
for char in mystring:
    print(char)

print("------------------")

# loop thru x 6 times
for x in range(0,5):
    print(x)

print("------------------")
# loop thru a dictionary
# we loop thru all the elements in the dictionary
person = {"name":"Glynis M. Peters","first_name":"Glynis", "last_name":"Peters", "gender":"female","age":54,"address":"367 Bellerive Dr","phone":8645738737,"birth_year":1965, "country_of_birth":"United States"}

for key in person:
    print(key,":",person[key])

print("------------------")
# a dictionary was created from the blog_post list at the top of this script - a new property of the dictionary was added named Javascript
# loop inside another, first loops thru blog_post list of Python posts, the second inside the first loops thru the list of javascript posts by catagory
blog_post = {"Python":["Hamburger","First","Second","Third Post"],"Javascript": ["jQuery is good","react javascript is ok"]}

for catagory in blog_post:
    print("Post about", catagory)
    for post in blog_post[catagory]:
        print(post)