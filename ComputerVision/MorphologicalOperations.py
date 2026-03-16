import cv2

import numpy as np


img1  = cv2.imread('D:\ML-DL-learns\ComputerVision\images\sha.jpg',0)

#Morphological operations work using a structuring element (kernel) that slides across the image.


# 1. Errosion
"""
typical pipeline:

Image
  ↓
Thresholding
  ↓
Morphological Operations
  ↓
Contour Detection / Object Detection

Erosion shrinks white regions (foreground objects) in a binary image.

Small white pixels or noise disappear.

the white region becomes --> Smaller

"""


ker = np.ones((3,3), np.uint8)

erosion = cv2.erode(img1, ker , iterations=1)

cv2.imshow("erro", erosion)


cv2.waitKey(0)

cv2.destroyAllWindows()