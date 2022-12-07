#Jose Lopez
#11/29/2022

#Problem 3: A function that multiplies all numbers in a list and returns the final result.

import random
List_of_Numbers = []
for num in range(1,11):
    List_of_Numbers.append(random.randint(1,100))
print(List_of_Numbers)

def ListMultiplier(List):
    n = 1
    for num in List:
        n = n * num
    return n

print(ListMultiplier(List_of_Numbers))

