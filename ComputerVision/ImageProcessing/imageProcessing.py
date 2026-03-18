import cv2

img1  = cv2.imread('D:\ML-DL-learns\ComputerVision\images\sha.jpg')

img2 = cv2.imread('D:\ML-DL-learns\ComputerVision\images\wall.jpg')


# four image processing techinqe are there 

resize = cv2.resize(img1, (200,200))

grayscale = cv2.cvtColor(img2 , cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(img1, (15,15),0)

canny_edge_detector = cv2.Canny(img2, 100,200)  # it was the values in th lower bound to higher bound , from that lower color range to higher color range it deteects (actual color ranges from(0-255))


cv2.imshow("re", resize)
cv2.imshow("gray", grayscale)

cv2.imshow("blurr",blur)

cv2.imshow("edge detector",canny_edge_detector)

cv2.waitKey(0)

cv2.destroyAllWindows()