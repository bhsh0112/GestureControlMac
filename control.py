import pyautogui
import subprocess

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
        """在Mac系统中打开访达"""
        subprocess.run(['open', '-a', 'Finder'])
    def take_screenshot_to_clipboard(self):
        """在Mac系统中截取全屏并复制到剪贴板"""
        subprocess.run(['screencapture', '-x', '-c'])

    def open_mission_control(self):
        """在Mac系统中打开任务控制（Mission Control）"""
        subprocess.run(['osascript', '-e', 'tell application "System Events" to key code 100 using {control down}'])

    def switch_to_next_recent_app(self):
        """切换到下一个最近使用的应用程序"""
        # 使用 AppleScript 模拟 Command + Tab 切换到下一个最近使用的应用程序
        subprocess.run(['osascript', '-e', 'tell application "System Events" to key code 48 using {command down}'])
    def open_system_settings(self):
        """在Mac系统中打开系统设置"""
        subprocess.run(['open', '-a', 'System Settings'])
    def focus_on_desktop(self):
        """将焦点切换到桌面（最小化所有应用程序窗口）"""
        # 使用 AppleScript 来最小化所有非桌面的应用程序
        subprocess.run([
            'osascript',
            '-e',
            """
            tell application "System Events"
                set visible of every application process to false
                set frontmost of process "Finder" to true
            end tell
            """
        ])
    def open_calendar(self):
        """打开日历应用"""
        subprocess.Popen(['open', '-a', 'Calendar'])