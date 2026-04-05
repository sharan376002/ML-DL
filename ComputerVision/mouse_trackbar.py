import cv2

top_left = []

top_right = []

def draw_rectangle(event ,x,y,flags,*userdata):
    global top_left, top_right


    if event ==  cv2.EVENT_LBUTTONUP:
        top_right = [(x,y)]

    elif event == cv2.EVENT_LBUTTONDOWN:
        top_left = [(x,y)]


    cv2.rectangle(image ,  top_left, top_right, (0,255,0),  2,7)

    cv2.imshow("cursor ", image)



image = cv2.imread(r'D:\ML-DL-learns\ComputerVision\Datasets\fl1.jpg')

temp = image.copy()
# Create a named window
cv2.namedWindow("Window")
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", draw_rectangle)
 
k=0
# Close the window when key q is pressed
while k!=113:
  # Display the image
  cv2.imshow("Window", image)
  k = cv2.waitKey(0)
  # If c is pressed, clear the window, using the dummy image
  if (k == 99):
    image= temp.copy()
    cv2.imshow("Window", image)
 
cv2.destroyAllWindows()