# Pixel color value, converting pixel value, ROI = Regin Of the Image
import numpy as np
import cv2

img = cv2.imread('diving.jpg', cv2.IMREAD_COLOR)

# Color value for that pixel
px = img[55, 55]
print(px)

# Convert the pixel [55, 55] to white
img[55, 55] = [255, 255, 255]
px = img[55, 55]
print(px)

# ROI = Regin of the image
roi = img[100:150, 100:150]
# Print the roi
print(roi)
# Change the ROI pixels to white pixels
img[100:150, 100:150] = [255, 255, 255]

# Copy and past pixels
diving_part = img[37:111, 107:194]
img[0:74, 0:87] = diving_part


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()