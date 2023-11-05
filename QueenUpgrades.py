from kivy.storage.jsonstore import JsonStore
import os.path
from Promotions import Promotions
from FoodStorage import FoodStorage

class QueenUpgrades:

    queenUpgradesFile = JsonStore('QueenUpgrades.json')
    eggLaySpeed = 60
    eggMultiplier = 1
    upgradePercentage = 0.025

    eggLaySpeedTier = 1
    eggLaySpeedTierStage = 0
    eggMultiplierTier = 1
    eggMultiplierTierStage = 0

    eggCounter = 0

    foodStorage = FoodStorage()

    def __init__(self):
        self.createFile()
        self.loadSavedData()

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
        self.queenUpgradesFile.put('eggLaySpeed', value=self.eggLaySpeed, eggLaySpeedTier=self.eggLaySpeedTier, eggLaySpeedTierStage=self.eggLaySpeedTierStage)
        self.queenUpgradesFile.put('eggMultiplier', value=self.eggMultiplier, eggMultiplierTier=self.eggMultiplierTier, eggMultiplierTierStage=self.eggMultiplierTierStage)
        self.queenUpgradesFile.put('eggCounter', value=self.eggCounter)

    def upgradeEggLaySpeed(self):
        print(self.eggLaySpeed * self.upgradePercentage)
        if (self.foodStorage.getFood() >= 50):
            self.foodStorage.addFood(self.foodStorage.getFood() - 50)
            self.eggLaySpeed -= self.eggLaySpeed * self.upgradePercentage
            self.eggLaySpeedTier, self.eggLaySpeedTierStage, self.upgradePercentage = Promotions().percentage(self.eggLaySpeedTier, self.eggLaySpeedTierStage, self.upgradePercentage)
            self.queenUpgradesFile.put('eggLaySpeed', value=self.eggLaySpeed, eggLaySpeedTier=self.eggLaySpeedTier, eggLaySpeedTierStage=self.eggLaySpeedTierStage)
        else:
            print("Not enough food resources.")

    def upgradeEggMultiplier(self):
        if (self.foodStorage.getFood() >= 100):
            self.foodStorage.addFood(self.foodStorage.getFood() - 100)
            self.eggMultiplier = self.eggMultiplierTier
            self.eggMultiplierTier, self.eggMultiplierTierStage, self.eggMultiplier = Promotions().multiplier(self.eggMultiplierTier, self.eggMultiplierTierStage, self.eggMultiplier)
            self.queenUpgradesFile.put('eggMultiplier', value=self.eggMultiplier, eggMultiplierTier=self.eggMultiplierTier, eggMultiplierTierStage=self.eggMultiplierTierStage)
        else:
            print("Not enough food resources.")

    def addEggs(self, amount):
        self.eggCounter += amount
        self.queenUpgradesFile.put('eggCounter', value=self.eggCounter)

    def getEggLaySpeed(self):
        return self.queenUpgradesFile.get('eggLaySpeed')['value']

    def setEggs(self, amount):
        self.eggCounter += amount
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

queen = QueenUpgrades()
queen.upgradeEggLaySpeed()