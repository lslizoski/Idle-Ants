from kivy.storage.jsonstore import JsonStore
from Promotions import Promotions
import os

class Incubator:

    # Open json file for incubator room
    incubatorUpgradesFile = JsonStore('../SavedData/Incubator.json')

    # Hatch multiplier
    hatchMultiplierTier = 1
    hatchMultiplierTierStage = 1
    hatchMultiplier = 1
    hatchMultiplierIncrease = 1

    # Hatch speed
    hatchSpeedTier = 1
    hatchSpeedTierStage = 1
    hatchSpeed = 60
    increasePercent = 0.025


    def __init__(self):
        self.createFile()

    def setInitialVariables(self):
        # Hatch multiplier variables
        self.hatchMultiplierTier = self.incubatorUpgradesFile.get('HatchMultiplier')['hatchMultiplierTier']
        self.hatchMultiplierTierStage = self.incubatorUpgradesFile.get('HatchMultiplier')['hatchMultiplierTierStage']
        self.hatchMultiplier = self.incubatorUpgradesFile.get('HatchMultiplier')['value']

        # Hatch Speed Variables
        self.hatchSpeedTier = self.incubatorUpgradesFile.get('HatchSpeed')['hatchSpeedTier']
        self.hatchSpeedTierStage = self.incubatorUpgradesFile.get('HatchSpeed')['hatchSpeedTierStage']
        self.hatchSpeed = self.incubatorUpgradesFile.get('HatchSpeed')['value']

    def createFile(self):
        path = '../SavedData/Incubator.json'
        if not os.path.isfile(path):
            self.incubatorUpgradesFile.put('HatchMultiplier', value=self.hatchMultiplier, hatchMultiplierTier=self.hatchMultiplierTier, hatchMultiplierTierStage=self.hatchMultiplierTierStage)
            self.incubatorUpgradesFile.put('HatchSpeed', value=self.hatchSpeed, hatchSpeedTier=self.hatchSpeedTier, hatchSpeedTierStage=self.hatchSpeedTierStage)
            print('created')
        else:
            self.setInitialVariables()

    def upgradeHatchSpeed(self):
        self.hatchSpeed -= self.hatchSpeed * self.increasePercent
        self.hatchSpeedTier, self.hatchSpeedTierStage, self.increasePercent = Promotions().percentage(self.hatchSpeedTier, self.hatchSpeedTierStage, self.increasePercent)
        self.incubatorUpgradesFile.put('HatchSpeed', value=self.hatchSpeed, hatchSpeedTier=self.hatchSpeedTier, hatchSpeedTierStage=self.hatchSpeedTierStage)

    def upgradeHatchMultiplier(self):
        self.hatchMultiplier = self.hatchMultiplierTier
        self.hatchMultiplierTier, self.hatchMultiplierTierStage, self.hatchMultiplier = Promotions().multiplier(self.hatchMultiplierTier, self.hatchMultiplierTierStage, self.hatchMultiplier)
        self.incubatorUpgradesFile.put('HatchMultiplier', value=self.hatchMultiplier, hatchMultiplierTier=self.hatchMultiplierTier, hatchMultiplierTierStage=self.hatchMultiplierTierStage)


incubator = Incubator()
