import pyautogui
import time
from helpers.create_delay import create_delay


def combat(times_ran):
    mouse_move = create_delay(0.25, 1, 2)
    run_delay = create_delay(14, 20, 2)
    wait_delay = create_delay(180, 240, 2)

    time.sleep(wait_delay)
    pyautogui.moveTo(1726, 67, duration=mouse_move, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(run_delay)
    pyautogui.moveTo(1724, 342, duration=mouse_move, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(run_delay)
    pyautogui.moveTo(952, 483, duration=mouse_move, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
