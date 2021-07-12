import pyautogui
import time
from helpers.create_delay import create_delay


def summoning():
    local_runs = 0
    ui_wait = create_delay(1.5, 2, 2)
    move_wait_summoning_room = create_delay(12.5, 15, 2)
    move_wait_bridge = create_delay(10, 15, 2)
    mouse_move = create_delay(0.75, 2.25, 2)
    summoning_wait = create_delay(1.25, 2.5, 2)
    if local_runs == 0:  # center the camera on north
        pyautogui.moveTo(1546, 73, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move to north button
        pyautogui.click()
        time.sleep(1)
    pyautogui.moveTo(907, 539, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move to bank stand
    pyautogui.click()
    time.sleep(ui_wait)  # wait for bank to open
    pyautogui.press("f8")
    time.sleep(ui_wait)  # wait for bank to close
    pyautogui.moveTo(1859, 238, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move to across bridge
    pyautogui.click()
    time.sleep(move_wait_bridge)
    pyautogui.moveTo(1823, 96, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move to summoning room
    pyautogui.click()
    time.sleep(move_wait_summoning_room)
    pyautogui.moveTo(1066, 552, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move to summoning stone
    pyautogui.click()
    time.sleep(ui_wait)  # wait for summoning UI to open
    pyautogui.press("space")
    time.sleep(summoning_wait)
    pyautogui.moveTo(1621, 360, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move back to bridge
    pyautogui.click()
    time.sleep(move_wait_summoning_room)
    pyautogui.moveTo(1601, 210, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move back to bank
    pyautogui.click()
    time.sleep(move_wait_bridge)
    local_runs += 1
