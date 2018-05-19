# Drawing line, rectangle, circle, polygon and Writing text in the image

import numpy as np
import cv2

img = cv2.imread('diving.jpg', cv2.IMREAD_COLOR)

# Drawing a line
#(255, 255, 255) = (blue, green, red)
cv2.line(img, (0,0), (150, 150), (255, 255, 255), 15)

# Drawing a rectangle
cv2.rectangle(img, (15, 25), (200, 150), (0, 255, 0), 5)

# Drawing a circle
cv2.circle(img, (100, 63), 55, (0, 0, 255), -1)

# Drawing a polygon
pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0, 255, 255), 3)

# Writing text in the image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV testing!', (0, 130), font, 1, (200, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destryAllWindows()