from ultralytics import YOLO

model = YOLO("./weights/yolov4_weights_ep150_608.pth")

results = model("0")