
import json
from control import Controller

method_dict={
    "open_finder":Controller.open_finder,
    "mouse_click":Controller.mouse_click,
    "press_space":Controller.press_space,
    "scroll_up":Controller.scroll_up,
    "scroll_down":Controller.scroll_down,
    "take_screenshot_to_clipboard":Controller.take_screenshot_to_clipboard
}

#设置快捷键
with open('shortcut.json', 'r', encoding='utf-8') as file:
    shortcut_dict = json.load(file)
for key in shortcut_dict:
    shortcut_dict[key]=method_dict[shortcut_dict[key]]

#TODO:手势识别
def run_gesture():
    pass

#TODO:主循环
while True:
    gesture=run_gesture()
    shortcut_dict[gesture]()