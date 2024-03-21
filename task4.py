"""
Nama : Nurul Aini
Nim : 221402005

soal 4 : Write a program that takes in grades one at a time until a -1 is seen to mark the end of the list.  
    Each grade will be separated by an enter key.  When you are done, output the average (as an int) 
    followed by the grades in order that you saw them.

"""

grades = []

while True:
    grade = input("Enter a grade (or -1 to finish): ")
    if grade == "-1":
        break
    else:
        grades.append(int(grade))

if grades:
    average = sum(grades) // len(grades)
    print(average)
    for grade in grades:
        print(grade)
else:
    print("No grades were entered.")
