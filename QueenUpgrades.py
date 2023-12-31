from kivy.storage.jsonstore import JsonStore
import os.path
from Promotions import Promotions
from kivy.core.audio import SoundLoader

class QueenUpgrades:

    queenUpgradesFile = JsonStore('QueenUpgrades.json')
    eggLaySpeed = 30
    eggMultiplier = 1
    upgradePercentage = 0.025

    eggLaySpeedTier = 1
    eggLaySpeedTierStage = 0
    eggMultiplierTier = 1
    eggMultiplierTierStage = 0

    eggCounter = 0
    sound = SoundLoader.load('Audio/FoodMunch.mp3')

    def __init__(self, foodStorage):
        self.createFile()
        self.loadSavedData()
        self.foodStorage = foodStorage

    def createFile(self):
        path = 'QueenUpgrades.json'
        fileExists = os.path.isfile(path)
        if not fileExists:
            self.setDefaultVariables()

    def loadSavedData(self):
        self.eggLaySpeed = self.queenUpgradesFile.get('eggLaySpeed')['value']
        self.eggLaySpeedTier = self.queenUpgradesFile.get('eggLaySpeed')['eggLaySpeedTier']
        self.eggLaySpeedTierStage = self.queenUpgradesFile.get('eggLaySpeed')['eggLaySpeedTierStage']

        self.eggMultiplier = self.queenUpgradesFile.get('eggMultiplier')['value']
        self.eggMultiplierTier = self.queenUpgradesFile.get('eggMultiplier')['eggMultiplierTier']
        self.eggMultiplierTierStage = self.queenUpgradesFile.get('eggMultiplier')['eggMultiplierTierStage']
        self.eggCounter = self.queenUpgradesFile.get('eggCounter')['value']

    def setDefaultVariables(self):
        self.eggLaySpeed = 30
        self.eggMultiplier = 1
        self.upgradePercentage = 0.025
        self.eggLaySpeedTier = 1
        self.eggLaySpeedTierStage = 0
        self.eggMultiplierTier = 1
        self.eggMultiplierTierStage = 0
        self.eggCounter = 0
        self.queenUpgradesFile.put('eggLaySpeed', value=self.eggLaySpeed, eggLaySpeedTier=self.eggLaySpeedTier, eggLaySpeedTierStage=self.eggLaySpeedTierStage)
        self.queenUpgradesFile.put('eggMultiplier', value=self.eggMultiplier, eggMultiplierTier=self.eggMultiplierTier, eggMultiplierTierStage=self.eggMultiplierTierStage)
        self.queenUpgradesFile.put('eggCounter', value=self.eggCounter)

    def upgradeEggLaySpeed(self):
        if self.getLaySpeedTier() == 5 and self.getLaySpeedTierStage() == 5:
            print('Max Level Reached')
        if (self.foodStorage.getFood() >= 50):
            self.foodStorage.addFood(-50)
            self.eggLaySpeed -= self.eggLaySpeed * self.upgradePercentage
            self.eggLaySpeedTier, self.eggLaySpeedTierStage, self.upgradePercentage = Promotions().percentage(self.eggLaySpeedTier, self.eggLaySpeedTierStage, self.upgradePercentage)
            self.queenUpgradesFile.put('eggLaySpeed', value=self.eggLaySpeed, eggLaySpeedTier=self.eggLaySpeedTier, eggLaySpeedTierStage=self.eggLaySpeedTierStage)
            self.sound.volume = 1
            self.sound.play()

        else:
            print("Not enough food resources.")

    def upgradeEggMultiplier(self):
        if self.getLayMultiTier() == 3:
            print('Max Level Reached')
        elif (self.foodStorage.getFood() >= 100):
            self.foodStorage.addFood(-100)
            self.eggMultiplierTier, self.eggMultiplierTierStage, self.eggMultiplier = Promotions().multiplier(self.eggMultiplierTier, self.eggMultiplierTierStage, self.eggMultiplier)
            self.queenUpgradesFile.put('eggMultiplier', value=self.eggMultiplier, eggMultiplierTier=self.eggMultiplierTier, eggMultiplierTierStage=self.eggMultiplierTierStage)
        else:
            print("Not enough food resources.")

    def getEggLaySpeed(self):
        return self.queenUpgradesFile.get('eggLaySpeed')['value']

    def addEggs(self, amount):
        self.eggCounter += amount
        self.queenUpgradesFile.put('eggCounter', value=self.eggCounter)

    def setEggs(self, amount):
        self.eggCounter = amount
        self.queenUpgradesFile.put('eggCounter', value=self.eggCounter)

    def getEggs(self):
        return self.queenUpgradesFile.get('eggCounter')['value']

    def getLaySpeedTier(self):
        return self.queenUpgradesFile.get('eggLaySpeed')['eggLaySpeedTier']

    def getLaySpeedTierStage(self):
        return self.queenUpgradesFile.get('eggLaySpeed')['eggLaySpeedTierStage']

    def getLayMultiTier(self):
        return self.queenUpgradesFile.get('eggMultiplier')['eggMultiplierTier']

    def getLayMultiTierStage(self):
        return self.queenUpgradesFile.get('eggMultiplier')['eggMultiplierTierStage']
