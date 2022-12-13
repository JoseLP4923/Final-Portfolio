#Jose Lopez
#12/01/2022

#This is scenario 2 and it continues after scenario 1.
#imported the MainCharatcer module, Scenerio 3 and the time module.
import MainCharacterAnalysis
import Scenerio3
import time
def Scenario_two():
    #Created a few variables to that a method from a different module.
    MC = MainCharacterAnalysis.MainCharacter.name
    HP = MainCharacterAnalysis.health_points()
    zombie_attack = MainCharacterAnalysis.zombie_attack()
    zombie_hp = MainCharacterAnalysis.zombie_hp()
    pistol = MainCharacterAnalysis.semi_pistol()
    m136 = MainCharacterAnalysis.auto_m136()
    m136_ammo = MainCharacterAnalysis.m136_ammo()
    time.sleep(2)
    print("""After killing the two zombies, Rick Grimes heads on forward on his journey. On his way, he finds the
Country Sheriffs Office building where he worked at before the apocalypse. while exploring the office, he finds an M136
with a 5.56mm caliber ammo box containing 120 rounds.
M136 and 5.56mm amo box has been added to inventory!""")
    #Added the M136 into the inventory.
    MainCharacterAnalysis.add_to_inv(MainCharacterAnalysis.ricks_inv(), "M136")
    time.sleep(2)
    #Created a variable that asks the user if they want to see their inventory with a YES or NO.
    print("Would you like to see your inventory?")
    while True:

        choice_2 = input("Type 'YES' or 'NO'?\n")
        if choice_2 == "YES":
            time.sleep(2)
        #If user types yes or YES, it'll print the new inventorey list with the new 5.56mm Ammo in that list.
            print(MC, "new inventory: ",MainCharacterAnalysis.add_to_inv(MainCharacterAnalysis.ricks_inv(), "5.56mm Ammo"))
            time.sleep(2)
            print("You shall proceed.")
            break
        elif choice_2 == "NO":
        #If user types no or NO, it will just keep on going.
            time.sleep(2)
            print("You shall proceed.")
            break

        else:
            print("Wrong input")

    time.sleep(2)
    print("""To Rick's surprise, he finds a vehicle within the office building that is still functional
He decides he will use the vehicle to get to Washington DC, but once he turns the car a small
group of 3 zombies appear as they were alerted by the running car. From the direction that Rick was coming from, a
horde of hundreds of zombies is on their way to Rick. He must figure out to do before that horde arrives to his
location!""")
    time.sleep(10)
    input("Press enter.\n")
    while True:
    #created a variable that will take the users reponse.
        scenario2_choice = input("""These are Ricks choices:
a. Use his semi pistol to take out the 3 zombies.
b. Use the M136 to take out the zombie.
c. Use your own body force.""")


        if scenario2_choice.lower() == 'a':
        #If user types a, itll print the following print statements.
            time.sleep(2)
            print("Rick decides to use his pistol. Each zombie has", zombie_hp, "health, and the semi pistol does", pistol , ".")
            time.sleep(5)
        #Next print statement will print how many bullets Rick has for semi pistol.
            print("Rick uses a total of 9 bullets. His semi pistol only has", MainCharacterAnalysis.semi_ammo_loss(9, MainCharacterAnalysis.semi_ammo()), "bullets left.")
            time.sleep(5)
            print("""Rick is able to defend himself against the zombies, but due to him using his pistol, the horde
of zombies that were coking from the direction he coming from have arrived and swarmed the sheriffs office building.
he is unable to escape, and with no exit days pass with no food or water. Rick decides that his fate is sealed and
he gives into the horde. He is soon swarmed by the Walking Dead, never to be seen again.""")
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


        elif scenario2_choice.lower() == 'b':
            time.sleep(2)
        #If user chooses 'b', it'll print the zombie hp and how much damage the m136 does and how much ammo it has.
            print("Rick decides to use his M136 to defend himself. Each zombie has", zombie_hp, "and his M136 does", m136, "damage, and has", m136_ammo, "ammo.")
            time.sleep(5)
            input("Press enter.\n")
            print("""Rick manages to quickly kill the zombies and drives away as the horde of zombies reached
the office after he had left a few minutes ago.""")
            time.sleep(5)
            input("Press enter.\n")
        #next print statment will print how much ammo the m136 has left.
            print("Rick has", MainCharacterAnalysis.m136_ammo_loss(12, MainCharacterAnalysis.m136_ammo()), "ammo left")
            time.sleep(2)
            print("For now Rick is safe and he continues on his journey.")
            if scenario2_choice == 'b':
                # if user chooses 'b', scenario 3 will start.
                Scenerio3.scenario_three()

        elif scenario2_choice.lower() == 'c':
            time.sleep(2)
        #If user chooses 'c', itll print how much health Rick Grimes takes.
            print("""Rick decides to use his own strength and body to force the zombies out of his way.
As Rick tries this method, he realizes it was too late to back out. He ends up getting bitten by one of the
three zombies. A bite from a zombie is very fatal""")
            time.sleep(5)
            input("Press enter.\n")
            print("His current health went from 50 to ", MainCharacterAnalysis.hp_lost(HP, zombie_attack),". Sadly Rick Grimes will die from this bite")
            time.sleep(2)
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





