#Jose Lopez
#12/3/2022

#Problem_1: A function that takes two inputs and prints if they are true or false.

input1 = int(input("Choose a number between one and five!\n"))
input2 = int(input("Chose another number between one and five!\n"))

def equal_or_not(int1, int2):
    if int1 <= 5 and int2 <= 5:
        if int1 == int2:
            print("They are equal!")
        else:
            print("They are not equal!")
    else:
        print("Your input must be be between one and five!")

equal_or_not(input1, input2)