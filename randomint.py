#Jose Lopez
#11/08/2022

#Problem 2: uses the random.randrange module to print and odd interger between 0 and 100.

import random
for numbers in range(0,1):
    numbers = (random.randrange(0,101))
    if numbers % 2 == 0:
        print("Random generated integer was not odd.")
    else:
        print(numbers)

