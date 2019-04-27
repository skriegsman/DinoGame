import random
import Constants
from Constants import consts

class GenericBot:
    distMisc = consts.distMisc
    fitness = 0

    def __init__(self):
        self.distMisc += random.randint(consts.initLowRange, consts.initHighRange)

    def mutate(self):
        self.distMisc += round(random.random(), 1)

    def printStats(self):
        print("distMisc = " + str(self.distMisc))

    def think(self, yLvl):
        raise NotImplementedError

class basicBot(GenericBot):
    def think(self, yLvl):
        pass

class geneticBot(GenericBot):
    def think(self, yLvl):
        if yLvl == 0: return 0 #No obs found
        elif yLvl == 1: return 1 #Low obstacle found, jump
        elif yLvl == 2: return 2 #mid obstacle found, duck
        else: return 0 #high obstacle found. ignore
