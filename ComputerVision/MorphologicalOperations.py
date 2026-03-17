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


Why we use it

Erosion is used to:

-remove small noise pixels
-separate connected objects

"""


ker = np.ones((3,3), np.uint8)

erosion = cv2.erode(img1, ker , iterations=1)

cv2.imshow("erro", erosion)



# 2.Dilation

# dilation explands the white region in the image 

# white object becomes larger

dil = cv2.dilate(img1 , ker , iterations=1)

cv2.imshow("Dilation : ", dil)

"""

dilation

Why we use it

Dilation helps to:

- fill small holes
-  connect broken object parts

"""



# OPening 

# it is errosion followed by dilation it occusliie one after another , accodrind to our needs

opening =  cv2.morphologyEx(img1, cv2.MORPH_OPEN, ker)

cv2.imshow("OPeing : ", opening)

"""

1. Erode image
2. Dilate result

Opening removes small objects or noise while keeping main shapes.

we use it to remove the noise in the image

"""


# 4. closing 

# it is dilation followed by errosion it just a opposite of the opening

clo = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, ker)

cv2.imshow("Closing : ", clo)

"""

Closing fills small holes and gaps inside objects.
1. Dilate image
2. Erode result


we ue it to
- fill small holes inside objects
- connect broken boundaries
"""


# morphological gradients 

# it is actually morph gradient = dilation - errosion 

# it only contains of the bboundraies of the image

# it is used to dectct the boundraies and highlight the edges

grad = cv2.morphologyEx(img1 , cv2.MORPH_GRADIENT, ker)

cv2.imshow("Gradient : ", grad)


cv2.waitKey(0)

cv2.destroyAllWindows()