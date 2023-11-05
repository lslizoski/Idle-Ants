from kivy.storage.jsonstore import JsonStore
import os.path
from Promotions import Promotions

class FoodStorage:
    
    foodStorageFile = JsonStore('FoodStorage.json')
    currentFoodUnits = 0
    maxFoodCapacity  = 50
    previousMaxCapacity = 50
    foodMultiplier = 1

    foodMultiplierTier = 1
    foodMultiplierTierStage = 0

    incubatorUpgradesFile = JsonStore('Incubator.json')

    def __init__(self):
        self.createFile()
        self.loadSavedData()

    def createFile(self):
        path = 'FoodStorage.json'
        fileExists = os.path.isfile(path)
        if not fileExists:
            self.foodStorageFile = JsonStore('FoodStorage.json')
            self.setDefaultVariables()

    def loadSavedData(self):
        self.currentFoodUnits = self.foodStorageFile.get('currentFoodUnits')['value']
        self.maxFoodCapacity = self.foodStorageFile.get('maxFoodCapacity')['value']
        self.previousMaxCapacity = self.foodStorageFile.get('previousMaxCapacity')['value']

        self.foodMultiplier = self.foodStorageFile.get('foodMultiplier')['value']
        self.foodMultiplierTier = self.foodStorageFile.get('foodMultiplier')['foodMultiplierTier']
        self.foodMultiplierTierStage = self.foodStorageFile.get('foodMultiplier')['foodMultiplierTierStage']

    def setDefaultVariables(self):
        self.foodStorageFile.put('currentFoodUnits', value=self.currentFoodUnits)
        self.foodStorageFile.put('maxFoodCapacity', value=self.maxFoodCapacity)
        self.foodStorageFile.put('previousMaxCapacity', value=self.previousMaxCapacity)
        self.foodStorageFile.put('foodMultiplier', value=self.foodMultiplier, foodMultiplierTier=self.foodMultiplierTier, foodMultiplierTierStage=self.foodMultiplierTierStage)


    def addFood(self, foodToAdd):
        if (self.currentFoodUnits + foodToAdd * self.foodMultiplier) >= self.maxFoodCapacity:
            self.currentFoodUnits = self.maxFoodCapacity
        else:
            self.currentFoodUnits += foodToAdd * self.foodMultiplier
        self.foodStorageFile.put('currentFoodUnits', value=self.currentFoodUnits)

    def upgradeStorage(self):
        if (self.getAnts() >= 50):
            self.maxFoodCapacity += 50
            self.setAnts(self.getAnts() - 50)
            self.foodStorageFile.put('maxFoodCapacity', value=self.maxFoodCapacity)
            self.foodStorageFile.put('previousMaxCapacity', value=self.previousMaxCapacity)
        else:
            print("Not enough ant resources.")

    def upgradeFoodMultiplier(self):
        if (self.getAnts() >= 50):
            self.setAnts(self.getAnts() - 50)
            self.foodMultiplier =  self.foodMultiplierTier
            self.foodMultiplierTier, self.foodMultiplierTierStage, self.foodMultiplier = Promotions().multiplier(self.foodMultiplierTier, self.foodMultiplierTierStage, self.foodMultiplier)
            self.foodStorageFile.put('foodMultiplier', value=self.foodMultiplier, foodMultiplierTier=self.foodMultiplierTier, foodMultiplierTierStage=self.foodMultiplierTierStage)
        else:
            print("Not enough food resources.")

    def getAnts(self):
        return self.incubatorUpgradesFile.get('antCounter')['value']

    def setAnts(self, totalAmount):
        self.incubatorUpgradesFile.put('antCounter', value=totalAmount)

    def getFood(self):
        return self.foodStorageFile.get('currentFoodUnits')['value']

    def getMaxFood(self):
        return self.foodStorageFile.get('maxFoodCapacity')['value']

    def setFood(self, addAmount):
        self.currentFoodUnits += addAmount
        self.foodStorageFile.put('currentFoodUnits', value=self.currentFoodUnits)

    def getMultiplyTier(self):
        return self.foodStorageFile.get('foodMultiplier')['foodMultiplierTier']

    def getMultiplyTierStage(self):
        return self.foodStorageFile.get('foodMultiplier')['foodMultiplierTierStage']

    def getFoodMultiplier(self):
        return self.foodStorageFile.get('foodMultiplier')['value']