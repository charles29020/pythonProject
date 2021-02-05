# 35_file_handiling-basics_read_write_and_append.py
# file handling, I created a text file named file.txt
# my code will be fun from the terminal

f = open("test.txt","w")
print("test.txt","w")


# print(f.read())

lp_cnt = 0
while lp_cnt < 7:
    lp_cnt += 1
    print("Looping at lp_cnt = ", str(lp_cnt) )
  #  f.write("\nLooping at lp_cnt = " + str(lp_cnt) )

print("Done at lp_cnt", lp_cnt)
f = open("test.txt","w")
f.write("\nDone at lp_cnt = " + str(lp_cnt) )  
# print(f.read())  
f = open("test.txt")
print(f.read())
