import pyautogui
import time
from helpers.create_delay import create_delay


def herbing(times_ran):
    mouse_move = create_delay(1, 2, 2)
    pyautogui.moveTo(811, 419, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move to banker
    pyautogui.click()
    time.sleep(1.25)  # wait for bank menu open
    pyautogui.press("f7")
    time.sleep(1)  # wait for bank menu to close (this should be faster than open)
    pyautogui.moveTo(1637, 907, duration=mouse_move, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    pyautogui.moveTo(1678, 908, duration=mouse_move, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(1.25)  # wait for herb making window
    pyautogui.press("space")
    time.sleep(12.5)
