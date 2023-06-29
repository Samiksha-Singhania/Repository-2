from math import pow , sqrt
from random import randint , shuffle , choice

result_1 = pow(2,4)
print("Result_1 is ", result_1)

result_2 = sqrt(16)
print("Result_2 is ", result_2)

result_3 = randint(0,100)
print("Result_3 is ", result_3)

names = ["Sarah", "Holley", "Ellena", "Emily", "Lily", "Mary" ]
print("Original names: ", names)

shuffle(names)
print("Names after shuffling ", names)

result_4 = choice(names)
print("Chosen name is ", result_4)