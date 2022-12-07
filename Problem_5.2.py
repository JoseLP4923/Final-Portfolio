#Jose Lopez
#12/4/2022

#Problem 5: A function that checks with your game character has all the items they've picked out.

class Meal:
    def __elit__(self, supply, food, size):
        self.supply = supply
        self.food = food
        self.size = size

    def meal_requirements(self):
        return self.supply, self.food

    def size_requirement(self):
        return self.size

cooking_ingredients = Meal('Pan', 'Groceries', 'Small')
for meal in cooking_ingredients.meal_requirements():
    print("You require:", meal)
print("Your cannot be:", cooking_ingredients.size_requirement())
