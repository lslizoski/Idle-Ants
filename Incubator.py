from kivy.storage.jsonstore import JsonStore
from Promotions import Promotions
import os
from kivy.core.audio import SoundLoader

class Incubator:

    def __init__(self, queenUpgrades, foodStorage):
        # Open json file for incubator room
        self.incubatorUpgradesFile = JsonStore('Incubator.json')

        self.hatchMultiplierTier = 1
        self.hatchMultiplierTierStage = 1
        self.hatchMultiplier = 1
        self.hatchMultiplierIncrease = 1

        self.hatchSpeedTier = 1
        self.hatchSpeedTierStage = 1
        self.hatchSpeed = 60
        self.increasePercent = 0.025

        self.antCounter = 0
        self.sound = SoundLoader.load('Audio/EggSqulech.mp3')
        self.queenUpgrades = queenUpgrades
        self.foodStorage = foodStorage
        self.createFile()

    def getHatchSpeed(self):
        return self.hatchSpeed

    def loadSaveData(self):
        # Hatch multiplier variables
        self.hatchMultiplierTier = self.incubatorUpgradesFile.get('hatchMultiplier')['hatchMultiplierTier']
        self.hatchMultiplierTierStage = self.incubatorUpgradesFile.get('hatchMultiplier')['hatchMultiplierTierStage']
        self.hatchMultiplier = self.incubatorUpgradesFile.get('hatchMultiplier')['value']

        # Hatch Speed Variables
        self.hatchSpeedTier = self.incubatorUpgradesFile.get('hatchSpeed')['hatchSpeedTier']
        self.hatchSpeedTierStage = self.incubatorUpgradesFile.get('hatchSpeed')['hatchSpeedTierStage']
        self.hatchSpeed = self.incubatorUpgradesFile.get('hatchSpeed')['value']

        self.antCounter = self.incubatorUpgradesFile.get('antCounter')['value']

    def createFile(self):
        path = 'Incubator.json'
        if not os.path.isfile(path):
            self.incubatorUpgradesFile.put('hatchMultiplier', value=self.hatchMultiplier, hatchMultiplierTier=self.hatchMultiplierTier, hatchMultiplierTierStage=self.hatchMultiplierTierStage)
            self.incubatorUpgradesFile.put('hatchSpeed', value=self.hatchSpeed, hatchSpeedTier=self.hatchSpeedTier, hatchSpeedTierStage=self.hatchSpeedTierStage)
            self.incubatorUpgradesFile.put('antCounter', value=self.antCounter)

        else:
            self.loadSaveData()

    def upgradeHatchSpeed(self):
        if self.getHatchSpeedTier() == 5 and self.getHatchSpeedTierStage() == 5:
            print('Max Level Reached')
        elif (self.foodStorage.getFood() >= 50):
            self.foodStorage.addFood(-50)
            self.hatchSpeed -= self.hatchSpeed * self.increasePercent
            self.hatchSpeedTier, self.hatchSpeedTierStage, self.increasePercent = Promotions().percentage(self.hatchSpeedTier, self.hatchSpeedTierStage, self.increasePercent)
            self.incubatorUpgradesFile.put('hatchSpeed', value=self.hatchSpeed, hatchSpeedTier=self.hatchSpeedTier, hatchSpeedTierStage=self.hatchSpeedTierStage)
        else:
            print("Not enough food resources.")

    def upgradeHatchMultiplier(self):
        if self.getHatchMultiTier() == 3:
            print('Max Level Reached')
        elif (self.foodStorage.getFood() >= 100):
            self.foodStorage.addFood(-100)
            self.hatchMultiplierTier, self.hatchMultiplierTierStage, self.hatchMultiplier = Promotions().multiplier(self.hatchMultiplierTier, self.hatchMultiplierTierStage, self.hatchMultiplier)
            self.incubatorUpgradesFile.put('hatchMultiplier', value=self.hatchMultiplier, hatchMultiplierTier=self.hatchMultiplierTier, hatchMultiplierTierStage=self.hatchMultiplierTierStage)
            self.sound.volume = 1
            self.sound.play()
        else:
            print("Not enough food resources.")

    def hatchEgg(self):
        self.queenUpgrades.setEggs(self.queenUpgrades.getEggs() - 1)
        self.setAnts(self.getAnts() + self.hatchMultiplier)

    def setAnts(self, addAmount):
        addAmount += self.incubatorUpgradesFile.get('antCounter')['value']
        self.incubatorUpgradesFile.put('antCounter', value=addAmount)

    def getAnts(self):
        return self.incubatorUpgradesFile.get('antCounter')['value']

    def getHatchSpeed(self):
        return self.incubatorUpgradesFile.get('hatchSpeed')['value']

    def getHatchSpeedTier(self):
        return self.incubatorUpgradesFile.get('hatchSpeed')['hatchSpeedTier']

    def getHatchSpeedTierStage(self):
        return self.incubatorUpgradesFile.get('hatchSpeed')['hatchSpeedTierStage']

    def getHatchMultiTier(self):
        return self.incubatorUpgradesFile.get('hatchMultiplier')['hatchMultiplierTier']

    def getHatchMultiTierStage(self):
        return self.incubatorUpgradesFile.get('hatchMultiplier')['hatchMultiplierTierStage']
