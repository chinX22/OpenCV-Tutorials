import cv2

# Read in image
img = cv2.imread('assets/logo.jpg', 1)

# Make half the size
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_img.jpg', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
print(img.shape)
cv2.destroyAllWindows()