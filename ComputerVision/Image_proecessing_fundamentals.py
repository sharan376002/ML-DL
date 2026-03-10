import cv2




img2 = cv2.imread('D:\ML-DL-learns\ComputerVision\images\sign.jpg')



# average blur (mean Blur)
#Average blur replaces each pixel with the average value of its neighboring pixels
#New pixel = average of surrounding pixels


blur  = cv2.blur(img2,(15,15))

"""
why we use the averge blur
-Removes simple noise

-Smooths an image

When to use it

Use Average Blur when:

- Noise is small and random
- You only need basic smoothing


"""

cv2.imshow("averageBlur : ", blur)



# Gaussian Blur
#Gaussian blur uses a Gaussian distribution (bell curve).

#Nearby pixels have higher weight, far pixels have lower weight.



blur2 = cv2.GaussianBlur(img2, (15,15),0)



cv2.imshow("Gausian_blur :", blur2)

"""
Why we use it

Gaussian blur:

-removes Gaussian noise
-smooths images naturally
-preserves structures better than average blur

When to use it

Use Gaussian blur before:

Edge detection (Canny)

Object detection

Feature detection

Image segmentation.

"""


# median blur 
#Median blur replaces a pixel with the median value of surrounding pixels.

blur3  = cv2.medianBlur(img2, 5)
#Median filter is excellent for removing impulse noise.

cv2.imshow("Median Blur: ", blur3)



# bilateral filter

#Bilateral filtering performs edge-preserving smoothing.
# it is like a if the pixels are same it wont blur it , edges are presevesd so we an cartooon like a smoothing 




blur4 = cv2.bilateralFilter(img2 , 9,75,75)
"""
the parameter in the bilater fiter
9  → neighborhood size
75 → color similarity
75 → spatial distance

why we use this filter:

-removes noise
-keeps edges sharp

when we use it : 

-edges must be preserved
- you want cartoon-like smoothing
-  segmentation tasks

"""
cv2.imshow(blur4)

cv2.waitKey(0)

cv2.destroyAllWindows()