from control import Controller

ctrl = Controller()

while True:
    ctrl.mouse_click()
    ctrl.scroll_up()
    time.sleep(1)
    ctrl.scroll_down()
    time.sleep(1)
    ctrl.press_space()
    time.sleep(1)