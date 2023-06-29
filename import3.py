import math as Calculations
import random as Different

result_1 = Calculations.pow(2,4)
print("Result_1 is ", result_1)

result_2 = Calculations.sqrt(16)
print("Result_2 is ", result_2)

result_3 = Different.randint(0,100)
print("Result_3 is ", result_3)

names = ["Sarah", "Holley", "Ellena", "Emily", "Lily", "Mary" ]
print("Original names: ", names)

Different.shuffle(names)
print("Names after shuffling ", names)

result_4 = Different.choice(names)
print("Chosen name is ", result_4)