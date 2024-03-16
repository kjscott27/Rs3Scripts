import pyautogui
import time
from helpers.create_delay import create_delay


def mining(times_ran):
    mouse_move = create_delay(0.2, 1, 2)
    random_mining_wait1 = create_delay(15, 25, 2)
    random_mining_wait2 = create_delay(13, 22, 2)
    pyautogui.moveTo(919, 318, duration=mouse_move, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(random_mining_wait1)

    if times_ran % 5 == 0:
        pyautogui.press("c")

    pyautogui.moveTo(1141, 513, duration=mouse_move, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(random_mining_wait2)
