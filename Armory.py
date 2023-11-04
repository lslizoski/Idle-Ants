from kivy.storage.jsonstore import JsonStore
from Promotions import Promotions
import os

class Armory:

    # Open json file for incubator room
    armoryUpgradesFile = JsonStore('Armory.json')

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
        self.carryMultiplierTier = self.armoryUpgradesFile.get('carryMultiplier')['carryMultiplierTier']
        self.carryMultiplierTierStage = self.armoryUpgradesFile.get('carryMultiplier')['carryMultiplierTierStage']
        self.carryMultiplier = self.armoryUpgradesFile.get('carryMultiplier')['value']

        # Hatch Speed Variables
        self.antSpeedTier = self.armoryUpgradesFile.get('antSpeed')['antSpeedTier']
        self.antSpeedTierStage = self.armoryUpgradesFile.get('antSpeed')['antSpeedTierStage']
        self.antSpeed = self.armoryUpgradesFile.get('antSpeed')['value']

    def createFile(self):
        path = 'Armory.json'
        if not os.path.isfile(path):
            self.armoryUpgradesFile.put('carryMultiplier', value=self.carryMultiplier, carryMultiplierTier=self.carryMultiplierTier, carryMultiplierTierStage=self.carryMultiplierTierStage)
            self.armoryUpgradesFile.put('antSpeed', value=self.antSpeed, antSpeedTier=self.antSpeedTier, antSpeedTierStage=self.antSpeedTierStage)

        else:
            self.setInitialVariables()

    def upgradeAntSpeed(self):
        self.antSpeed -= self.antSpeed * self.increasePercent
        self.antSpeedTier, self.antSpeedTierStage, self.increasePercent = Promotions().percentage(self.antSpeedTier, self.antSpeedTierStage, self.increasePercent)
        self.armoryUpgradesFile.put('HatchSpeed', value=self.antSpeed, hatchSpeedTier=self.antSpeedTier, hatchSpeedTierStage=self.antSpeedTierStage)

    def upgradeCarryMultiplier(self):
        self.carryMultiplier = self.carryMultiplierTier
        self.carryMultiplierTier, self.carryMultiplierTierStage, self.carryMultiplier = Promotions().multiplier(self.carryMultiplierTier, self.carryMultiplierTierStage, self.carryMultiplier)
        self.armoryUpgradesFile.put('HatchMultiplier', value=self.carryMultiplier, hatchMultiplierTier=self.carryMultiplierTier, hatchMultiplierTierStage=self.carryMultiplierTierStage)
