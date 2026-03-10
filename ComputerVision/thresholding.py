import cv2

img2 = cv2.imread('D:\ML-DL-learns\ComputerVision\images\sign.jpg',0)



"""

threshold is 
Essentially, it’s about setting a cutoff point — known as the threshold — and anything above this point becomes white, 
while anything below it turns black.

For example, if you’re working on detecting text in a scanned document, 
thresholding can help you isolate the text from the background by turning the text black and the background white.

It’s a straightforward yet powerful tool, especially when you need to simplify an image for further analysis



for example :
     when thresholding is import is like there is a scanned document that background isnt uniform white and the text 
     isnt perfect black so in that place wheere thresholding is realy helpful 

It’s a straightforward yet powerful tool, especially when you need to simplify an image for further analysis



"""


# 1 .binnarry threshold 

#Binary threshold converts a grayscale image into black and white based on a fixed threshold value.

_, thresh = cv2.threshold(img2, 120 ,255, cv2.THRESH_BINARY)

cv2.imshow("Binary",thresh)




# 2 adaptive threshold :

"""

in the previous thresholding where it is global , where it thresholding is apply to all the regios of the image , where in the
adaptive threshold is where if document where flash light is on where the image becomes dark in that places so we use advative thresholding
for that special cases

This means that it adjusts dynamically based on the local pixel intensities, allowing you to effectively handle
 images with varying lighting conditions and contrasts.

 it mainly helps when the light is uneven

 it is like, Bright region -> higher threshold , Dark region -> lower threshold

 Adaptive thresholding solves this problem by calculating different threshold values 
 for different small regions of the image based on nearby pixels

"""

adp_thresh = cv2.adaptiveThreshold(img2, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

"""
- adaptiveThreshold()  -> it calculate the local threshold for small region
- 255 , max pixel value
- ADAPTIVE_THRESH_MEAN_C ->threshold based on mean of neighboring pixels
- 11 -> size of neighborhood area
- 2 -> constant subtracted from the mean

"""

cv2.imshow("Adaptive Threshold : ", adp_thresh)



# 3.Otsu’s threshold

#Otsu’s method automatically finds the best threshold value.

"""
in the otsu threshold goal is to separate the image into two 
 - foreground  pixels
 - backround  pixels

 Otsu thresholding automatically finds the best threshold value to clearly separate object and background.

 steps of working od otsu thresh:

 - convert the image into grayscale
 - compute the histogram for pixel intenshity(0-255)
 -try every possible combinations values
 - for each threhold , divide into two clases , calculate the vairance with clases
 - choose the threshold that minimize the intra  class variance 

that gives the ooptiaml threshold


in simple words , it create the histogram of image of [background peak , foreground peak] where the peak pixels values aorund are 
(0-80 , 180-255) the optimal maybe [120]


"""

_, thresh1 = cv2.threshold(img2, 0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("Otsu threshold : ", thresh1)


cv2.waitKey(0)

cv2.destroyAllWindows()




