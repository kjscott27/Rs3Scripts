import pyautogui
import time
from helpers.create_delay import create_delay


def summoning(times_ran):
    ui_wait = create_delay(1.5, 2, 2)
    move_wait_summoning_room = create_delay(12.5, 15, 2)
    move_wait_bridge = create_delay(10, 15, 2)
    mouse_move = create_delay(0.75, 2.25, 2)
    summoning_wait = create_delay(1.25, 2.5, 2)
    if times_ran == 1:  # center the camera on north
        pyautogui.moveTo(1562, 81, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move to north button
        pyautogui.click()
        time.sleep(1)
    pyautogui.moveTo(908, 512, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move to bank stand
    pyautogui.click()
    time.sleep(ui_wait)  # wait for bank to open
    pyautogui.press("f8")
    time.sleep(ui_wait)  # wait for bank to close
    pyautogui.moveTo(1856, 220, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move to across bridge
    pyautogui.click()
    time.sleep(move_wait_bridge)
    pyautogui.moveTo(1820, 73, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move to summoning room
    pyautogui.click()
    time.sleep(move_wait_summoning_room)
    pyautogui.moveTo(1064, 496, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move to summoning stone
    pyautogui.click()
    time.sleep(ui_wait)  # wait for summoning UI to open
    pyautogui.press("space")
    time.sleep(summoning_wait)
    pyautogui.moveTo(1625, 335, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move back to bridge
    pyautogui.click()
    time.sleep(move_wait_summoning_room)
    pyautogui.moveTo(1595, 190, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move back to bank
    pyautogui.click()
    time.sleep(move_wait_bridge)
