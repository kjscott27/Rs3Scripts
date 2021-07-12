import pyautogui
import time
from helpers.create_delay import create_delay


def mining():
    local_runs = 0
    random_mining_wait1 = create_delay(5, 12, 2)
    random_mining_wait2 = create_delay(7.5, 15, 2)
    pyautogui.moveTo(1002, 412, duration=1.5, tween=pyautogui.easeInOutQuad)  # move to banker
    pyautogui.click()
    time.sleep(random_mining_wait1)

    if local_runs % 5 == 0:
        pyautogui.press("1")

    pyautogui.moveTo(850, 577, duration=1.5, tween=pyautogui.easeInOutQuad)  # move to banker
    pyautogui.click()
    time.sleep(random_mining_wait2)
    local_runs += 1
