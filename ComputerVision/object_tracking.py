import cv2
from ultralytics import YOLO

import numpy as np



vid = cv2.VideoCapture(r'D:\ML-DL-learns\ComputerVision\Datasets\bottles.mp4')

model = YOLO("yolov8n.pt")

unique_id = set()

while True:

    ret,frame = vid.read()
    if not ret:
        break

    result = model.track(frame, classes = [39], persist = True , verbose = False, tracker="bytetrack.yaml", conf=0.3)
    """
    in this ,
    class 39 - is used for to detect the BOTTLE
    Class 1 for persons
    for to see the various object we need to see in the yolo ducumentation website 

    persist - is used to use the same id for an object without changing it 

    verbose - is used to it dont print the unwanted things in the output terminal it print only whatever is required
    
    """
    annotated_frame = result[0].plot()

    if result[0].boxes and result[0].boxes.id is not None:

        ids = result[0].boxes.id.numpy()

        for uids in ids:
            unique_id.add(uids)

        cv2.putText(annotated_frame , f"Count : {len(unique_id)}", (10,20), cv2.FONT_HERSHEY_COMPLEX, 1,(0,255,0),2)


    cv2.imshow("Object Tracking ", annotated_frame)

    


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



vid.release()

cv2.destroyAllWindows()