from kivy.core.audio import SoundLoader
from Armory import Armory
from FoodStorage import FoodStorage
from Incubator import Incubator
from QueenUpgrades import QueenUpgrades

class Game:

    queenUpgrades = QueenUpgrades()
    incubator = Incubator()
    foodStorage = FoodStorage()
    armory = Armory()
    sound = SoundLoader.load('Audio/FoodMunch.mp3')

    def __init__(self):
        self.queenMultiplierUpgradeButton()

    def update(self):
        pass
    def layEgg(self):
        self.queenUpgrades.addEggs(self.queenUpgrades.eggMultiplier)

    def foodUpgradeButton(self):
        self.foodStorage.upgradeStorage()

    def queenMultiplierUpgradeButton(self):
        self.queenUpgrades.upgradeEggMultiplier()
        if self.sound:
            self.sound.volume = 1
            self.sound.play()

    def queenEggSpeedUpgradeButton(self):
        self.queenUpgrades.upgradeEggLaySpeed()

    def incubatorMultiplierUpgradeButton(self):
        self.incubator.upgradeHatchMultiplier()

    def incubatorHatchSpeedUpgradeButton(self):
        self.incubator.upgradeHatchSpeed()

    def armoryCarryMultiplierUpgradeButton(self):
        self.armory.upgradeCarryMultiplier()

    def armoryAntSpeedUpgradeButton(self):
        self.armory.upgradeAntSpeed()

    def getQueenUpgrades(self):
        return self.queenUpgrades

    def getIncubator(self):
        return self.incubator

    def getFoodStorage(self):
        return self.foodStorage

    def getArmory(self):
        return self.armory