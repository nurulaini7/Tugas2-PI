"""
Nama : Nurul Aini
Nim : 221402005

Soal 2. In this second part of the first programming assignment, you should write a program that reads in numbers until a -1 is entered and prints the sum of all numbers entered in decimal format with two digits after the decimal. 
For example, if the user enters 5000 10 15 -1 the program should display 5025.00 (Each number will be separated by a carriage return). 
"""

total = 0
while True:
    number = float(input())
    if number == -1:
        break
    total += number
    print(f"{number:.2f}")
print(f"The sum of all numbers is: {int(total)}")
