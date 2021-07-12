import pyautogui
import time
from helpers.create_delay import create_delay


def fletching():
    wait = create_delay(50, 57.5, 2)  # when cutting bows
    wait2 = create_delay(19.5, 22.5, 2)  # when stringing bows
    ui_wait = create_delay(1.5, 2, 2)
    pyautogui.click()
    time.sleep(ui_wait)
    pyautogui.press("f10")
    time.sleep(ui_wait)
    pyautogui.press("4")
    time.sleep(ui_wait)
    pyautogui.press("space")
    time.sleep(wait2)
