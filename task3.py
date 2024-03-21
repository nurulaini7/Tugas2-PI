"""
Nama : Nurul Aini
Nim : 221402005

soal 3 :  Write a class that calculates and stores the height and weight of a person in metric.

"""

class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def BMI_Value(self):
        return self.weight / (self.height**2)
    
height = 1.66
weight = 55

bmi = BMI(height, weight)
print("The BMI is", round(bmi.BMI_Value(), 2))