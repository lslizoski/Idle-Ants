from kivy.storage.jsonstore import JsonStore
import os.path
from Upgrades.Promotions import Promotions

class QueenUpgrades:

    queenUpgradesFile = JsonStore('C:/Users/pagel/OneDrive/Documents/GitHub/Idle-Ants/SavedData/QueenUpgrades.json')
    eggLaySpeed = 60
    eggMultiplier = 1
    upgradePercentage = 0.025

    eggLaySpeedTier = 1
    eggLaySpeedTierStage = 0
    eggMultiplierTier = 1
    eggMultiplierTierStage = 0

    def __init__(self):
        self.createFile()
        self.loadSavedData()
        self.upgradeEggMultiplier()
        self.upgradeEggLaySpeed()

    def createFile(self):
        path = 'C:/Users/pagel/OneDrive/Documents/GitHub/Idle-Ants/SavedData/QueenUpgrades.json'
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

    def setDefaultVariables(self):
        self.queenUpgradesFile.put('eggLaySpeed', value=self.eggLaySpeed, eggLaySpeedTier=self.eggLaySpeedTier, eggLaySpeedTierStage=self.eggLaySpeedTierStage)
        self.queenUpgradesFile.put('eggMultiplier', value=self.eggMultiplier, eggMultiplierTier=self.eggMultiplierTier, eggMultiplierTierStage=self.eggMultiplierTierStage)

    def upgradeEggLaySpeed(self):
        self.eggLaySpeed -= self.eggLaySpeed * self.upgradePercentage
        self.eggLaySpeedTier, self.eggLaySpeedTierStage, self.upgradePercentage = Promotions().percentage(self.eggLaySpeedTier, self.eggLaySpeedTierStage, self.upgradePercentage)
        self.queenUpgradesFile.put('eggLaySpeed', value=self.eggLaySpeed, eggLaySpeedTier=self.eggLaySpeedTier, eggLaySpeedTierStage=self.eggLaySpeedTierStage)

    def upgradeEggMultiplier(self):
        self.eggMultiplier =  self.eggMultiplierTier
        self.eggMultiplierTier, self.eggMultiplierTierStage, self.eggMultiplier = Promotions().multiplier(self.eggMultiplierTier, self.eggMultiplierTierStage, self.eggMultiplier)
        self.queenUpgradesFile.put('eggMultiplier', value=self.eggMultiplier, eggMultiplierTier=self.eggMultiplierTier, eggMultiplierTierStage=self.eggMultiplierTierStage)

queenUpgrades = QueenUpgrades()