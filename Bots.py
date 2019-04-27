import random
import Constants
from Constants import consts

class GenericBot:
    distSingleLittle = consts.distSingleLittle
    distDoubleLittle = consts.distDoubleLittle
    distTripleLittle = consts.distTripleLittle
    distSingleLarge = consts.distSingleLarge
    distDoubleLarge = consts.distDoubleLarge
    distCluster = consts.distCluster
    distLowBird = consts.distLowBird
    distMidBird = consts.distMidBird
    distHighBird = consts.distHighBird
    distMisc = consts.distMisc
    fitness = 0

    def __init__(self):
        distSingleLittle += random.randint(consts.initLowRange, consts.initHighRange)
        distDoubleLittle += random.randint(consts.initLowRange, consts.initHighRange)
        distTripleLittle += random.randint(consts.initLowRange, consts.initHighRange)
        distSingleLarge += random.randint(consts.initLowRange, consts.initHighRange)
        distDoubleLarge += random.randint(consts.initLowRange, consts.initHighRange)
        distCluster += random.randint(consts.initLowRange, consts.initHighRange)
        distLowBird += random.randint(consts.initLowRange, consts.initHighRange)
        distMidBird += random.randint(consts.initLowRange, consts.initHighRange)
        distHighBird += random.randint(consts.initLowRange, consts.initHighRange)
        distMisc += random.randint(consts.initLowRange, consts.initHighRange)

    def mutate(self):
        distSingleLittle += round(random.random(), 1)
        distDoubleLittle += round(random.random(), 1)
        distTripleLittle += round(random.random(), 1)
        distSingleLarge += round(random.random(), 1)
        distDoubleLarge += round(random.random(), 1)
        distCluster += round(random.random(), 1)
        distLowBird += round(random.random(), 1)
        distMidBird += round(random.random(), 1)
        distHighBird += round(random.random(), 1)
        distMisc += round(random.random(), 1)

    def printStats(self):
        print("duckJumpPause = " )

    def think(self, dist, type):
        raise NotImplementedError

class basicBot(GenericBot):
    def think(self, dist, type):
        if dist <= self.distSingleLittle:
            return 1
        return 0

class geneticBot(GenericBot):
    def think(self, dist, type):
        if dist <= self.distSingleLittle:
            return 1
        return 0
