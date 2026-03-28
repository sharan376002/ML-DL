import cv2

import numpy as np


img  = cv2.imread('D:\ML-DL-learns\ComputerVision\Datasets\cube.jpg')

resize = cv2.resize(img , (500,500))


# converting to respective color spaces 

hsv = cv2.cvtColor(resize , cv2.COLOR_BGR2HSV)

lab = cv2.cvtColor(resize, cv2.COLOR_BGR2LAB)

ycb = cv2.cvtColor(resize , cv2.COLOR_BGR2YCR_CB)



# i choose green color


bgrC = [0,165,255]

hsvC = [5, 100, 10]

ycbC = [0, 140, 100]

labC = [20, 140, 150]

threshold = 80  # the threshold act as tolerance if any diffent lighting conditon , it responds accordingly so that we can varry it 



#  for bgr 


minBgr = np.array([bgrC[0] - threshold, bgrC[1]- threshold, bgrC[2] -threshold])
maxBgr = np.array([bgrC[0] + threshold , bgrC[1]+ threshold, bgrC[2] + threshold ])


# the in range function will within the pixel range it will while other will becomes black
maskbgr = cv2.inRange(resize ,minBgr,maxBgr)
# with the bitwise and we actually comapare with the orginal image to color the actuial pixel where that within in the range
resBgr = cv2.bitwise_and(resize,resize,mask=maskbgr)



# for HSV


minHsv = np.array([hsvC[0] - threshold, hsvC[1]- threshold, hsvC[2] -threshold])
maxHsv = np.array([hsvC[0] + threshold , hsvC[1]+ threshold, hsvC[2] + threshold ])

maskHsv = cv2.inRange(hsv,minHsv,maxHsv)

resHsv = cv2.bitwise_and(resize,resize,mask=maskHsv)


# for ycrcb

minYcb = np.array([ycbC[0] - threshold, ycbC[1]- threshold, ycbC[2] -threshold])
maxYcb = np.array([ycbC[0] + threshold , ycbC[1]+ threshold, ycbC[2] + threshold ])

maskYcb = cv2.inRange(ycb,minYcb,maxYcb)

resYcb = cv2.bitwise_and(resize,resize,mask=maskYcb)




# for lab 


minlab = np.array([labC[0] - threshold, labC[1]- threshold, labC[2] -threshold])
maxlab = np.array([labC[0] + threshold , labC[1]+ threshold, labC[2] + threshold ])

masklab = cv2.inRange(lab,minlab,maxlab)

reslab = cv2.bitwise_and(resize,resize,mask=masklab)



# final  results


cv2.imshow("orginal image : ", resize)
# maks
cv2.imshow("BGR MASK : ", maskbgr)

cv2.imshow("HSV MASK : ", maskHsv)

cv2.imshow("YCB mask : ", maskYcb)

cv2.imshow("Lab mask : ", masklab)


# result 

cv2.imshow("BGR RES : ", resBgr)

cv2.imshow("HSV RES : ", resHsv)

cv2.imshow("YCB RES  : ", resYcb)

cv2.imshow("LAB RES : ", reslab)









if cv2.waitKey(1) & 0xFF ==27:
    quit()


cv2.waitKey(0)
cv2.destroyAllWindows()