import pyautogui
import time
from helpers.create_delay import create_delay


def agility():
    # APE ATOLL COURSE, START FROM ENDING
    mouse_tween = create_delay(1, 2, 2)
    # OBSTACLE 1
    pyautogui.moveTo(1589, 440, duration=mouse_tween, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(10)

    mouse_tween = create_delay(1, 2, 2)
    # OBSTACLE 2
    pyautogui.moveTo(1014, 506, duration=mouse_tween, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(5)

    mouse_tween = create_delay(1, 2, 2)
    # OBSTACLE 3
    pyautogui.moveTo(992, 470, duration=mouse_tween, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(5)

    mouse_tween = create_delay(1, 2, 2)
    # OBSTACLE 4
    pyautogui.moveTo(1058, 528, duration=mouse_tween, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(5)

    mouse_tween = create_delay(1, 2, 2)
    # OBSTACLE 5
    pyautogui.moveTo(605, 313, duration=mouse_tween, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(7.5)

    mouse_tween = create_delay(1, 2, 2)
    # OBSTACLE 6
    pyautogui.moveTo(897, 660, duration=mouse_tween, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(15)
