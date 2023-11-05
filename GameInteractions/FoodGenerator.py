import random
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout


class FoodGenerator:

    foodDict = {
        'breadCrumb': [1],
        'appleSlice': [2],
        'sugarCube': [3]
    }

    def __init__(self):
        self.food = self.chooseFood()

    def chooseFood(self):
        food, value = random.choice(list(self.foodDict.items()))
        return value[0]

