from PIL import ImageGrab
from pyautogui import *
import time
class co_ordinates:
    def _init(self):
        print("this has all the co_ordinates of the buttons to be clicked")
    wifi_btn = (1785, 1059)
    wifi_sw  = (1495, 989)
    nwt_sett = (1532, 930)
    my_wifi = (505, 283)
    connect_btn = (921, 405)
    next_btn = (786, 515)
    cls_btn = (1890, 14)
    wifi_box = (1477, 952, 1575, 1016)


moveTo(co_ordinates.wifi_btn)
click()
time.sleep(1)

x = co_ordinates.wifi_box[2] - co_ordinates.wifi_box[0]
y = co_ordinates.wifi_box[3] - co_ordinates.wifi_box[1]
pix_num = x*y
print(pix_num)
image = ImageGrab.grab(co_ordinates.wifi_box)
pix_val = list(image.getdata())
red = 0
green = 0
blue = 0
for p in pix_val:
    for val in range(1):
        red+=p[0]
        green+=p[1]
        blue+=p[2]
avg_RBG = [red, green, blue]
if ((avg_RBG[2]>(avg_RBG[0])) | (avg_RBG[2]>(avg_RBG[1]))):
    moveTo(co_ordinates.nwt_sett)
    click()
    time.sleep(8)
else:
    moveTo(co_ordinates.wifi_sw)
    click()
    time.sleep(1)

moveTo(co_ordinates.nwt_sett)
click()
time.sleep(8)

moveTo(co_ordinates.my_wifi)
click()
time.sleep(1)

moveTo(co_ordinates.connect_btn)
click()
time.sleep(1)

typewrite('yasir74hc0', 0.25)

moveTo(co_ordinates.next_btn)
time.sleep(1)
click()
time.sleep(1)
click()

moveTo(co_ordinates.cls_btn)
time.sleep(1)
click()
print("you are now connected !")

