import math as calculate

import random as unknown


result_1 = calculate.pow(2, 4)
print("result_1 is ", result_1)

result_2 = calculate.sqrt(16)
print("result_2 is ", result_2)

result_3 = unknown.randint(0, 100)
print("result_3 is ", result_3)

names = ["amaryllis", "GOdson", "Emily", "Reina", "Derin", "ELena", "Enacio"]
print("Orignal names are ", names)

unknown.shuffle(names)
print("names after shuffle are ", names)

result_4 = unknown.choice(names)
print("Chosen name is: ", result_4)
