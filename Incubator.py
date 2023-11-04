from kivy.storage.jsonstore import JsonStore
import os


class Incubator:

    # Open json file for incubator room
    incubatorUpgradesFile = JsonStore('Incubator.json')

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
        path = './Incubator.json'
        if not os.path.isfile(path):
            self.incubatorUpgradesFile.put('HatchMultiplier', value=self.hatchMultiplier, hatchMultiplierTier=self.hatchMultiplierTier, hatchMultiplierTierStage=self.hatchMultiplierTierStage)
            self.incubatorUpgradesFile.put('HatchSpeed', value=self.hatchSpeed, hatchSpeedTier=self.hatchSpeedTier, hatchSpeedTierStage=self.hatchSpeedTierStage)
            print('created')
        else:
            self.setInitialVariables()

    def upgradeHatchSpeed(self):
        if self.hatchSpeedTier == 2:
            self.increasePercent = 0.05
        if self.hatchSpeedTier == 3:
            self.increasePercent = 0.075
        if self.hatchSpeedTier == 4:
            self.increasePercent = 0.1
        if self.hatchSpeedTier == 5:
            self.increasePercent = 0.15
        self.hatchSpeed -= self.hatchSpeed * self.increasePercent
        self.incubatorUpgradesFile.put('HatchSpeed', value=self.hatchSpeed, hatchSpeedTier=self.hatchSpeedTier, hatchSpeedTierStage=self.hatchSpeedTierStage)

    def upgradeHatchMultiplier(self):
        if self.hatchMultiplierTier == 2:
            self.hatchMultiplierIncrease = 2
        if self.hatchMultiplierTier == 3:
            self.hatchMultiplierIncrease = 3
        if self.hatchMultiplierTier == 4:
            self.hatchMultiplierIncrease = 4
        if self.hatchMultiplierTier == 5:
            self.hatchMultiplierIncrease = 5
        self.hatchMultiplier += self.hatchMultiplierIncrease
        self.incubatorUpgradesFile.put('HatchMultiplier', value=self.hatchMultiplier, hatchMultiplierTier=self.hatchMultiplierTier, hatchMultiplierTierStage=self.hatchMultiplierTierStage)


incubator = Incubator()
incubator.upgradeHatchSpeed()
incubator.upgradeHatchMultiplier()
