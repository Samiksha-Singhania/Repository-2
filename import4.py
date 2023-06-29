from math import pow as p , sqrt as s
from random import randint as r , shuffle as t, choice as c

result_1 = p(2,4)
print("Result_1 is ", result_1)

result_2 = s(16)
print("Result_2 is ", result_2)

result_3 = r(0,100)
print("Result_3 is ", result_3)

names = ["Sarah", "Holley", "Ellena", "Emily", "Lily", "Mary" ]
print("Original names: ", names)

t(names)
print("Names after shuffling ", names)

result_4 = c(names)
print("Chosen name is ", result_4)