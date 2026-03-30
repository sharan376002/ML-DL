import cv2

import numpy as np


"""
Sudden changes in pixel intensity characterize edges. We need to look for such changes in the neighboring pixels to detect edges.

the two important edge detection algorithm are avil in opencv is 
- soble edge detection
- canny edge dectection

Edges = places where brightness changes sharply (like object boundaries).

soble detector :

The Sobel operator applies two filters (kernels) to an image:

One detects changes in the horizontal direction (x)
One detects changes in the vertical direction (y)

then finally  we compute teh gradient of it 

   G = squareroot(gx^2 + gy^2)
     it give the edge strength at each pixel 

"""


img = cv2.imread(r'D:\ML-DL-learns\ComputerVision\Datasets\fl3.jpg')












if cv2.waitKey(1) & 0xFF ==27:
    quit()


cv2.waitKey(0)
cv2.destroyAllWindows()

