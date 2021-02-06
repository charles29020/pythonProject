# 17_conditions-if-elif-else.py

# Look at a student grading scenario
# student grades in classes and attendance help determine a grade
# assume 3 test grades

# Rules
# Grades are 0 to 10
# There will be 3 graded tests
# Students need an average grade of 6 or higher to get approval
#   an average grade below 6 will cause a failure
# Students need an absences rate of 80% or higher to get approval
#   an absences rate will cause a failure

tests = 3
grade1 = float(input ("Enter the grade of the first test: ") )
grade2 = float(input ("Enter the grade of the second test: ") )
grade3 = float(input ("Enter the grade of the third test: ") )

absences = int (input ("Enter the total number of absences: ") )
total_classes = int (input ("Enter the number of classes: ") )

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

if (avg_grade >= 6 ):
    if (attendance_rate >= 80 ):
       print("Passed - Good Job!")  # need an average grade of 6 or higher to get approval
    else:
       print("Failed - The student had good grades but too many absences.")  # need an attendance rate of 80% or higher to get approval
elif (attendance_rate >= 80):
        print("Failed - The student had poor test scores but attend classes at an acceptable rate.")
else:
    print("Failed - The student had bad grades and an attendance rate below 80%.")  # need an average grade of 6 or higher to get approval, below 6 will cause a failure