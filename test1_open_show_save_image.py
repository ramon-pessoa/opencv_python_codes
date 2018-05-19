# Opening, showing, and saving an image

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('diving.jpg', cv2.IMREAD_GRAYSCALE) # cv2.IMREAD_GRAYSCALE = 0
# img = cv2.imread('diving.jpg', cv2.IMREAD_COLOR) # cv2.IMREAD_GRAYSCALE = 1
# img = cv2.imread('diving.jpg', cv2.IMREAD_UNCHANGED) # cv2.IMREAD_GRAYSCALE = -1

nPixels = img.size;
print("diving.jpg . Total number of pixels = ", nPixels)

# Plotting with OpenCV
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Plotting with Matplotlib
plt.imshow(img, cmap='gray', interpolation='bicubic')
# Drawing a line
# plt.plot([50, 100], [80, 100], 'c', linewidth=5)
plt.show()

# To save an image
cv2.imwrite('diving_gray.png', img)