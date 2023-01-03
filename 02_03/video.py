import numpy as np
import cv2

# creates a video capture object to check if it can open file
# if you want to use webcam, replace the path with 0
cap = cv2.VideoCapture('../images/shore.mov')

if cap.isOpened() == False:
    print('Cannot open file or video stream')

# loops through video frame unless escaped
while True:
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow('Frame', frame)

        # if passing images, pass 0 to waitKey function
        # if passing videos, pass # > 0, as 0 would pause the video on the frame

        # waits 25 milliseconds
        if cv2.waitKey(25) & 0xFF == 27:
            break

    else:
        break

# release vid cap object and close windows
cap.release()
cv2.destroyAllWindows()


