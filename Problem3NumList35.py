#Jose Lopez
#12/6/2022

#A while loop that asks the user for an input and appends each number into a list that adds them together.

sum_list = []

x = 0

while x <100:
    num = int(input("Enter a number:"))
    sum_list.append(num)
    x = sum(sum_list)

print(sum_list)
print(x)







