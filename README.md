## 0 GetStart

python>=3.8

### 0.1 安装pytorch

[pytorch官网](https://pytorch.org/)查找并安装与个人设备适配的pytorch版本

### 0.2 安装其他软件环境

运行：

```
pip install -r requirements.txt
```

### 0.3 快捷键设置

​		用户可以通过修改`shortcut.json`中的内容，指明每一手势对应的快捷键，完成对快捷键的设置（支持的手势与快捷键见下表，可以对两个表格的内容进行排列组合设置）

### 0.4 代码运行

完备的参数设置：

```
python main.py --weights /path/to/weight --input_path /path/to/input --output_path /path/to/output
```

参数说明：

- weights：手势检测所用的权重文件
- input_path：继承自yolo，输入也可以是图像或视频，但在本项目的应用场景下，**输出一般为摄像头(0)**
- output_path：可以将手势检测过程保存下来，但在本项目应用场景下无意义，所以这里默认不保存

综上，如果用户只想直接应用本项目，直接运行下面的命令就可以了：

```
python main.py
```



#### 支持的手势

|  支持手势  | 命名 |
| :--------: | :--: |
| 打电话手势 | call |
|  竖大拇指  | like |
|    握拳    | palm |
|  五指张开  | fist |
|   ok手势   |  ok  |

#### 支持的快捷键

| 支持快捷键                 | 命名                         |
| -------------------------- | ---------------------------- |
| 打开资源管理器             | open_finder                  |
| 单击鼠标                   | mouse_click                  |
| 滚轮上滚                   | scroll_up                    |
| 滚轮下滚                   | scroll_down                  |
| 单击空格                   | press_space                  |
| 打开访达                   | open_finder                  |
| 截屏并存储在剪切板         | take_screenshot_to_clipboard |
| 切换到下一个最近使用的程序 | switch_to_next_recent_app    |
| 焦点切换到桌面             | focus_on_desktop             |
| 打开日历                   | open_calendar                |

## 1 说明

### 1.1 多手势问题

​		当输入中同时出现多种手势时，会自动选取置信度最高的一个检测结果作为最终的输出根据，并不存在同时完成多种快捷键的情况