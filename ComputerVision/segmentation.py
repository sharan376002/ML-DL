import cv2

from ultralytics import YOLO



vid  = cv2.VideoCapture(0)


model = YOLO("yolov8n-seg.pt")


while True:

    ret,frame = vid.read()

    res = model.track(frame , classes=[0], persist=True , verbose=False)

    