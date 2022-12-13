# Jose Lopez
# 12/01/2022

# This file contains the main character class.
#created a class for my character
class MainCharacter:
    name = "Rick Grimes"
    HP = 100
    ATK_DMG = 5
    Inv = []
    SemiPistol = 40
    M136 = 30
    Knife = 10
    Apple = 5
    SemiPistolAmmo = 18
    M136_ammo = 150

#created a multiple method that returns a characteristic from the character class
def m136_ammo():
    return MainCharacter.M136_ammo


def semi_ammo():
    return MainCharacter.SemiPistolAmmo


def ricks_inv():
    return MainCharacter.Inv


def health_points():
    return MainCharacter.HP


def attack_damage():
    return MainCharacter.ATK_DMG


def semi_pistol():
    return MainCharacter.SemiPistol


def auto_m136():
    return MainCharacter.M136


def ricks_knife():
    return MainCharacter.Knife


def ricks_apple():
    return MainCharacter.Apple


# Created a class for the enemy: Zombie
class ZombieHP:
    HP = 100
    ATK_DMG = 50

#created a multiple method that returns a characteristic from the zombie class
def zombie_attack():
    return ZombieHP.ATK_DMG


def zombie_hp():
    return ZombieHP.HP


# created a function that will return a current new health if 'Rick Grimes' takes damage by a zombie.
def hp_lost(healthpoints, zomebieattack):
    current_health = healthpoints - zomebieattack
    return current_health

#created a function thatwill take an amount of bullets that were lost and subtracts it from the current amount for the semi pistol.
def semi_ammo_loss(amount_lost, current_amount):
    new_amount = current_amount - amount_lost
    return new_amount

#created a function thatwill take an amount of bullets that were lost and subtracts it from the current amount for the M136 pistol.
def m136_ammo_loss(amount_lost, current_amount):
    new_amount = current_amount - amount_lost
    return new_amount

#created a function that will take the Rick's inventory and adds items to it.
def add_to_inv(inventory, item):
    inventory.append(item)
    return inventory

