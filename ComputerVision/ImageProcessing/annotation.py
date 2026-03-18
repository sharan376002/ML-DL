import cv2

import numpy as np


canvas = np.zeros((512,512,3), dtype=np.uint8)  # in that dtype that represent the color channel 



cv2.line(canvas, (3,7), (511,511),(0,0,255),7) # canvas -> coordination  -> canva size -> color channel -> line thickness

cv2.rectangle(canvas, (200,333), (473,133),(111,222,121),-1)


cv2.putText(canvas, "Hello Sharan", (10,30),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255),2)



cv2.imshow("canvas " , canvas)

cv2.waitKey(0)

cv2.destroyAllWindows()