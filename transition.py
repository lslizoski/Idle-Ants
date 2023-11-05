from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from Incubator import Incubator
from FoodStorage import FoodStorage
from QueenUpgrades import QueenUpgrades
from Game import Game


class WindowManager(ScreenManager):
    pass


class MainWidget(Widget):
    pass


class Home(Screen):
    incubator = Incubator()
    foodStorage = FoodStorage()
    queenUpgrades = QueenUpgrades()

    antCount = incubator.getAnts()
    food_count = foodStorage.getFood()
    egg_count = queenUpgrades.getEggs()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(self.antCount)

    def updateCounters(self):
        self.ids.ant_count.text = str(self.antCount)
        self.ids.food_count.text = str(self.food_count)
        self.ids.egg_count.text = str(self.egg_count)


class Menu(Screen):
    pass


class Queen(Screen):
    game = Game()


class Incubator(Screen):
    incubator = Incubator()
    def incubatorMultiplierUpgradeButton(self):
        self.incubator.upgradeHatchMultiplier()


    def incubatorHatchSpeedUpgradeButton(self):
        self.incubator.upgradeHatchSpeed()


class Storage(Screen):
    def foodUpgradeButton(self):
        self.foodStorage.upgradeStorage()


file = Builder.load_file('Screen.kv')


class ScreenApp(App):
    def build(self):
        return file


# run the app
ScreenApp().run()
