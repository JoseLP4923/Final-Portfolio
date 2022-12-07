#Jose Lopez
#12/4/2022

#Problem_4: a function that a year as a parameter and trutrns true if the year is leap day and false if its not.

def leap_year(year):
    if year % 100 == 0 and year % 400 == 0 or year % 4 == 0 and year % 100 !=0:
        print(True)
    else:
        print(False)

chosen_year = int(input("What year have you chosen?\n"))
leap_year(chosen_year)

