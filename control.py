import pyautogui

class Controller:
    def __init__(self, speed=1.0, interval=0.5):
        self.speed = speed
        self.interval = interval

    def press_space(self):
        """模拟按下空格键"""
        pyautogui.press('space', interval=self.interval)

    def mouse_click(self, position=None):
        """模拟鼠标点击，默认点击当前位置"""
        if position:
            x, y = position
            pyautogui.moveTo(x, y, duration=self.speed)
            pyautogui.click()
        else:
            pyautogui.click()

    def scroll_up(self, amount=1):
        """向上滑动"""
        pyautogui.scroll(amount)

    def scroll_down(self, amount=1):
        """向下滑动"""
        pyautogui.scroll(-amount)

    def set_speed(self, speed):
        """设置操作速度"""
        self.speed = speed

    def set_interval(self, interval):
        """设置按键间隔时间"""
        self.interval = interval
    def open_finder(self):
        """在Mac系统中打开访达（Command + Shift + E）"""
        pyautogui.hotkey('command', 'shift', 'e')