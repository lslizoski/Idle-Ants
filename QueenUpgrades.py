from kivy.storage.jsonstore import JsonStore
import os.path

class QueenUpgrades:

    queenUpgradesFile = JsonStore('QueenUpgrades.json')
    eggLayTime = 60
    eggMultiplier = 1
    upgradePercentage = 0.025
    tierOneCounter = 0
    tierTwoCounter = 0
    tierThreeCounter = 0

    def __init__(self):
        self.createFile()
        self.loadSavedData()

    def createFile(self):
        path = './QueenUpgrades.json'
        fileExists = os.path.isfile(path)
        if not fileExists:
            self.queenUpgradesFile = JsonStore('QueenUpgrades.json')
            self.setDefaultVariables()

    def loadSavedData(self):
        self.eggLayTime = self.queenUpgradesFile.get('eggLayTime')['value']

    def setDefaultVariables(self):
        self.queenUpgradesFile.put('eggLayTime', value=self.eggLayTime, eggMultiplier=self.eggMultiplier)
        self.queenUpgradesFile.put('eggMultiplier', value=self.eggMultiplier)

    def upgradeEggLayTime(self):
        self.eggLayTime -= self.eggLayTime * self.upgradePercentage
        self.queenUpgradesFile.put('eggLayTime', value=self.eggLayTime)
        print(self.eggLayTime)

    def upgradeEggMultiplier(self):
        pass


#queenUpgrades = QueenUpgrades()