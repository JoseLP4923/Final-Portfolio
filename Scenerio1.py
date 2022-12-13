#Jose Lopez
#12/01/2022

#Scenerio 1 start with rick waking up in his home.
#imported the Main character module and scenerio 2s scenerio 1 will call scenerio 2 in the end.
#Also impoirted the time module so that my code has some delay between functions and statements.
import MainCharacterAnalysis
import Scenerio2
import time

def Scenerio_One():

    #I assigned name, healthpoints, and attack damage from the class MainCharacter as variables in Scenerio 1.
    MC = MainCharacterAnalysis.MainCharacter.name
    HP = MainCharacterAnalysis.health_points()
    ATK_DMG = MainCharacterAnalysis.attack_damage()
    semi_pistol = MainCharacterAnalysis.semi_pistol()
    zombie_hp = MainCharacterAnalysis.zombie_hp()
    zombie_attack = MainCharacterAnalysis.zombie_attack()
    #Story will continue with Rick picking up supplies and adding them to his inventory.
    time.sleep(2)
    print("""Rick Grimes wakes up from his bed, he soon realizes that the world has gone into mayhem.
The world has been overrun by zombies and he realizes that he must now head to Washington DC
where he will hopefully be safe.""")
    #created a delay between
    time.sleep(10)#supposed to be 10
    input("Press enter.\n")
    print("""As he prepares for his voyage, Rick Grimes scouts his empty house for any supplies or
weapons that will keep him alive and safe until he reaches Washington DC.""")
    time.sleep(5)#supposed to be 5
    input("Press enter.\n")

    #user must enter yes or noin order to show Rick Grimes stats.
    print("Would you like to see " + MC + " stats?")
    while True:
        user_input = input("Type YES or NO?\n")
    #if the user enter any lowercase letters for the word yes or no, .upper() will capitalize them.
        if user_input.upper() == 'YES':
            time.sleep(3)
            print(MC + " stats:\nHP:", HP, "\nAttack Damage:", ATK_DMG)
            time.sleep(1)
            print("You will now proceed.")
            break
        elif user_input.upper() == 'NO':
            input("Please press enter.")
            break
        else:
            print("Wrong input.")

    time.sleep(2)

    print("""As Rick Grimes goes through his home, he is able to collect an apple. Apple has been added to inventory!""")
    time.sleep(3)
    input("Press enter.\n")

#When Rick Grimes picks up an apple, till be added to the inventory function located in the MainCharacterAnalysis file.
    MainCharacterAnalysis.add_to_inv(MainCharacterAnalysis.ricks_inv(), "Apple")
    time.sleep(2)
    print("""He finds his personal .380 caliber semiautomatic pistol and a box of .388 ammo.
0.380 caliber semiautomatic pistol and ammo has been added to inventory.""")

    MainCharacterAnalysis.add_to_inv(MainCharacterAnalysis.ricks_inv(), ".388 Ammo")

    MainCharacterAnalysis.add_to_inv(MainCharacterAnalysis.ricks_inv(), ".380 Semi Pistol")
    time.sleep(5)
    input("Press enter.\n")
    time.sleep(2)
    print("He finds a knife and decides to leave.")
    time.sleep(3)
    input("Press enter.\n")
#This print statement will print the lsit while also adding the itme 'Knife' into the list.
    print(MC + " inventory: ", MainCharacterAnalysis.add_to_inv(MainCharacterAnalysis.ricks_inv(), "Knife"))
    time.sleep(2)
    input("Press enter.\n")
    time.sleep(3)
#assigned the user input to a varibale called scenerio1_choice.
    print(""""After collecting supplies, Rick Grimes starts his journey towards Washington DC.
As he is on his way, he suddenly encounters two zombies. Unfortunately, the 2 zombies also take notice of him
and Rick must figure out plan before he is consumed by them.""")

#if user inputs a capital A, B or C, lower.() will make sure it make the letter a lowercase letter.
    time.sleep(2)
    while True:
        scenerio1_choice = input("""Here are Rick Grimes' options:
a. Shoot each zombie.
b. You can run the opposite side.
c. You can use your knife to save some bullets.\n""")
        if scenerio1_choice.lower() == 'a':
            print("Rick decides to shoot each zombie with his semi pistol. Each Zombie has ", zombie_hp, "and does ",zombie_attack, ".")
            time.sleep(2)
            print(MC, "semi pistol does", semi_pistol, ",has a mag of 6 rounds, ands you have", MainCharacterAnalysis.semi_ammo(), "bullets in the ammo box.")
            time.sleep(2)
            print("He uses his semi pistol which results in killing each zombie with 6 bullets.")
            time.sleep(2)
            print("After taking out the two zombies you only have", MainCharacterAnalysis.semi_ammo_loss(6, MainCharacterAnalysis.semi_ammo()), "bullets left.")
            if scenerio1_choice == 'a':
                Scenerio2.Scenario_two()

        elif scenerio1_choice.lower() == 'b':
            time.sleep(2)
            print("""Rick decides to run away in the opposite direction. As he arrives back home, he realizes he's
made a mistake. His hometown, his own home has already been overrun a horde of zombies. Nearly 100 zombies
have already spotted and the ones that he previously ran away from are already behind him.""")
            time.sleep(2)
            print("Rick has come to the realization that it is over for him, and he is soon hoarded by the Walking dead.")
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

        elif scenerio1_choice.lower() == 'c':
            time.sleep(2)
            print("Rick decides to use his knife and save his bullets")
            time.sleep(3)
            print("Each Zombie has ", zombie_hp, "and does", zombie_attack, ".")
            time.sleep(3)
            print("Ricks knife does ", MainCharacterAnalysis.ricks_knife(), ". He is able to kill both zombies in the end.")
            time.sleep(3)
            print("Unfortunately, Rick gets bitten by one of the two zombies he fought")
            time.sleep(3)
            print("His current health went from 50 to ",MainCharacterAnalysis.hp_lost(HP, zombie_attack),". Sadly rick Grimes will die from this bite")
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

        else:
            print("Wrong input. Must input 'a', 'b', or 'c'.")

