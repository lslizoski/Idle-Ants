from kivy.storage.jsonstore import JsonStore
import os.path
from Upgrades.Incubator import Incubator

class FoodStorage:
    
    foodStorageFile = JsonStore('FoodStorage.json')
    currentFoodUnits = 0
    maxFoodCapacity  = 50
    previousMaxCapacity = 50
    incubator = Incubator()
    
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

    def setDefaultVariables(self):
        self.foodStorageFile.put('currentFoodUnits', value=self.currentFoodUnits)
        self.foodStorageFile.put('maxFoodCapacity', value=self.maxFoodCapacity)
        self.foodStorageFile.put('previousMaxCapacity', value=self.previousMaxCapacity)

    def addFood(self, foodToAdd):
        if (self.currentFoodUnits + foodToAdd) >= self.maxFoodCapacity:
            self.currentFoodUnits = self.maxFoodCapacity
        else:
            self.currentFoodUnits += foodToAdd
        self.foodStorageFile.put('currentFoodUnits', value=self.currentFoodUnits)

    def upgradeStorage(self):
        if (self.incubator.getAnts() >= 50):
            self.maxFoodCapacity += 50
            self.incubator.setAnts(self.incubator.getAnts() - 50)
            self.foodStorageFile.put('maxFoodCapacity', value=self.maxFoodCapacity)
            self.foodStorageFile.put('previousMaxCapacity', value=self.previousMaxCapacity)
            print(self.incubator.getAnts())
        else:
            print("Not enough food resources")