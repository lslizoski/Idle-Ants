from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from Incubator import Incubator
from FoodStorage import FoodStorage
from QueenUpgrades import QueenUpgrades
from GameInteractions.FoodGenerator import FoodGenerator
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.clock import Clock


class WindowManager(ScreenManager):
    pass

class Home(Screen):
    foodStorage = FoodStorage()
    queenUpgrades = QueenUpgrades(foodStorage)
    incubator = Incubator(queenUpgrades, foodStorage)
    foodGenerator = FoodGenerator()
    hatchClock = 1
    layClock = 1

    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        ant = Image(source="images/ant.png")

        # Add the image to the layout
        ant.pos = (0, -100)
        self.add_widget(ant)
        anim = Animation(x=250, y=-410, duration=5) + Animation(x=500, duration=5) + Animation(y=-500, duration=0.1) + Animation(x=-500, y=-500, duration=0.1)
        anim.start(ant)
        Clock.schedule_interval(self.timers, 0.1)

    def timers(self, interval):
        self.updateCounters()
        if self.hatchClock - self.incubator.getHatchSpeed() >= 0:
            self.hatchEgg()
            self.hatchClock = 1
        if self.layClock - self.queenUpgrades.getEggLaySpeed() >= 0:
            self.layEgg()
            self.layClock = 1

        self.hatchClock += 0.1
        self.layClock += 0.1

    def start(self):
        Clock.unschedule(self.timers)
        Clock.schedule_interval(self.timers, 0.1)

    def stop(self):
        Clock.unschedule(self.timers)

    def updateCounters(self):
        self.ids.ant_count.text = str('Ants: ' + str(self.incubator.getAnts()))
        self.ids.food_count.text = str('Food: ' + str(self.foodStorage.getFood()) + '/' + str(self.foodStorage.getMaxFood()))
        self.ids.egg_count.text = str('Eggs: ' + str(self.queenUpgrades.getEggs()))

    def setAnt(self):
        self.incubator.setAnts(1)

    def layEgg(self):
        self.queenUpgrades.setEggs(self.queenUpgrades.getLayMultiTier())

    def hatchEgg(self):
        if self.queenUpgrades.getEggs() <= 0:
            pass
        else:
            self.incubator.setAnts(self.incubator.getHatchMultiTier())
            self.queenUpgrades.setEggs(0 - (self.queenUpgrades.getLayMultiTier()))
            self.foodStorage.addFood(self.foodGenerator.chooseFood() * self.foodStorage.getMultiplyTier())
            if self.queenUpgrades.getEggs() <= 0:
                self.queenUpgrades.setEggs(0)


class Menu(Screen):
    foodStorage = FoodStorage()
    queenUpgrades = QueenUpgrades(foodStorage)
    incubator = Incubator(queenUpgrades, foodStorage)

    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_interval(self.updateCounters, 0.1)

    def updateCounters(self, *args):
        self.ids.ant_count.text = str('Ants: ' + str(self.incubator.getAnts()))
        self.ids.food_count.text = str('Food: ' + str(self.foodStorage.getFood()) + '/' + str(self.foodStorage.getMaxFood()))
        self.ids.egg_count.text = str('Eggs: ' + str(self.queenUpgrades.getEggs()))


class Queen(Screen):
    foodStorage = FoodStorage()
    queenUpgrades = QueenUpgrades(foodStorage)
    incubator = Incubator(queenUpgrades, foodStorage)

    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_interval(self.updateCounters, 0.1)

    def queenEggSpeedUpgradeButton(self):
        self.queenUpgrades.upgradeEggLaySpeed()

    def queenMultiplierUpgradeButton(self):
        self.queenUpgrades.upgradeEggMultiplier()

    def updateCounters(self, *args):
        self.ids.ant_count.text = str('Ants: ' + str(self.incubator.getAnts()))
        self.ids.food_count.text = str('Food: ' + str(self.foodStorage.getFood()) + '/' + str(self.foodStorage.getMaxFood()))
        self.ids.egg_count.text = str('Eggs: ' + str(self.queenUpgrades.getEggs()))
        self.ids.speed_tier.text = str('TIER:' + str(self.queenUpgrades.getLaySpeedTier()))
        self.ids.speed_stage.text = str('STAGE:' + str(self.queenUpgrades.getLaySpeedTierStage()))
        self.ids.multi_tier.text = str('TIER:' + str(self.queenUpgrades.getLayMultiTier()))
        self.ids.multi_stage.text = str('STAGE:' + str(self.queenUpgrades.getLayMultiTierStage()))


class Storage(Screen):
    foodStorage = FoodStorage()
    queenUpgrades = QueenUpgrades(foodStorage)
    incubator = Incubator(queenUpgrades, foodStorage)
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_interval(self.updateCounters, 0.1)

    def foodUpgradeButton(self):
        if self.foodStorage.upgradeStorage(self.incubator.getAnts()):
            self.incubator.setAnts(-50)

    def foodMultiplyButton(self):
        if self.foodStorage.upgradeFoodMultiplier(self.incubator.getAnts()):
            self.incubator.setAnts(-100)

    def updateCounters(self, *args):
        self.ids.ant_count.text = str('Ants: ' + str(self.incubator.getAnts()))
        self.ids.food_count.text = str('Food: ' + str(self.foodStorage.getFood()) + '/' + str(self.foodStorage.getMaxFood()))
        self.ids.egg_count.text = str('Eggs: ' + str(self.queenUpgrades.getEggs()))
        self.ids.multi_tier.text = str('TIER:' + str(self.foodStorage.getMultiplyTier()))
        self.ids.multi_stage.text = str('STAGE:' + str(self.foodStorage.getMultiplyTierStage()))


class Incubator(Screen):
    foodStorage = FoodStorage()
    queenUpgrades = QueenUpgrades(foodStorage)
    incubator = Incubator(queenUpgrades, foodStorage)

    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_interval(self.updateCounters, 0.1)

    def incubatorMultiplierUpgradeButton(self):
        self.incubator.upgradeHatchMultiplier()

    def incubatorHatchSpeedUpgradeButton(self):
        self.incubator.upgradeHatchSpeed()

    def updateCounters(self, *args):
        self.ids.ant_count.text = str('Ants: ' + str(self.incubator.getAnts()))
        self.ids.food_count.text = str('Food: ' + str(self.foodStorage.getFood()) + '/' + str(self.foodStorage.getMaxFood()))
        self.ids.egg_count.text = str('Eggs: ' + str(self.queenUpgrades.getEggs()))
        self.ids.speed_tier.text = str('TIER:' + str(self.incubator.getHatchSpeedTier()))
        self.ids.speed_stage.text = str('STAGE:' + str(self.incubator.getHatchSpeedTierStage()))
        self.ids.multi_tier.text = str('TIER:' + str(self.incubator.getHatchMultiTier()))
        self.ids.multi_stage.text = str('STAGE:' + str(self.incubator.getHatchMultiTierStage()))


class ScreenApp(App):
    def build(self):
        return


# run the app
ScreenApp().run()
