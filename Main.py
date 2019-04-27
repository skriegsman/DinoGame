import cv2
import Bots
import pytesseract
import pyautogui
import time
import numpy as np
from Constants import consts
from PIL import ImageGrab

def score():
    scoreImg = np.array(ImageGrab.grab(bbox=consts.scoreCoords))
    return pytesseract.image_to_string(scoreImg, config='--psm 1 --oem 1').lstrip("0")

def getObsInfo():
    screenOne = np.array(ImageGrab.grab(bbox=consts.gameCoords))
    screenTwo = cv2.cvtColor(screenOne, cv2.COLOR_BGR2GRAY)
    screenThree = cv2.GaussianBlur(screenTwo, (1,1), 0)
    _, screen = cv2.threshold(screenThree,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    return dist, yLvl

#Initial population of bots with random values
population = [] #list of bots that can be referenced by position
for botNum in range(consts.populationSize):
    population.append(Bots.geneticBot())

#value to store the current best bot for the next generations seed
bestBot = Bots.geneticBot()

for genNum in range(consts.numGenerations):
    for bot in population:
        move = bot.think(getObsInfo())
        if move == 1: #If the move is to jump
            pyautogui.press('up')
        else: #If the move is to duck
            pyautogui.press('down')

        if(obsDist <= consts.collisonBuffer): # checks for collison and ends cycle
            if score() > bestBot.fitness:
                bestBot = bot

    bestBot.mutate()
bestBot.printStats()

#https://github.com/zvodd/sendkeys-py-si
#https://pypi.org/project/SendKeys/
#https://stackoverflow.com/questions/4636887/how-to-send-simulated-keyboard-strokes-to-the-active-window-using-sendkeys
