from kivy.core.audio import SoundLoader
from Upgrades.Armory import Armory
from Upgrades.FoodStorage import FoodStorage
from Upgrades.Incubator import Incubator
from Upgrades.QueenUpgrades import QueenUpgrades

class Game:

    queenUpgrades = QueenUpgrades()
    incubator = Incubator()
    foodStorage = FoodStorage()
    armory = Armory()
    sound = SoundLoader.load('../Audio/FoodMunch.mp3')

    def __init__(self):
        self.queenMultiplierUpgradeButton()

    def foodUpgradeButton(self):
        self.foodStorage.upgradeStorage()

    def queenMultiplierUpgradeButton(self):
        self.queenUpgrades.upgradeEggMultiplier()
        if self.sound:
            print("Sound found at %s" % self.sound.source)
            print("Sound is %.3f seconds" % self.sound.length)
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