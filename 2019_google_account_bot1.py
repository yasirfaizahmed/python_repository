import pyautogui
import time
import random
class co_ordinates:

    def _init_(self):
        print("this class includes all the necessary co_ordinates of the buttons of a chrome tab at 100% zoom level")
    first_name = (613, 476)
    back_btn = (24, 61)
    ref_btn = (112, 64)

f_name = ['alex', 'adam', 'jeorge', 'david', 'jason', 'william', 'eminem', 'arnold', 'marshal', 'mathers']
s_name = ['jorgeo', 'will', 'gutta', 'durulo', 'lilpump', 'charlie', 'puth', 'khalifa', 'sia', 'pitbull']
passwords = ['7227545yfnfif', 'bullmastiff9348', 'mustang0000', '999992adfgadg000', 'zaqwsxcderf', 'ht83y4tv0u09u09ytty']
phone_number = '8867973546'

n = 20
for i in range(n):

    rand_num = random.randint(0, 99999)
    rand_str = str(rand_num)
    rand_f_name = random.randint(0, 9)
    rand_s_name = random.randint(0, 9)

    pyautogui.moveTo(co_ordinates.first_name)
    pyautogui.click()
    time.sleep(1)

    pyautogui.typewrite(f_name[rand_f_name], 0.25)
    pyautogui.keyDown('tab')
    time.sleep(1)

    pyautogui.typewrite(s_name[rand_s_name], 0.25)
    pyautogui.keyDown('tab')
    time.sleep(1)

    pyautogui.typewrite(f_name[rand_f_name] + s_name[rand_s_name] + rand_str, 0.25)
    rand_pass = random.randint(0, 5)

    pyautogui.keyDown('tab')
    time.sleep(1)

    pyautogui.keyDown('tab')
    pyautogui.typewrite(passwords[rand_pass], 0.25)
    pyautogui.keyDown('tab')
    pyautogui.typewrite(passwords[rand_pass], 0.25)
    pyautogui.keyDown('tab')
    time.sleep(1)
    pyautogui.keyDown('tab')
    time.sleep(1)
    pyautogui.keyDown('enter')
    time.sleep(7)

    pyautogui.typewrite(phone_number, 0.25)
    time.sleep(0.5)

    pyautogui.keyDown('enter')
    time.sleep(10)

    pyautogui.moveTo(co_ordinates.back_btn)
    pyautogui.click()
    time.sleep(10)
    pyautogui.moveTo(co_ordinates.ref_btn)
    pyautogui.click()
    time.sleep(10)
    print("loops done:", n)


