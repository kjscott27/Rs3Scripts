import pyautogui
import time
from helpers.create_delay import create_delay


def click(times_ran):
    flick_wait = create_delay(25, 50, 2)
    click_wait = create_delay(0.75, 0.2, 2)

    time.sleep(flick_wait)
    pyautogui.click()
    time.sleep(click_wait)
    pyautogui.click()