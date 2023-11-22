import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from Incubator import Incubator
from FoodStorage import FoodStorage
from QueenUpgrades import QueenUpgrades
from GameInteractions.FoodGenerator import FoodGenerator
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.clock import Clock
from random import randint


class WindowManager(ScreenManager):
    pass


class Home(Screen):
    foodStorage = FoodStorage()
    queenUpgrades = QueenUpgrades(foodStorage)
    incubator = Incubator(queenUpgrades, foodStorage)
    foodGenerator = FoodGenerator()
    hatchClock = 0
    layClock = 0

    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        Clock.schedule_interval(self.timers, 0.1)

    def ant_leave_animation(self, *args):
        ant = Image(source="images/ant.png")
        ant.pos = (50, -140)
        self.add_widget(ant)
        anim = (Animation(x=250, y=-410, duration=5) +
                Animation(x=500, duration=5))
        anim.bind(on_complete=lambda *args : self.remove_widget(ant))
        anim.bind(on_complete=self.ant_return_animation)
        anim.start(ant)

    def ant_return_animation(self, *args):
        food_type = randint(1, 3)
        if food_type == 1:
            ant = Image(source="images/AntLeaf.png")
        elif food_type == 2:
            ant = Image(source="images/AntBread.png")
        elif food_type == 3:
            ant = Image(source="images/AntSugar.png")
        ant.pos = (-500, -410)
        self.add_widget(ant)
        anim = (Animation(x=-250, y=-410, duration=5) +
                Animation(x=-50, y=-160, duration=5))
        anim.bind(on_complete=lambda *args: self.remove_widget(ant))
        anim.bind(on_complete=lambda *args: self.foodStorage.addFood(food_type * self.foodStorage.getMultiplyTier()))
        anim.start(ant)

    def timers(self, interval):
        self.updateCounters()
        if self.hatchClock - self.incubator.getHatchSpeed() >= 0:
            self.hatchEgg()
            self.hatchClock = 0
        if self.layClock - self.queenUpgrades.getEggLaySpeed() >= 0:
            self.layEgg()
            self.layClock = 0
        if self.ids.ant_progress_bar.value >= self.incubator.getHatchSpeed():
            self.ids.ant_progress_bar.value = 0
        self.ids.ant_progress_bar.value += 0.1
        self.ids.ant_progress_bar.max = self.incubator.getHatchSpeed()
        self.hatchClock += 0.1
        if self.ids.egg_progress_bar.value >= self.queenUpgrades.getEggLaySpeed():
            self.ids.egg_progress_bar.value = 0
        self.ids.egg_progress_bar.value += 0.1
        self.ids.egg_progress_bar.max = self.queenUpgrades.getEggLaySpeed()
        self.layClock += 0.1

    def updateCounters(self):
        self.ids.ant_count.text = str('Ants: ' + str(self.incubator.getAnts()))
        self.ids.food_count.text = str('Food: ' + str(self.foodStorage.getFood()) + '/' + str(self.foodStorage.getMaxFood()))
        self.ids.egg_count.text = str('Eggs: ' + str(self.queenUpgrades.getEggs()))

    def setAnt(self):
        self.incubator.setAnts(1)
        if randint(0,10) == 3:
            self.foodStorage.addFood(1)

    def layEgg(self):
        self.queenUpgrades.setEggs(self.queenUpgrades.getLayMultiTier())

    def hatchEgg(self):
        if self.queenUpgrades.getEggs() <= 0:
            pass
        else:
            self.ant_leave_animation()
            self.incubator.setAnts(self.incubator.getHatchMultiTier())
            self.queenUpgrades.setEggs(0 - (self.queenUpgrades.getLayMultiTier()))
            if self.queenUpgrades.getEggs() <= 0:
                self.queenUpgrades.setEggs(0)


