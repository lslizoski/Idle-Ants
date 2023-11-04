import random

class FoodGenerator:

    foodDict = {
        'breadCrumb': [1, 'breadCrumb.png'],
        'appleSlice': [2, 'appleSlice.png'],
        'sugarCube': [3, 'sugarCube.png']
    }

    def __init__(self):
        self.chooseFood()

    def chooseFood(self):
        food, value = random.choice(list(self.foodDict.items()))
        return food

foodGenerator = FoodGenerator()