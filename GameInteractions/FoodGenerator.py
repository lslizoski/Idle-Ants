import random
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout


class FoodGenerator:

    foodDict = {
        'breadCrumb': [1, 'breadCrumb.png'],
        'appleSlice': [2, 'appleSlice.png'],
        'sugarCube': [3, 'sugarCube.png']
    }

    def __init__(self):
        self.food = self.chooseFood()

    def chooseFood(self):
        food, value = random.choice(list(self.foodDict.items()))
        return value[1] # must return the filename of the selected food

class FoodDisplay(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        foodGenerator = FoodGenerator()
        image = Image(source=foodGenerator.food)
        layout.add_widget(image)
        return layout

FoodDisplay().run()

