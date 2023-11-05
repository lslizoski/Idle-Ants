from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from Incubator import Incubator
from FoodStorage import FoodStorage
from QueenUpgrades import QueenUpgrades
from Game import Game
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.clock import Clock


class WindowManager(ScreenManager):
    pass


class MainWidget(Widget):
    pass


class Home(Screen):
    incubator = Incubator()
    foodStorage = FoodStorage()
    queenUpgrades = QueenUpgrades()
    game = Game()
    clock = 1

    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        ant = Image(source="images/ant.png")

        # Add the image to the layout
        ant.pos = (0, -100)
        self.add_widget(ant)
        anim = Animation(x=250, y=-410, duration=5) + Animation(x=500, duration=5) + Animation(y=-500, duration=0.1) + Animation(x=-500, y=-500, duration=0.1)
        anim.start(ant)
        Clock.schedule_interval(self.timers, 1)

    def timers(self, interval):
        if (self.clock % round(self.game.incubator.getHatchSpeed()) == 0):
            self.game.hatchEgg()
            print("Hatch")
        if (self.clock % round(self.game.queenUpgrades.getEggLaySpeed())) == 0:
            self.game.layEgg()
            print("Lay")
        self.clock += 1

    def start(self):
        Clock.unschedule(self.timers)
        Clock.schedule_interval(self.timers, 1)

    def stop(self):
        Clock.unschedule(self.timers)

    def updateCounters(self):
        self.ids.ant_count.text = str('Ants: ' + str(self.incubator.getAnts()))
        self.ids.food_count.text = str('Food: ' + str(self.foodStorage.getFood()) + '/' + str(self.foodStorage.getMaxFood()))
        self.ids.egg_count.text = str('Eggs: ' + str(self.queenUpgrades.getEggs()))

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
    game = Game()
    incubator = Incubator()

    def __init__(self, **kw):
        super().__init__(**kw)

    def incubatorMultiplierUpgradeButton(self):
        self.incubator.upgradeHatchMultiplier()
        if self.game.sound2:
            self.game.sound2.volume = 1
            self.game.sound2.play()

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

    def foodMultiplyButton(self):
        self.foodStorage.upgradeFoodMultiplier()

    def updateCounters(self):
        self.ids.multi_tier.text = str('TIER:' + str(self.foodStorage.getMultiplyTier()))
        self.ids.multi_stage.text = str('STAGE:' + str(self.foodStorage.getMultiplyTierStage()))


file = Builder.load_file('Screen.kv')


class ScreenApp(App):
    def build(self):
        return file


# run the app
ScreenApp().run()
