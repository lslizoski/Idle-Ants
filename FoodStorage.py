from kivy.storage.jsonstore import JsonStore
from Promotions import Promotions
import os

class FoodStorage:

    # Open json file for incubator room
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
        # Hatch multiplier variables
        self.currentFoodUnits = self.storageUpgradesFile.get('currentFoodUnits')['value']
        self.maxFoodCapacity = self.storageUpgradesFile.get('maxFoodCapacity')['value']
        self.foodMultiplier = self.storageUpgradesFile.get('foodMultiplier')['value']
        self.foodMultiplierTier = self.storageUpgradesFile.get('foodMultiplier')['foodMultiplierTier']
        self.foodMultiplier = self.storageUpgradesFile.get('foodMultiplier')['foodMultiplierTierStage']

    def addFood(self, foodToAdd):
        self.currentFoodUnits = self.storageUpgradesFile.get('currentFoodUnits')['value']
        self.maxFoodCapacity = self.storageUpgradesFile.get('maxFoodCapacity')['value']
        if (self.currentFoodUnits + foodToAdd * self.foodMultiplier) >= self.maxFoodCapacity:
            self.currentFoodUnits = self.maxFoodCapacity
        else:
            self.currentFoodUnits += foodToAdd * self.foodMultiplier
        self.storageUpgradesFile.put('currentFoodUnits', value=self.currentFoodUnits)

    def upgradeStorage(self):
        incubatorUpgradesFile = JsonStore('Incubator.json')
        self.antCounter = incubatorUpgradesFile.get('antCounter')['value']
        if (self.antCounter >= 50):
            self.maxFoodCapacity += 50
            self.antCounter -= 50
            self.storageUpgradesFile.put('maxFoodCapacity', value=self.maxFoodCapacity)
            incubatorUpgradesFile.put('antCounter', value=self.antCounter)
        else:
            print("Not enough ant resources.")

    def upgradeFoodMultiplier(self):
        incubatorUpgradesFile = JsonStore('Incubator.json')
        self.antCounter = incubatorUpgradesFile.get('antCounter')['value']
        if (self.antCounter >= 50):
            self.antCounter -= 50
            incubatorUpgradesFile.put('antCounter', value=self.antCounter)
            self.foodMultiplier = self.foodMultiplierTier
            self.foodMultiplierTier, self.foodMultiplierTierStage, self.foodMultiplier = Promotions().multiplier(self.foodMultiplierTier, self.foodMultiplierTierStage, self.foodMultiplier)
            incubatorUpgradesFile.put('antCounter', value=self.antCounter)
            self.storageUpgradesFile.put('foodMultiplier', value=self.foodMultiplier, foodMultiplierTier=self.foodMultiplierTier, foodMultiplierTierStage=self.foodMultiplierTierStage)
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