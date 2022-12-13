#Jose Lopez
#12/12/202

#This file contains everything for file 5

import MainCharacterAnalysis
import time
def scenario_five():
    MC = MainCharacterAnalysis.MainCharacter.name

    print(MC, """finally arrives to the White House. As he slowly approaches the White House, he notices that
the fences that are keeping the zombies away are about to fall as the zombies try to break into the White House base.
Over the amount of zombies Rick sees a sliver of hope. Multiple helicopters are flying in and out with survivors
before the zombies overrun the base. He sees one more helicopter that is about to leave and that's his only chance
for survival.""")
    time.sleep(10)
    input("Press enter.\n")
    while True:

        scenario5_choice = input("""Rick Grimes only has two options that will lead him to survival or death. His options are:
a. Rick cna fight the horde until the very end.
b. Rick can crash the car into the fence.""")

        if scenario5_choice.lower() == 'a':
            print("""Rick decides to fight the horde until his last dying breath. He believed he would be
able to do something against The Walking Dead, but he was mistaken. There were too many of them. Sadly, he saw
the helicopter depart before he could even get on it. His last string of hope. Just gone. In an instant.
# He fell into despair as th horde had overrun him. He was soon consumed by The Walking Dead. Never to be heard again.""")
            time.sleep(10)
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

        elif scenario5_choice.lower() == 'b':
            print(MC, """decides to crash the car into the fence. With the car crashing into the fence, it creates
a distraction for the horde to focus on. He quickly exits the vehicle and starts to run towards the helicopter.
Luckily, the pilot notices him and waits for him to board the helicopter. Soon the helicopter sytarts to fly upwards
and it soon leaves Washington DC. Rick sees how the horde finally break down the fences surrounding Washington DC.
It does not matter to him since he made it out alive.""")
            time.sleep(5)
            input("Press enter.\n")
            print("You have successfully completed the game!!!")
            time.sleep(2)
            print("Congratulations player, you have successfully lead", MC, "to safety.")
            time.sleep(2)
            print("Game is over. Shutting down.")

            exit()

        else:
            print("Wrong input. Only input 'a', or 'b'.")
