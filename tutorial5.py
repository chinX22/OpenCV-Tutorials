import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # Get frame and dimensions
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Save the HSV of the frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Set limits on whats considered blue in hsv
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Makes a mask where if a pixel is in the range of blue we defined, it will
    # be white, else black
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # frame =  frame & mask
    result = cv2.bitwise_and(frame, frame, mask=mask)


    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
