import cv2

from ultralytics import YOLO

import numpy as np


img = cv2.imread('D:\ML-DL-learns\ComputerVision\Datasets\sha.jpg')

model = YOLO("yolov8n.pt")  # pt -> is pre trained 

result = model(img)

annot = result[0].plot()

cv2.imshow("Annoted image : ", annot)


cv2.waitKey(0)

cv2.destroyAllWindows()

