#Jose Lopez
#11/29/2022

#Problem 4: A function that takes a list of numbers and returns a new list.
import random

my_list = []

for numbers in range(1,11):
    my_list.append(random.randint(1,5))
print(my_list)

def UniqueList(List_of_Numbers):
    UniqueList = []
    for num in List_of_Numbers:
        if num in UniqueList:
            continue
        else:
            UniqueList.append(num)
    return UniqueList

print(UniqueList(my_list))



