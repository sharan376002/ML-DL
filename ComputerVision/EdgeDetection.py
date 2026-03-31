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

resize = cv2.resize(img,(500,500))


img_gray = cv2.cvtColor(resize ,cv2.COLOR_BGR2GRAY)

img_blur = cv2.GaussianBlur(img_gray , (3,3),0)

sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
# Display Sobel Edge Detection Images
cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y', sobely)
cv2.imshow('Sobel X Y using Sobel() function', sobelxy)







if cv2.waitKey(1) & 0xFF ==27:
    quit()


cv2.waitKey(0)
cv2.destroyAllWindows()

