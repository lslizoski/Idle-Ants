from kivy.storage.jsonstore import JsonStore
from Upgrades.Promotions import Promotions
import os


class Armory:

    # Open json file for incubator room
    incubatorUpgradesFile = JsonStore('C:/Users/pagel/OneDrive/Documents/GitHub/Idle-Ants/SavedData/Armory.json')

    # Ant Carry Weight multiplier
    carryMultiplierTier = 1
    carryMultiplierTierStage = 1
    carryMultiplier = 1
    carryMultiplierIncrease = 1

    # Ant speed
    antSpeedTier = 1
    antSpeedTierStage = 1
    antSpeed = 60
    increasePercent = 0.025


    def __init__(self):
        self.createFile()

    def setInitialVariables(self):
        # Hatch multiplier variables
        self.carryMultiplierTier = self.incubatorUpgradesFile.get('carryMultiplier')['carryMultiplierTier']
        self.carryMultiplierTierStage = self.incubatorUpgradesFile.get('carryMultiplier')['carryMultiplierTierStage']
        self.carryMultiplier = self.incubatorUpgradesFile.get('carryMultiplier')['value']

        # Hatch Speed Variables
        self.antSpeedTier = self.incubatorUpgradesFile.get('antSpeed')['antSpeedTier']
        self.antSpeedTierStage = self.incubatorUpgradesFile.get('antSpeed')['antSpeedTierStage']
        self.antSpeed = self.incubatorUpgradesFile.get('antSpeed')['value']

    def createFile(self):
        path = 'C:/Users/pagel/OneDrive/Documents/GitHub/Idle-Ants/SavedData/Armory.json'
        if not os.path.isfile(path):
            self.incubatorUpgradesFile.put('carryMultiplier', value=self.carryMultiplier, hatchMultiplierTier=self.carryMultiplierTier, hatchMultiplierTierStage=self.carryMultiplierTierStage)
            self.incubatorUpgradesFile.put('antSpeed', value=self.antSpeed, hatchSpeedTier=self.antSpeedTier, hatchSpeedTierStage=self.antSpeedTierStage)

        else:
            self.setInitialVariables()

    def upgradeAntSpeed(self):
        self.antSpeed -= self.antSpeed * self.increasePercent
        self.antSpeedTier, self.antSpeedTierStage, self.increasePercent = Promotions().percentage(self.antSpeedTier, self.antSpeedTierStage, self.increasePercent)
        self.incubatorUpgradesFile.put('HatchSpeed', value=self.antSpeed, hatchSpeedTier=self.antSpeedTier, hatchSpeedTierStage=self.antSpeedTierStage)

    def upgradeCarryMultiplier(self):
        self.carryMultiplier = self.carryMultiplierTier
        self.carryMultiplierTier, self.carryMultiplierTierStage, self.carryMultiplier = Promotions().multiplier(self.carryMultiplierTier, self.carryMultiplierTierStage, self.carryMultiplier)
        self.incubatorUpgradesFile.put('HatchMultiplier', value=self.carryMultiplier, hatchMultiplierTier=self.carryMultiplierTier, hatchMultiplierTierStage=self.carryMultiplierTierStage)


armory = Armory()
armory.upgradeCarryMultiplier()
armory.upgradeAntSpeed()
