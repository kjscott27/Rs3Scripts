import pyautogui
import time
from helpers.create_delay import create_delay

local_runs = 0


def mining(times_ran):
    random_mining_wait1 = create_delay(15, 25, 2)
    random_mining_wait2 = create_delay(13, 22, 2)
    pyautogui.moveTo(919, 388, duration=1.5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(random_mining_wait1)

    if times_ran % 5 == 0:
        pyautogui.press("c")

    pyautogui.moveTo(1141, 513, duration=1.5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(random_mining_wait2)
