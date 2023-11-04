from kivy.storage.jsonstore import JsonStore
import os.path

class QueenUpgrades:

    eggLayTime = 60
    doubleEgg = False
    queenUpgradesFile = JsonStore('QueenUpgrades.json')

    def __init__(self):
        self.createFile()
        self.setInitialVariables()

    def saveUpgrades(self):
        self.queenUpgradesFile.put('QueenUpgrades', eggLayTime=60, doubleEgg=False)

    def createFile(self):
        path = './QueenUpgradess.py'
        check_file = os.path.isfile(path)
        print(check_file)

    def setInitialVariables(self):
        #print(self.queenUpgradesFile.get('QueenUpgrades')['eggLayTime'])
        #self.queenUpgradesFile.put('QueenUpgrades', eggLayTime=60, doubleEgg=False)
        pass

#queenUpgrades = QueenUpgrades()