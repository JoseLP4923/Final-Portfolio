#Jose Lopez
#12/2/2022

#problem_3: A function that takes a list and prints if the value 5 is in the list.

my_list = [13, 2, 4, 7,  8, 5, 10]

def is_value_in(chosen_num, list ):
    if chosen_num in list:
        if chosen_num == 5:
            print("The value 5 is in the list.")
        else:
            print("Your value is not 5!")
    else:
        print("Your value is not in the list!")

number_1 = int(input("What is your chosen number?\n"))

is_value_in(number_1, my_list)
