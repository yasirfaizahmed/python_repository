import pyautogui
import time
time.sleep(3)
#print(pyautogui.position())
pyautogui.moveTo(74, 595, 3, pyautogui.easeInOutQuad)
time.sleep(2)
print(pyautogui.position())
#pyautogui.moveTo(1439, 334, 2, pyautogui.easeInOutQuad)
pyautogui.click()