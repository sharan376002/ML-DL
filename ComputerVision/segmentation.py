import cv2

from ultralytics import YOLO

import numpy as np



vid  = cv2.VideoCapture('D:\ML-DL-learns\ComputerVision\Datasets\peoples.mp4')


model = YOLO("yolov8n-seg.pt")


while True:

    ret,frame = vid.read()

    res = model.track(frame , classes=[0], persist=True , verbose=False)

    for r in res:

        annotated_frame = frame.copy()

        if r.masks is not  None  and r.boxes is not None  and r.boxes.id is not None:
            masks = r.masks.data.numpy()
            boxes = r.boxes.xyxy.numpy()
            ids = r.boxes.id.numpy()



            for i,mask in enumerate(masks):
                person_id = ids[i]
                x1,y1,x2,y2 = boxes[i].astype(int)
                
                # Resize mask to frame size
                mask_resi = cv2.resize(mask.astype(np.uint8), (annotated_frame.shape[1], annotated_frame.shape[0]))
                
                # Apply mask to frame with overlay
                colored_mask = np.zeros_like(annotated_frame)
                colored_mask[:,:] = (0, 255, 0)  # Green color for masks
                mask_indices = mask_resi > 0.5
                annotated_frame[mask_indices] = cv2.addWeighted(annotated_frame[mask_indices], 0.6, colored_mask[mask_indices], 0.4, 0)
                
                # Draw bounding box and ID
                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(annotated_frame, f'ID: {int(person_id)}', (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    if not ret:
        break
    
    # Display frame
    cv2.imshow('YOLOv8 Instance Segmentation & Tracking', annotated_frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
vid.release()
cv2.destroyAllWindows()

    