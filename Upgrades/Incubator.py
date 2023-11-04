from kivy.storage.jsonstore import JsonStore
from Promotions import Promotions
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

    antCounter = 0


    def __init__(self):
        self.createFile()

    def getSpeed(self):
        return str(self.hatchSpeed)

    def loadSaveData(self):
        # Hatch multiplier variables
        self.hatchMultiplierTier = self.incubatorUpgradesFile.get('hatchMultiplier')['hatchMultiplierTier']
        self.hatchMultiplierTierStage = self.incubatorUpgradesFile.get('hatchMultiplier')['hatchMultiplierTierStage']
        self.hatchMultiplier = self.incubatorUpgradesFile.get('hatchMultiplier')['value']

        # Hatch Speed Variables
        self.hatchSpeedTier = self.incubatorUpgradesFile.get('hatchSpeed')['hatchSpeedTier']
        self.hatchSpeedTierStage = self.incubatorUpgradesFile.get('hatchSpeed')['hatchSpeedTierStage']
        self.hatchSpeed = self.incubatorUpgradesFile.get('hatchSpeed')['value']

        self.antCounter = self.incubatorUpgradesFile.get('antCounter')['value']

    def createFile(self):
        path = 'Incubator.json'
        if not os.path.isfile(path):
            self.incubatorUpgradesFile.put('hatchMultiplier', value=self.hatchMultiplier, hatchMultiplierTier=self.hatchMultiplierTier, hatchMultiplierTierStage=self.hatchMultiplierTierStage)
            self.incubatorUpgradesFile.put('hatchSpeed', value=self.hatchSpeed, hatchSpeedTier=self.hatchSpeedTier, hatchSpeedTierStage=self.hatchSpeedTierStage)
            self.incubatorUpgradesFile.put('antCounter', value=self.antCounter)

        else:
            self.loadSaveData()

    def upgradeHatchSpeed(self):
        self.hatchSpeed -= self.hatchSpeed * self.increasePercent
        self.hatchSpeedTier, self.hatchSpeedTierStage, self.increasePercent = Promotions().percentage(self.hatchSpeedTier, self.hatchSpeedTierStage, self.increasePercent)
        self.incubatorUpgradesFile.put('HatchSpeed', value=self.hatchSpeed, hatchSpeedTier=self.hatchSpeedTier, hatchSpeedTierStage=self.hatchSpeedTierStage)

    def upgradeHatchMultiplier(self):
        self.hatchMultiplier = self.hatchMultiplierTier
        self.hatchMultiplierTier, self.hatchMultiplierTierStage, self.hatchMultiplier = Promotions().multiplier(self.hatchMultiplierTier, self.hatchMultiplierTierStage, self.hatchMultiplier)
        self.incubatorUpgradesFile.put('HatchMultiplier', value=self.hatchMultiplier, hatchMultiplierTier=self.hatchMultiplierTier, hatchMultiplierTierStage=self.hatchMultiplierTierStage)

    def addAnt(self, amount):
        self.antCounter += amount
        self.incubatorUpgradesFile.put('antCounter', value=self.antCounter)
        print(self.incubatorUpgradesFile.get('antCounter')['value'])