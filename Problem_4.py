#Jose Lopez
#11/1/2022
#
#A program that prints 1 throught 50, and displays numbers divisible by 3, 5, or both.

for num in range(1, 51):
    if num % 3 == 0 and num % 5 ==0:
        print("Divisible by both")
    elif num % 3 == 0:
        print("Divisible by 3")
    elif num % 5 == 0:
        print("Divisible by 5")
    else:
        print(num)