import pyautogui
import time
from helpers.create_delay import create_delay


def cooking():
    cook_wait = create_delay(70, 75, 2)
    pyautogui.moveTo(852, 760, duration=1.5, tween=pyautogui.easeInOutQuad)  # move to range
    pyautogui.click()
    time.sleep(3.5)  # wait for player walk to and open range
    pyautogui.press("space")
    time.sleep(cook_wait)
    pyautogui.moveTo(1021, 367, duration=1.5, tween=pyautogui.easeInOutQuad)  # move to banker
    pyautogui.click()
    time.sleep(3.5)  # wait for player walk to and open bank
    pyautogui.press("f10")
    time.sleep(1.5)
