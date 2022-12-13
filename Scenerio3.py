#Jose Lopez
#12/01/2022

#This file will contain everything for Scenerio 3.
import MainCharacterAnalysis
import Scenerio4
import time
def scenario_three():
    HP = MainCharacterAnalysis.health_points()
    zombie_attack = MainCharacterAnalysis.zombie_attack()
    MC = MainCharacterAnalysis.MainCharacter.name
    time.sleep(3)

    print("""As Rick heads towards Washington DC., he hadn't realized that the vehicle was low on fuel. The vehicle
soon starts to shut down because there is no fuel. Luckily, the vehicle ran out of fuel as it reaches a hospital.
He finds a new vehicle to take but he decides to to explore the hospital first to see if he can collect items or
or supplies. As he enters the hospital, many doors are either blocked off or locked from the outside. Rick doesn't
really find anything useful so he decides to leave the hospital. While being on the second floor, he hears a few noises
behind a blocked door. Due to his good conscious he believed there might have been people that were still alive.
He gets rid of the blockage and decides to open the doors. That was his biggest mistake. A horde of 10 zombies starts
to rush out of the doors and RIck is trapped in the hospital.""")
    time.sleep(10)
    input("Press enter.\n")
    print("In order to get to the car, Rick has to come up with a quick solution.")
    time.sleep(5)

    while True:

        scenario3_choice = input("""He only has a few options being:
a. Rick uses his m136.
b. Rick runs through the horde in an attempt to not waste ammo.
c. Rick decides to jump out through a window on the second floor.""")

        if scenario3_choice.lower() == 'a':
            print(MC, "decides to use his m136 to kill all 10 zombies.")
            time.sleep(3)
            print("He ends up using 40 bullets which leaves him with", MainCharacterAnalysis.m136_ammo_loss(40, MainCharacterAnalysis.m136_ammo()), "bullets left.")
            time.sleep(5)
            print("""After killing the zombies, he is able to escape death. he decides to hop on the car and
drives off to his journey.""")
            time.sleep(5)
            input("Press enter.\n")
            if scenario3_choice == 'a':
                Scenerio4.scenario_four()

        elif scenario3_choice.lower() == 'b':
            print("""Rick decides to take his chance and preserve his ammo. He charges at the horde of zombies but he
ends up getting bitten.""")
            time.sleep(5)
            print("His current health went from 50 to ", MainCharacterAnalysis.hp_lost(HP, zombie_attack), "That bite decided his fate. Death.")
            time.sleep(3)
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

        elif scenario3_choice.lower() == 'c':
            print("""Rick decides his best chance of survival is jumping through the window within the room next to him.
He decides to take the risk and jumps off a two story window. This jump sadly ends with Rick breaking both of
hia legs.""")
            time.sleep(5)
            input("Press enter.\n")
            print("""Rick's only survival is getting to the car, but he realizes he won't make it in time. Despair
overcomes his strive for survival and he loses hope that he will make it to Washington DC. Zombies take notice of him,
and Rick Grimes is slowly consumed by The Walking Dead.""")
            time.sleep(5)
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
        else:
            print("Wrong input. Only input 'a', 'b', or 'c'.")




