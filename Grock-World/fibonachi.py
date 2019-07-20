
import random as rand



input = []
output = []

for i in range(0,10):
    input.append(rand.randint(0,10))

print (input)


while len(input)>0:
    a = input.pop(0)
    if a == 0:
        output.append(a)

