import cv2



cap = cv2.VideoCapture(0)



gap =5

count = 0

frames = []



while True:

    ret, frame = cap.read()

    if not ret:
        print("no video is been captured ")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frames.append(gray)

    if len(frames) > gap+1:  # we removing the first Frame when it exceed the gap , like sliding window 
        frames.pop(0)

    cv2.putText(frame, f"COUNT : {count}", (10,30), cv2.FONT_HERSHEY_PLAIN ,1,(0,255,3),2)

    if len(frames) > gap:   

        diff = cv2.absdiff(frames[0], frames[-1])
        # Convert the difference image into a binary image using thresholding.
        # Pixels with value > 30 become white (255), and pixels <= 30 become black (0).
        # '_' ignores the first return value (the threshold used), because we only need the binary image.
        # the 30 value we take it has countor white spaces

        _, thresh = cv2.threshold(diff, 30 , 255, cv2.THRESH_BINARY)

        # Find contours (object boundaries) from the binary image.
        # RETR_EXTERNAL → detects only outer contours (ignores inner shapes).
        # CHAIN_APPROX_SIMPLE → reduces number of points in the contour to save memory.
        # '_' ignores the hierarchy output because we don't use it.

        contours ,_ = cv2.findContours(thresh , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)




