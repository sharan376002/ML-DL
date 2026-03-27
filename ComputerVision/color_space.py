import cv2


img  = cv2.imread('D:\ML-DL-learns\ComputerVision\Datasets\cube.jpg')

resize = cv2.resize(img , (500,500))

# lab color space  

lab = cv2.cvtColor(resize , cv2.COLOR_BGR2LAB)

l,a,b = cv2.split(lab)

cv2.imshow("Lightness : ", l)
cv2.imshow("green-red : ", a)
cv2.imshow("blue to yellow : ", b)


# when u want to run the output just uncomment it ..
# cv2.imshow("lab image : ", lab)



ycrcb = cv2.cvtColor(resize,cv2.COLOR_BGR2YCR_CB)

cv2.imshow("ycr : ", ycrcb)


# hsv color spcae :


hsv  = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)

h,s,v = cv2.split(hsv)

cv2.imshow("H", h)
cv2.imshow("S",s)
cv2.imshow("v", v)

cv2.imshow("HSV : ", hsv)

if cv2.waitKey(1) & 0xFF ==27:
    quit()


cv2.waitKey(0)
cv2.destroyAllWindows()