#importing libraries
from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *
#class coordinate
class coordinate():
    restart_btn = (472, 509)
    dino_pnt = (200, 512)
    #x1 ,y1 = 286, 495
    #x2, y2 = 375, 559

#some functions
def restart():
    pyautogui.click(coordinate.restart_btn )
    time.sleep(0.5)
def jump():
    pyautogui.keyDown('space')
def image_recognition():
    box =(coordinate.dino_pnt[0]+115, coordinate.dino_pnt[1], coordinate.dino_pnt[0]+182, coordinate.dino_pnt[1]+34)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()
def main():
    restart()
    while True:
        if (image_recognition()!=5700):
            jump()
            #time.sleep(0.1)
            print(image_recognition())
main()

