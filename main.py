
import json
from control import Controller

method_dict={
    "open_finder":Controller.open_finder,
    "mouse_click":Controller.mouse_click,
    "press_space":Controller.press_space,
    "scroll_up":Controller.scroll_up,
    "scroll_down":Controller.scroll_down,
    "take_screenshot_to_clipboard":Controller.take_screenshot_to_clipboard,
    "open_mission_control":Controller.open_mission_control,
    "switch_to_next_recent_app":Controller.switch_to_next_recent_app,
    "open_system_settings":Controller.open_system_settings,
    "focus_on_desktop":Controller.focus_on_desktop,
    "open_calendar":Controller.open_calendar
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
pre_gesture=None
while True:
    gesture=run_gesture()
    #收起”日历“对应手势后即关闭日历
    if shortcut_dict[pre_gesture]==Controller.open_calendar and shortcut_dict[gesture]!=Controller.open_calendar:
        Controller.switch_to_next_recent_app()
    
    shortcut_dict[gesture]()
    pre_gesture=gesture