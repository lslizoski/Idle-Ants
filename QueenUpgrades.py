from kivy.storage.jsonstore import JsonStore
import os.path

class QueenUpgrades:

    queenUpgradesFile = JsonStore('QueenUpgrades.json')
    eggLayTime = 60
    eggMultiplier = 1
    upgradePercentage = 0.025

    eggLayTimeTier = 1
    eggLayTimeTierStage = 0
    eggMultiplierTier = 1
    eggMultiplierTierStage = 0

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
        self.eggLayTimeTier = self.queenUpgradesFile.get('eggLayTime')['eggLayTimeTier']
        self.eggLayTimeTierStage = self.queenUpgradesFile.get('eggLayTime')['eggLayTimeTierStage']

        self.eggMultiplier = self.queenUpgradesFile.get('eggMultiplier')['value']
        self.eggMultiplierTier = self.queenUpgradesFile.get('eggMultiplier')['eggMultiplierTier']
        self.eggMultiplierTierStage = self.queenUpgradesFile.get('eggMultiplier')['eggMultiplierTierStage']

    def setDefaultVariables(self):
        self.queenUpgradesFile.put('eggLayTime', value=self.eggLayTime, eggLayTimeTier=self.eggLayTimeTier, eggLayTimeTierStage=self.eggLayTimeTierStage)
        self.queenUpgradesFile.put('eggMultiplier', value=self.eggMultiplier, eggMultiplierTier=self.eggMultiplierTier, eggMultiplierTierStage=self.eggMultiplierTierStage)

    def upgradeEggLayTime(self):
        self.eggLayTime -= self.eggLayTime * self.upgradePercentage
        if (self.eggLayTimeTierStage >= 5):
            self.eggLayTimeTier += 1
            self.eggLayTimeTierStage = 0
        else:
            self.eggLayTimeTierStage += 1

        self.eggLayTimeTierStage += 1
        self.queenUpgradesFile.put('eggLayTime', value=self.eggLayTime, eggLayTimeTier=self.eggLayTimeTier, eggLayTimeTierStage=self.eggLayTimeTierStage)

    def upgradeEggMultiplier(self):
        if self.eggLayTimeTier >= 2:
            self.eggMultiplier += 1
            self.queenUpgradesFile.put('eggMultiplier', value=self.eggMultiplier, eggMultiplierTier=self.eggMultiplierTier, eggMultiplierTierStage=self.eggMultiplierTierStage)
        else:
            print("Must be at least Tier II in eggLayTime")


queenUpgrades = QueenUpgrades()