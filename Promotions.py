class Promotions:

    def __init__(self):
        pass

    def percentage(self, tier, tierStage, oldPercent):
        newPercent = oldPercent
        if tier == 1:
            newPercent = 0.025
            tierStage += 1
        if tier == 2:
            newPercent = 0.05
            tierStage += 1
        elif tier == 3:
            newPercent = 0.075
            tierStage += 1
        elif tier == 4:
            newPercent = 0.1
            tierStage += 1
        elif tier == 5 and tierStage < 5:
            newPercent = 0.15
            tierStage += 1
        if tierStage >= 5 and tier != 5:
            tier += 1
            tierStage = 0
        return tier, tierStage, newPercent

    def multiplier(self, tier, tierStage, oldMultiplier):
        newMultiplier = oldMultiplier
        if tier == 1:
            newMultiplier = 1
            tierStage += 1
        if tier == 2:
            newMultiplier = 0.05
            tierStage += 1
        elif tier == 3 and tierStage < 3:
            newMultiplier = 0.075
            tierStage += 1
        if tierStage >= 3 and tier != 3:
            tier += 1
            tierStage = 0
        return tier, tierStage, newMultiplier