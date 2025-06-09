import time
from control import Controller

ctrl = Controller()


ctrl.mouse_click()
print("完成单击")
time.sleep(5)
ctrl.scroll_up()
print("完成上滚")
time.sleep(5)
ctrl.scroll_down()
print("完成下滚")
time.sleep(5)
ctrl.press_space()
print("完成空格")
time.sleep(5)