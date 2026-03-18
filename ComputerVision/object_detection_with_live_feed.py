import cv2

from ultralytics import YOLO


vid  = cv2.VideoCapture(0)


model = YOLO("yolov8n.pt")

while True:

    ret,frame = vid.read()

    res = model(frame)

    annot = res[0].plot()

    cv2.imshow("image : ", annot)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()

cv2.destroyAllWindows()