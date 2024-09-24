import numpy as np
import cv2

img = cv2.imread('assets/logo.jpg')
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Usage: image, number of best corners, the threshold of what the computer
# thinks is a corner. minimum distance betwen corners
corners = cv2.goodFeaturesToTrack(gray, 250, 0.1, 4)

# Turn floats into ints
corners = np.int0(corners)

# Get all corners' coords and draw a circle there
for corner in corners:
	x, y = corner.ravel()
	cv2.circle(img, (x, y), 1, (255, 255, 0), -1)

# Draws a line from a corner to all other corners
"""
for i in range(len(corners)):
	for j in range(i + 1, len(corners)):
		corner1 = tuple(corners[i][0])
		corner2 = tuple(corners[j][0])
		color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
		cv2.line(img, corner1, corner2, color, 1)
"""

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()