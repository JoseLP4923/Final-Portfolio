#Jose Lopez
#12/3/2022

#Problem_2: A function that takes two user inputs and prints wether they are greater than, less than, or eqaul to 10.

input_1 = int(input("Choose a number between 1 and 10!\n"))
input_2 = int(input("choose a second number between 1 and 10!\n"))

def greater_less_equal(int1, int2):
    if int1 <= 10 and int2 <= 10:
        sum = int1 + int2
        if sum < 10:
            print("The sum of your numbers is less than 10.")
        elif sum > 10:
            print("The sum of your number is more than 10.")
        elif sum == 10:
            print("The sum of your number is equal to 10")
    else:
        print("Your numbers must both be below 10!")

greater_less_equal(input_1, input_2)