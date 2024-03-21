"""
Nama : Nurul Aini
Nim : 221402005

Soal 1. Write a program that reads in a number and prints the date that number of days from now in this format: Saturday, February 06, 2021.

"""
import datetime

days = int(input("Enter the number of days: "))
date_from_now = datetime.datetime.now() + datetime.timedelta(days=days)
formatted_date = date_from_now.strftime("%A, %B %d, %Y")
print(formatted_date)