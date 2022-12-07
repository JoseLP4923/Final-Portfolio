#Jose Lopez
#11/25/2022

#Problem 5:A program that solves the Pythagorean theorem with two user inputs.

import math
print("You are going to solvd the Pythogorena theorem and you must enter the length of the two shortest sides on the triangle.")
a = float(input("What is the length of the first side?\n"))
b = float(input("What is the length of the second side?\n"))
c = math.pow(a,2) * math.pow(b,2)
print("The Pythagorean theorem of your triangle is:",math.sqrt(c),".")