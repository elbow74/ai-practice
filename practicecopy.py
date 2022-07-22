from math import pow, sqrt

from random import randint, choice, shuffle

result_1 = pow(2, 4)
print("result_1 is ", result_1)

result_2 = sqrt(16)
print("result_2 is ", result_2)

result_3 = randint(0, 100)
print("result_3 is ", result_3)

names = ["amaryllis", "GOdson", "Emily", "Reina", "Derin", "ELena", "Enacio"]
print("Orignal names are ", names)

shuffle(names)
print("names after shuffle are ", names)

result_4 = choice(names)
print("Chosen name is: ", result_4)
