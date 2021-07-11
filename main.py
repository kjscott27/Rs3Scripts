import pyautogui
import time
import helpers.create_delay

times_to_run = 5000  # set times to run
times_ran = 0  # times run
time.sleep(1.5)


def __main__():
    print('')


while times_ran < times_to_run:
    __main__()
    times_ran += 1
    print(times_ran)


# ACADIA TREE MENAPHOS
#     swing_sleep = create_delay(10.5, 15, 10)
#     incense_delay = create_delay(33, 40, 10)
#
#     pyautogui.click()
#     time.sleep(swing_sleep)
#     pyautogui.click()
#     time.sleep(swing_sleep)
#     pyautogui.click()
#     time.sleep(swing_sleep)
#     pyautogui.click()
#     time.sleep(swing_sleep)
#     pyautogui.click()
#     time.sleep(swing_sleep)
#     pyautogui.click()
#     time.sleep(swing_sleep)
#     pyautogui.click()
#     time.sleep(swing_sleep)
#     pyautogui.click()
#     time.sleep(swing_sleep)
#     pyautogui.click()
#     time.sleep(swing_sleep)
#     pyautogui.click()
#     time.sleep(swing_sleep)
#     pyautogui.press('3')
#     time.sleep(1.25)
#     pyautogui.press('space')
#     time.sleep(incense_delay)

# SUMMONING TRAINING
#     ui_wait = create_delay(1.5, 2, 2)
#     move_wait_summoning_room = create_delay(12.5, 15, 2)
#     move_wait_bridge = create_delay(10, 15, 2)
#     mouse_move = create_delay(0.75, 2.25, 2)
#     summoning_wait = create_delay(1.25, 2.5, 2)
#     if times_ran == 0:
#         pyautogui.moveTo(1546, 73, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move to north button
#         pyautogui.click()
#         time.sleep(1)
#     pyautogui.moveTo(907, 539, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move to bank stand
#     pyautogui.click()
#     time.sleep(ui_wait)  # wait for bank to open
#     pyautogui.press('f8')
#     time.sleep(ui_wait)  # wait for bank to close
#     pyautogui.moveTo(1859, 238, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move to across bridge
#     pyautogui.click()
#     time.sleep(move_wait_bridge)
#     pyautogui.moveTo(1823, 96, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move to summoning room
#     pyautogui.click()
#     time.sleep(move_wait_summoning_room)
#     pyautogui.moveTo(1066, 552, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move to summoning stone
#     pyautogui.click()
#     time.sleep(ui_wait)  # wait for summoning UI to open
#     pyautogui.press('space')
#     time.sleep(summoning_wait)
#     pyautogui.moveTo(1621, 360, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move back to bridge
#     pyautogui.click()
#     time.sleep(move_wait_summoning_room)
#     pyautogui.moveTo(1601, 210, duration=mouse_move, tween=pyautogui.easeInOutQuad)  # move back to bank
#     pyautogui.click()
#     time.sleep(move_wait_bridge)


# BANK STAND FLETCHING
#     wait = create_delay(50, 57.5, 2)  # when cutting bows
#     wait2 = create_delay(19.5, 22.5, 2)  # when stringing bows
#     ui_wait = create_delay(1.5, 2, 2)
#     pyautogui.click()
#     time.sleep(ui_wait)
#     pyautogui.press('f10')
#     time.sleep(ui_wait)
#     pyautogui.press('4')
#     time.sleep(ui_wait)
#     pyautogui.press('space')
#     time.sleep(wait2)

# RANGE COOKING
#     wait = create_delay(70, 75, 2)
#     pyautogui.moveTo(852, 760, duration=1.5, tween=pyautogui.easeInOutQuad)  # move to range
#     pyautogui.click()
#     time.sleep(3.5)
#     pyautogui.press('space')
#     time.sleep(wait)
#     pyautogui.moveTo(1021, 367, duration=1.5, tween=pyautogui.easeInOutQuad)  # move to banker
#     pyautogui.click()
#     time.sleep(3.5)
#     pyautogui.press('f10')
#     time.sleep(1.5)

# DOUBLE NODE MINING
#     random_mining_wait1 = create_delay(5, 12, 2)
#     random_mining_wait2 = create_delay(7.5, 15, 2)
#     pyautogui.moveTo(1002, 412, duration=1.5, tween=pyautogui.easeInOutQuad)  # move to banker
#     pyautogui.click()
#     time.sleep(random_mining_wait1)
#
#     if times_ran % 5 == 0:
#         pyautogui.press('1')
#
#     pyautogui.moveTo(850, 577, duration=1.5, tween=pyautogui.easeInOutQuad)  # move to banker
#     pyautogui.click()
#     time.sleep(random_mining_wait2)

# BANK STAND HERBING
#     pyautogui.moveTo(811, 419, duration=1.5, tween=pyautogui.easeInOutQuad)  # move to banker
#     pyautogui.click()
#     time.sleep(1.25)  # wait for bank menu open
#     pyautogui.press('f7')
#     time.sleep(1)  # wait for bank menu to close (this should be faster than open)
#     pyautogui.moveTo(1637, 907, duration=1, tween=pyautogui.easeInOutQuad)
#     pyautogui.click()
#     pyautogui.moveTo(1678, 908, duration=0.5, tween=pyautogui.easeInOutQuad)
#     pyautogui.click()
#     time.sleep(1.25)  # wait for herb making window
#     pyautogui.press('space')
#     time.sleep(12.5)

# APE ATOLL COURSE, START FROM ENDING
# # OBSTACLE 1
#     pyautogui.moveTo(1589, 440, duration=2, tween=pyautogui.easeInOutQuad)
#     pyautogui.click()
#     time.sleep(10)
#
#     # OBSTACLE 2
#     pyautogui.moveTo(1014, 506, duration=2, tween=pyautogui.easeInOutQuad)
#     pyautogui.click()
#     time.sleep(5)
#
#     # OBSTACLE 3
#     pyautogui.moveTo(992, 470, duration=2, tween=pyautogui.easeInOutQuad)
#     pyautogui.click()
#     time.sleep(5)
#
#     # OBSTACLE 4
#     pyautogui.moveTo(1058, 528, duration=2, tween=pyautogui.easeInOutQuad)
#     pyautogui.click()
#     time.sleep(5)
#
#     # OBSTACLE 5
#     pyautogui.moveTo(605, 313, duration=2, tween=pyautogui.easeInOutQuad)
#     pyautogui.click()
#     time.sleep(7.5)
#
#     # OBSTACLE 6
#     pyautogui.moveTo(897, 660, duration=2, tween=pyautogui.easeInOutQuad)
#     pyautogui.click()
#     time.sleep(15)
