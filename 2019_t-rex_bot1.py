#importing libraries
from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *
#class coordinate
class coordinate():
    restart_btn = (960, 489)

#some functions
def restart():
    pyautogui.click(coordinate.restart_btn )

def jump():
    pyautogui.keyDown('space')                                                                                          lambda
def image_recognition():
    box =(760, 530, 850, 540)
    #box = (777, 517, 810, 534)
    image = ImageGrab.grab(box)  # takes a screen shot of the coordinates of the box
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()
def main():
    restart()
    #pyautogui.moveTo(793, 525)
    while True:
        if (image_recognition()!=1147):
            jump()
            #time.sleep(0.1)
            print(image_recognition())
main()
#start moving the box towards right as the time proceeds , starting from 500 or earlier

