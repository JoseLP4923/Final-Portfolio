#Jose Lopez
#11/29/2022

#Problem 1: a function that returns the area of a cirle
import math
r = float(input("What is your radius?\n"))
pi = math.pi
def areaOfCircle(r):
    A = pi * r**2
    return A
A = areaOfCircle(r)
print("The area of a cirle is", A)



