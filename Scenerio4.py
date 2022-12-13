#Jose Lopez
#12/12/2002

#This file will contain everything aboput Scenario 4

import MainCharacterAnalysis
import Scenerio5
import time
def scenario_four():
    MC = MainCharacterAnalysis.MainCharacter.name
    time.sleep(3)
    print("""As Rick heads towards Washington DC, he must make his was through the city to get to the White House where
there is a base for survivors. He ends up encountering survivors in the city.""")
    time.sleep(5)
    input("Press enter.\n")

    print("""At first he thought they were normal people who were just trying to survive but they were thieves, dangerous
people who were stealing other people's supplies and leaving them with nothing. He is soon noticed by this villainous
gang and he now must figure out a way to deal with them so that he can go on his way to the White House.""")
    time.sleep(5)
    input("Press enter.\n")
    while True:

        scenario4_choice = input("""There are a total of 7 armed men. He only has a few options:
a. Use his M136.
b. Keep on driving with the vehicle in hopes of losing them.""")

        if scenario4_choice.lower() == 'a':
            print(MC, "decides to use his M136 to defend himself against the 7 armed men. Sadly, this is an unfair situation.")
            time.sleep(5)
            print(MC, """couldnt defend himself against 7 armed men. He soon shot by one and than it follows up with
him getting shot 7 more times. He soon falls to the ground. Grasping for his life, knowing he would never make it
to the white house.""")
            time.sleep(5)
            input("Press enter.\n")
            print("Would you like to try again or exit?")
            exit_or_try = input("Type 'again' or 'exit'.\n")
            if exit_or_try == 'again':
                continue
            elif exit_or_try == 'exit':
                time.sleep(2)
                print("Game will shut down.")
                exit()
            else:
                print("Wrong input.")

        elif scenario4_choice.lower() == 'b':
            print(MC, """decides to keep on driving the vehicle in hopes of losing them. His vehicle is shot multiple times
but he is able to escape without being hurt.""")
            time.sleep(5)
            print("He is able to lose them and proceeds to drive towards the White House in hopes of safety.")
            input("Press enter.\n")
            if scenario4_choice == 'b':
                Scenerio5.scenario_five()
        else:
            print("Wrong input. Only input 'a' or 'b'.")





