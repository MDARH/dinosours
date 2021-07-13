from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import time
from numpy import *

replaybtn = (640, 400)
dinosaur = (420, 420)


def restartGame():
    time.sleep(0.2)
    pyautogui.click(replaybtn)


def image_grab():
    box = (dinosaur[0]+55, dinosaur[1], dinosaur[0]+145, dinosaur[1]+5)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()
    # print(a)


def pressSpace():
    pyautogui.keyDown('space')


time.sleep(4)
restartGame()

while True:
    image_grab()
    if(image_grab() != 697):
        pressSpace()
        time.sleep(0.1)
