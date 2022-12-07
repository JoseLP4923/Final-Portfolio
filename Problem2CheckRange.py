#Jose Lopez
#11/29/2022

#Problem 2: A function that checks wether a number is between 1 and 10 and takes that number as a paramter
#and returns True or False if the number is or isnt within the number 1 and 10.

import random
print("""You will be assigned a random interger between 1 and 20! You will either get a 'True' statement if your number
is between 1 and 20 and a 'False' Statement if its any other number above 10!""""")
x = random.randint(1,20)
print("Your random number is", x)
def TrueorFalse(x):
    if 0 < x <= 10:
        return x == True
    elif 11 <= x < 20:
        return x == False
x = TrueorFalse(x)
print ("Your number is",x )

