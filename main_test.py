import argparse
import json
import os
from pathlib import Path
import signal
import sys
import time
from control import Controller
import cv2
from ultralytics import YOLO

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

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

class GetstureDetctor:
    def __init__(self, yolov10_model,input_path,output_path):
        self.model = yolov10_model
        self.tracked_data = []
        self.frame = []
        self.curGesture = None
        self.preGesture = None

        cap = cv2.VideoCapture(input_path)
        # 获取视频的帧率、宽度和高度
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # 定义视频编码器和输出文件
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    def get_frame(self):
        return self.frame
    

    def run_tracking(self, video_path):
        """Run YOLOv10 model for object detection"""
        # 判断输入源类型（摄像头或视频文件）
        if video_path.isdigit():
            cap = cv2.VideoCapture(int(video_path))
            print(f"Using camera device: {video_path}")
        else:
            cap = cv2.VideoCapture(video_path)
            print(f"Processing video file: {video_path}")
        
        assert cap.isOpened(), "Cannot open video source"

        while cap.isOpened():
            # for _ in range(2):  # Discard the most recent 2 frames
            ret, self.frame = cap.read()
            if not ret:
                break

            # yolov10 track
            results = self.model(self.frame)
            # Ensure tracks is not None
            if results is None :
                print("Error: Tracks data is None.")
                continue  # Skip this frame if no tracks

            # Draw detection results
            result=[False,False,False]#jam,park,people
            for result in results:
                boxes = result.boxes  # Get bounding box data
                confidences = boxes.conf  # Get confidence scores
                class_ids = boxes.cls  # Get class IDs
                names = result.names if hasattr(result, 'names') else {}

                # Iterate over each detection box
                for i, box in enumerate(boxes.xyxy):
                    x_min, y_min, x_max, y_max = box  # Get coordinates
                    confidence = confidences[i]  # Get current box confidence
                    class_id = int(class_ids[i])  # Get class ID

                    if confidence < 0.1:
                        continue

                    # Draw bounding box
                    color = (0, 255, 0)  # Green box
                    cv2.rectangle(self.frame, (int(x_min), int(y_min)), (int(x_max), int(y_max)), color, 2)

                    # Label the box with class and confidence
                    class_name = names[class_id] if names and class_id in names else "unknown"
                    label = f"{class_name}: {confidence:.2f}"
                    cv2.putText(self.frame, label, (int(x_min), int(y_min) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

                    # Get the current position of the vehicle
                    current_position = (x_min + x_max) / 2, (y_min + y_max) / 2

                
            #TODO:run shortcut
            print(result)
            # Show and output
            cv2.imshow("Frame", self.frame)
            self.video_writer.write(self.frame)

            # Press 'q' to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        self.video_writer.release()
        cv2.destroyAllWindows()

    def output(self):
        #收起”日历“对应手势后即关闭日历
        if shortcut_dict[self.preGesture]==Controller.open_calendar and shortcut_dict[self.curGesture]!=Controller.open_calendar:
            Controller.switch_to_next_recent_app()
        
        shortcut_dict[self.curGesture]()
        self.curGesture=self.curGesture

def signal_handler(sig, frame):
    print("\nRecording stopped! Video saved as", output_path)
    sys.exit(0)

# Capture Ctrl+C signal
signal.signal(signal.SIGINT, signal_handler)

parser = argparse.ArgumentParser()
parser.add_argument("--weights", nargs="+", type=str, default=ROOT / "./weights/YOLOv10n_gestures.pt", help="model path or triton URL")
parser.add_argument("--source", type=str, default="0", help="file/dir/URL/glob/screen/0(webcam)")
parser.add_argument("--output", type=str, default=ROOT / "output/", help="output path")

args = parser.parse_args()

# Start YOLOv10Tracker
input_path = str(args.source)
output_path = str(args.output)
yolov_model = YOLO(args.weights)
yolo_tracker = GetstureDetctor(yolov_model,input_path=input_path,output_path=output_path)
yolo_tracker.run_tracking(input_path)