class Menu(Screen):
    foodStorage = FoodStorage()
    queenUpgrades = QueenUpgrades(foodStorage)
    incubator = Incubator(queenUpgrades, foodStorage)
    hatchClock = 0
    layClock = 0

    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_interval(self.updateCounters, 0.1)

    def updateCounters(self, *args):
        self.ids.ant_count.text = str('Ants: ' + str(self.incubator.getAnts()))
        self.ids.food_count.text = str('Food: ' + str(self.foodStorage.getFood()) + '/' + str(self.foodStorage.getMaxFood()))
        self.ids.egg_count.text = str('Eggs: ' + str(self.queenUpgrades.getEggs()))
        if self.ids.ant_progress_bar.value >= self.incubator.getHatchSpeed():
            self.ids.ant_progress_bar.value = 0
        self.ids.ant_progress_bar.value += 0.1
        self.ids.ant_progress_bar.max = self.incubator.getHatchSpeed()
        self.hatchClock += 0.1
        if self.ids.egg_progress_bar.value >= self.queenUpgrades.getEggLaySpeed():
            self.ids.egg_progress_bar.value = 0
        self.ids.egg_progress_bar.value += 0.1
        self.ids.egg_progress_bar.max = self.queenUpgrades.getEggLaySpeed()
        self.layClock += 0.1

    def reset_stats(self):
        os.remove('FoodStorage.json')
        os.remove('Incubator.json')
        os.remove('QueenUpgrades.json')
        self.foodStorage.createFile()
        self.incubator.createFile()
        self.queenUpgrades.createFile()


class Queen(Screen):
    foodStorage = FoodStorage()
    queenUpgrades = QueenUpgrades(foodStorage)
    incubator = Incubator(queenUpgrades, foodStorage)
    hatchClock = 0
    layClock = 0

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
        if self.ids.ant_progress_bar.value >= self.incubator.getHatchSpeed():
            self.ids.ant_progress_bar.value = 0
        self.ids.ant_progress_bar.value += 0.1
        self.ids.ant_progress_bar.max = self.incubator.getHatchSpeed()
        self.hatchClock += 0.1
        if self.ids.egg_progress_bar.value >= self.queenUpgrades.getEggLaySpeed():
            self.ids.egg_progress_bar.value = 0
        self.ids.egg_progress_bar.value += 0.1
        self.ids.egg_progress_bar.max = self.queenUpgrades.getEggLaySpeed()
        self.layClock += 0.1


class Storage(Screen):
    foodStorage = FoodStorage()
    queenUpgrades = QueenUpgrades(foodStorage)
    incubator = Incubator(queenUpgrades, foodStorage)
    hatchClock = 0
    layClock = 0
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
        if self.ids.ant_progress_bar.value >= self.incubator.getHatchSpeed():
            self.ids.ant_progress_bar.value = 0
        self.ids.ant_progress_bar.value += 0.1
        self.ids.ant_progress_bar.max = self.incubator.getHatchSpeed()
        self.hatchClock += 0.1
        if self.ids.egg_progress_bar.value >= self.queenUpgrades.getEggLaySpeed():
            self.ids.egg_progress_bar.value = 0
        self.ids.egg_progress_bar.value += 0.1
        self.ids.egg_progress_bar.max = self.queenUpgrades.getEggLaySpeed()
        self.layClock += 0.1


class Incubator(Screen):
    foodStorage = FoodStorage()
    queenUpgrades = QueenUpgrades(foodStorage)
    incubator = Incubator(queenUpgrades, foodStorage)
    hatchClock = 0
    layClock = 0

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
        if self.ids.ant_progress_bar.value >= self.incubator.getHatchSpeed():
            self.ids.ant_progress_bar.value = 0
        self.ids.ant_progress_bar.value += 0.1
        self.ids.ant_progress_bar.max = self.incubator.getHatchSpeed()
        self.hatchClock += 0.1
        if self.ids.egg_progress_bar.value >= self.queenUpgrades.getEggLaySpeed():
            self.ids.egg_progress_bar.value = 0
        self.ids.egg_progress_bar.value += 0.1
        self.ids.egg_progress_bar.max = self.queenUpgrades.getEggLaySpeed()
        self.layClock += 0.1


class ScreenApp(App):
    def build(self):
        return


# run the app
ScreenApp().run()
