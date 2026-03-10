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



        for c in contours:

            if cv2.contourArea(c) <500:
                continue

            x,y,w,h = cv2.boundingRect(c)

            cv2.rectangle(frame , (x,y), (x+w ,y+h), (0,255,0),2)


        motion = any(cv2.contourArea(c) <500 for c in contours)

        if motion:
            cv2.putText(frame , "Motion Detected ",(10,60), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

            #cv2.imwrite(f"motionFrame{count}.jpg",frame)  this line for to save as image if any motion detected 

            # print(f" file saves {count}.jpg")


        
        cv2.imshow("motion Detected", frame)

        count+=1


        if cv2.waitKey(1) & 0xFF ==27:
            break


cap.release()

cv2.destroyAllWindows()

        






