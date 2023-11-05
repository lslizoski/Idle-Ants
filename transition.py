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

    def updateCounters(self):
        self.ids.ant_count.text = str(self.antCount)
        self.ids.food_count.text = str(self.food_count)
        self.ids.egg_count.text = str(self.egg_count)

    def setAnt(self):
        self.incubator.setAnts(1)


class Menu(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)


class Queen(Screen):
    game = Game()
    queenUpgrades = QueenUpgrades()

    def queenEggSpeedUpgradeButton(self):
        self.queenUpgrades.upgradeEggLaySpeed()

    def queenMultiplierUpgradeButton(self):
        self.queenUpgrades.upgradeEggMultiplier()
        if self.game.sound:
            self.game.sound.volume = 1
            self.game.sound.play()

    def updateCounters(self):
        self.ids.speed_tier.text = str('TIER:' + str(self.queenUpgrades.getLaySpeedTier()))
        self.ids.speed_stage.text = str('STAGE:' + str(self.queenUpgrades.getLaySpeedTierStage()))
        self.ids.multi_tier.text = str('TIER:' + str(self.queenUpgrades.getLayMultiTier()))
        self.ids.multi_stage.text = str('STAGE:' + str(self.queenUpgrades.getLayMultiTierStage()))

class Incubator(Screen):
    incubator = Incubator()

    def __init__(self, **kw):
        super().__init__(**kw)

    def incubatorMultiplierUpgradeButton(self):
        self.incubator.upgradeHatchMultiplier()

    def incubatorHatchSpeedUpgradeButton(self):
        self.incubator.upgradeHatchSpeed()

    def updateCounters(self):
        self.ids.speed_tier.text = str('TIER:' + str(self.incubator.getHatchSpeedTier()))
        self.ids.speed_stage.text = str('STAGE:' + str(self.incubator.getHatchSpeedTierStage()))
        self.ids.multi_tier.text = str('TIER:' + str(self.incubator.getHatchMultiTier()))
        self.ids.multi_stage.text = str('STAGE:' + str(self.incubator.getHatchMultiTierStage()))


class Storage(Screen):
    foodStorage = FoodStorage()
    def foodUpgradeButton(self):
        self.foodStorage.upgradeStorage()


file = Builder.load_file('Screen.kv')


class ScreenApp(App):
    def build(self):
        return file


# run the app
ScreenApp().run()
