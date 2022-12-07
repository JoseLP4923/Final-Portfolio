#Problem 4: A while loopthat intializes a counter at 0 and reaches 50 but appends any countr that is divisible by 10
#and places it in a new list called tens.

list = []
tens = []
x = 0
while x <= 50:
    list.append(x)
    x += 1
    if x % 10 == 0:
        tens.append(x)

print(list)
print(tens)

