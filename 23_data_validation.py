# 23_data_validation.py

# refer to student grades program (18_conditions-and-or.py)
# DATA VALIDATION USING LOOPS TO BE APPLIED TO THIS SCRIPT

# 18_conditions-and-or.py

# Look at the same student grading scenario as previous lesson, but this time, use and - or conditions.
# student grades in classes and attendance help determine a grade
# assume 3 test grades
# use and and or conditions

# Rules
# Grades are 0 to 10
# There will be 3 graded tests
# Students need an average grade of 6 or higher to get approval
#   an average grade below 6 will cause a failure
# Students need an absences rate of 80% or higher to get approval
#   an absences rate will cause a failure

tests = 3

### grade1 = float(input ("Enter the grade of the third test: ") )
data_valid = False

while data_valid == False:
    grade1 =  input ("Enter the grade of the first test: ")
    try:
        grade1 = float(grade1)
        print("The number of absences is:", grade1)
    except:
        print("This grade value is invalid, this must be a number and can have decimals. No string characters.")
        continue

    if grade1 < 0 or grade1 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True


### grade2 = float(input ("Enter the grade of the second test: ") )
data_valid = False

while data_valid == False:
    grade2 = input ("Enter the grade of the second test: ")
    try:
        grade2 = float(grade2)
        print("The number of absences is:", grade2)
    except:
        print("This grade value is invalid, this must be a number and can have decimals. No string characters.")
        continue
    if grade2 < 0 or grade2 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True

### grade3 = float(input ("Enter the grade of the third test: ") )
data_valid = False

while data_valid == False:
     grade3 = input("Enter the grade of the third test: ")
     try:
         grade3 = float(grade3)
         print("The number of absences is:", grade3)
     except:
         print("This grade value is invalid, this must be a number and can have decimals. No string characters.")
         continue
     if grade3 < 0 or grade3 > 10:
         print("Grade should be between 0 and 10")
         continue
     else:
         data_valid = True


data_valid = False

while data_valid == False:
     total_classes = input ("Enter the number of classes: ")
     try:
         total_classes = int(total_classes)
         print("The number of absences is:", total_classes)
     except:
         print("This total classes value is invalid, this must be a number without decimals or string characters.")
         continue
     if total_classes < 1:
         print("This must be a number without decimals.")
         continue
     else:
         data_valid = True

data_valid = False

while data_valid == False:
    absences = input ("Enter the total number of absences: ")
    try:
        absences = int(absences)
        print("The number of absences is:", absences)
    except:
        print("This absences value is invalid")
        continue

    if ( absences < 0 ) or ( absences > total_classes ):
        print("You can not have less than zero absences and you can not have more absences than classes!")
        continue
    else:
        data_valid = True


avg_grade = ( (grade1 + grade2 + grade3) / tests) # * 100
attendance = (total_classes - absences)
attendance_rate = (attendance / total_classes) * 100

# values
print("Grade1 = ", grade1)
print("Grade2 = ", grade2)
print("Grade3 = ", grade3)
print("Absences = ", absences)
print("Total Classes = ", total_classes)
print("Average Grade = ", round(avg_grade,2) )
print("Attendance Rate =", str(round(attendance_rate,0) ) +'%')

# from lesson 18- Conditions (if, elif and else)
# if (avg_grade >= 6 ):
#     if (attendance_rate >= 80 ):
#        print("Passed - Good Job!")  # need an average grade of 6 or higher to get approval
#     else:
#        print("Failed - The student had good grades but too many absences.")  # need an attendance rate of 80% or higher to get approval
# elif (attendance_rate >= 80):
#         print("Failed - The student had poor test scores but attend classes at an acceptable rate.")
# else:
#     print("Failed - The student had bad grades and an attendance rate below 80%.")  # need an average grade of 6 or higher to get approval, below 6 will cause a failure
#
###

if   (avg_grade >= 6 ) and (attendance_rate >= 80 ):
    print("Passed - Good Job!")  # need an average grade of 6 or higher to get approval
elif (avg_grade < 6  ) and (attendance_rate < 80):
    print("Failed - The student had bad grades but an acceptable attendance rate above 80%.")
elif (avg_grade >= 6 ) and (attendance_rate < 80):
    print("Failed - The student had good test scores but attendance rate below 80%.")
# else:
#     print("Failed - The student had an attendance rate below 80%.")  # need an average grade of 6 or higher to get approval, below 6 will cause a failure




