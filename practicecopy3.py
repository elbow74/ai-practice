from math import pow as pw
from math import sqrt as srt

from random import choice as choose
from random import shuffle as change
from random import randint as random

result_1 = pw(2, 4)
print("result_1 is ", result_1)

result_2 = srt(16)
print("result_2 is ", result_2)

result_3 = random(0, 100)
print("result_3 is ", result_3)

names = ["amaryllis", "GOdson", "Emily", "Reina", "Derin", "ELena", "Enacio"]
print("Orignal names are ", names)

change(names)
print("names after shuffle are ", names)

result_4 = choose(names)
print("Chosen name is: ", result_4)
