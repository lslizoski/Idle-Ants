from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore


class WindowManager(ScreenManager):
    incubatorUpgradesFile = JsonStore('Incubator.json')
    FoodUpgradesFile = JsonStore('FoodStorage.py')
    QueenUpgradesFile = JsonStore('QueenUpgrades.py')
    antCount = incubatorUpgradesFile.get('antCounter')['value']
    food_count = incubatorUpgradesFile.get('currentFoodUnits')['value']
    egg_count = incubatorUpgradesFile.get('eggCounter')['value']

    def __init__(self):
        print(self.antCount)

    def updateCounters(self):
        self.ids.ant_count = self.antCount
        self.ids.food_count = self.food_count
        self.ids.egg_count = self.egg_count


class MainWidget(Widget):
    pass


class Home(Screen):
    pass


class Menu(Screen):
    pass


class Incubator(Screen):
    pass


file = Builder.load_file('Screen.kv')
class ScreenApp(App):
    def build(self):
        return file


# run the app
ScreenApp().run()
