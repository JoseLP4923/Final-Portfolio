#Jose Lopez
#12/01/2022

#This is the main game file where all files and modules will be implemented.
import MainCharacterAnalysis
import Scenerio1
import time
MC = MainCharacterAnalysis.MainCharacter.name

print("""Welcome to The Walking Dead!!!\n
Designed by Jose Lopez!\n
All game rights are preserved by the creator and any copied code will be subject to a lawsuit!
\nThank You!!""")
time.sleep(4)
input("Press enter.\n")

time.sleep(2)

print("""Game Objective:\nSurvive multiple scenarios of endless zombie interactions and harsh survival situation. Waking
up from his bed in a world overrun by the undead, Rick Grimes, former Country Sheriff, must leave his home, gather
supplies and food, and head towards Washington DC, for there is refuge and safety. Throughout his journey, Rick Grimes
will face ferocious and mindless beings that will try to consume his very flesh and bones. In order to survive he must
move forward and collect supplies and weaponry on the chosen path he has taken. Due to the sudden apocalypse, supplies
are very limited and he must preserve and use his supplies wisely until he reaches Washington DC. The choices that he
makes will decide the path that he will take and ultimately, his life if he does not take the right decisions.\n""")
time.sleep(10)#supposed to be 10
input("Press enter.\n")


#created a while loop that allows the user access to play the game while ending the program if the user does not want to
#play the game after being asked 3 times to reconsider!
time.sleep(3)#Supposed to be 3


def StartGame():# created a function to call back later.

    print("Would you like to proceed with the game?")
    attempts = 0
    while True:

        user = input("Type YES or NO\n")
        if user.upper() == "YES":
            print("You will proceed," + MC + ".")  # The will proceed if the user types yes or YES.
            Scenerio1.Scenerio_One()
        elif user.upper() == "NO":
            attempts += 1
            if attempts  >= 3:
                print("You have entered 'NO' 3 times!")
                time.sleep(3)
                print("Program will shut down!")
                time.sleep(3)
                print("Not my Problem!")
                time.sleep(3)
                print("Bye Bye!")
                time.sleep(3)
                exit()
        else:
            print("Wrong input!")

print(StartGame())

#Once the user says types YES> Scenerio 1 will start!


