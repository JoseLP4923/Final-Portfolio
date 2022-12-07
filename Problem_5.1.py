#Jose Lopez
#12/4/2022

#Problem 5: A function that checks with your game character has all the items they've picked out.

class Climb:
    def __init__(self, gear,clothing, health, weaknesses):
        self.gear = gear
        self.clothing = clothing
        self.health = health
        self.weaknesses = weaknesses

    def full_gear(self):
        return self.gear, self.clothing, self.health

    def status_debuff(self):
        return self.weaknesses
player_gear = Climb('Rope', 'Coat', 'First Aid Kit', 'Slow')
for equipment in player_gear.full_gear():
    print("Gear that is needed:", equipment)
print("Your debuff is:", player_gear.status_debuff())
