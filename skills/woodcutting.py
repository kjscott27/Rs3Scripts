import pyautogui
import time
from helpers.create_delay import create_delay


def woodcutting():
    swing_sleep = create_delay(10.5, 15, 10)
    incense_delay = create_delay(33, 40, 10)

    pyautogui.click()
    time.sleep(swing_sleep)
    pyautogui.click()
    time.sleep(swing_sleep)
    pyautogui.click()
    time.sleep(swing_sleep)
    pyautogui.click()
    time.sleep(swing_sleep)
    pyautogui.click()
    time.sleep(swing_sleep)
    pyautogui.click()
    time.sleep(swing_sleep)
    pyautogui.click()
    time.sleep(swing_sleep)
    pyautogui.click()
    time.sleep(swing_sleep)
    pyautogui.click()
    time.sleep(swing_sleep)
    pyautogui.click()
    time.sleep(swing_sleep)
    pyautogui.press('3')
    time.sleep(1.25)
    pyautogui.press('space')
    time.sleep(incense_delay)
