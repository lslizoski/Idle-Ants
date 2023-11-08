from kivy.storage.jsonstore import JsonStore
from Promotions import Promotions
import os

class FoodStorage:

    # Open json file for incubator room and food storage
    storageUpgradesFile = JsonStore('FoodStorage.json')

    currentFoodUnits = 0
    maxFoodCapacity = 50
    foodMultiplier = 1
    foodMultiplierTier = 1
    foodMultiplierTierStage = 0

    def __init__(self):
        self.createFile()

    def createFile(self):
        path = 'FoodStorage.json'
        if not os.path.isfile(path):
            self.storageUpgradesFile.put('currentFoodUnits', value=self.currentFoodUnits)
            self.storageUpgradesFile.put('maxFoodCapacity', value=self.maxFoodCapacity)
            self.storageUpgradesFile.put('foodMultiplier', value=self.foodMultiplier, foodMultiplierTier=self.foodMultiplierTier, foodMultiplierTierStage=self.foodMultiplierTierStage)

    def loadSaveData(self):
        self.currentFoodUnits = self.storageUpgradesFile.get('currentFoodUnits')['value']
        self.maxFoodCapacity = self.storageUpgradesFile.get('maxFoodCapacity')['value']
        self.foodMultiplier = self.storageUpgradesFile.get('foodMultiplier')['value']
        self.foodMultiplierTier = self.storageUpgradesFile.get('foodMultiplier')['foodMultiplierTier']
        self.foodMultiplierTierStage = self.storageUpgradesFile.get('foodMultiplier')['foodMultiplierTierStage']

    def addFood(self, foodToAdd):
        self.currentFoodUnits = self.storageUpgradesFile.get('currentFoodUnits')['value']
        self.maxFoodCapacity = self.storageUpgradesFile.get('maxFoodCapacity')['value']
        if (self.currentFoodUnits + foodToAdd * self.foodMultiplier) >= self.maxFoodCapacity:
            self.currentFoodUnits = self.maxFoodCapacity
        else:
            self.currentFoodUnits += foodToAdd * self.foodMultiplier
        self.storageUpgradesFile.put('currentFoodUnits', value=self.currentFoodUnits)

    def upgradeStorage(self, ants):
        if (ants >= 50):
            self.maxFoodCapacity = self.storageUpgradesFile.get('maxFoodCapacity')['value']
            self.maxFoodCapacity += 50
            self.storageUpgradesFile.put('maxFoodCapacity', value=self.maxFoodCapacity)
            return True
        else:
            print("Not enough ant resources.")

    def upgradeFoodMultiplier(self, ants):
        if self.getMultiplyTier() == 3:
            print('Max Level Reached')
        elif (ants >= 100):
            self.foodMultiplierTier = self.storageUpgradesFile.get('foodMultiplier')['foodMultiplierTier']
            self.foodMultiplierTierStage = self.storageUpgradesFile.get('foodMultiplier')['foodMultiplierTierStage']
            self.foodMultiplierTier, self.foodMultiplierTierStage, self.foodMultiplier = Promotions().multiplier(self.foodMultiplierTier, self.foodMultiplierTierStage, self.foodMultiplier)
            self.storageUpgradesFile.put('foodMultiplier', value=self.foodMultiplier, foodMultiplierTier=self.foodMultiplierTier, foodMultiplierTierStage=self.foodMultiplierTierStage)
            return True
        else:
            print("Not enough food resources.")


    def getFood(self):
        return self.storageUpgradesFile.get('currentFoodUnits')['value']

    def getMaxFood(self):
        return self.storageUpgradesFile.get('maxFoodCapacity')['value']

    def getMultiplyTier(self):
        return self.storageUpgradesFile.get('foodMultiplier')['foodMultiplierTier']

    def getMultiplyTierStage(self):
        return self.storageUpgradesFile.get('foodMultiplier')['foodMultiplierTierStage']

    def getFoodMultiplier(self):
        return self.storageUpgradesFile.get('foodMultiplier')['value']