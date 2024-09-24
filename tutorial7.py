import numpy as np
import cv2

# Graycale the image and template, size of template and image matter
img = cv2.resize(cv2.imread('assets/soccer_practice.jpg', 0), (0, 0), fx=0.8, fy=0.8)
template = cv2.resize(cv2.imread('assets/shoe.PNG', 0), (0, 0), fx=0.8, fy=0.8)
h, w = template.shape

# Throw every method at the wall
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:

    # You need a new image for each method for a blank slate
    img2 = img.copy()

    # Slides the templete over every area in the image thats the size of the
    # template, the out put array for each area is the img.dims = tem.dims
    result = cv2.matchTemplate(img2, template, method)

    # With different methods you want either the max or min value
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)    
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()