import pyautogui
import time
from helpers.create_delay import create_delay


def smithing():
    smith_delay = create_delay(45, 55, 2)
    heat_delay = create_delay(8, 12, 2)
    pyautogui.click()
    time.sleep(smith_delay)
    pyautogui.click()
    time.sleep(heat_delay)
