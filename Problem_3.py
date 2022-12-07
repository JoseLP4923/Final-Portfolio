#jose Lopez
#11/1/2022
#
#A program that asks the user for the length, fill color, and shape of their choosing through Loops.

import turtle
tom = turtle.Turtle()

shape = input("Would you like to draw a square or a triangle?\n" )
length = int(input("what si the length of your sides?\n" ))
color = input("What color would you like to fill in?\n" )

if shape == "triangle" :
    tom.fillcolor(color)
    tom.begin_fill()
    for num in range (3):
        tom.forward(length)
        tom.right(120)
    tom.end_fill()

if shape == "square" :
    tom.fillcolor(color)
    tom.begin_fill()
    for num in range (4):
        tom.forward(length)
        tom.right(90)
    tom.end_fill()
input()