# Image arithmetics and logic

import cv2
import numpy as np

# img1 and img2 must be same size images
img1 = cv2.imread('frame_2220.png')
img2 = cv2.imread('frame_2230.png')

# add form 1
# add = img1 + img2
# add form 2
#add = cv2.add(img1, img2)
# add form 3
add = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
cv2.imshow('add', add)

# ===========================
# Creating our own logo
img = cv2.imread('python_logo.png')
img_backgroud = cv2.imread('diving.jpg')
rows, cols, channels = img.shape
roi = img_backgroud[0:rows, 0:cols]

img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', img2gray)
ret, mask = cv2.threshold(img2gray, 150, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('mask', mask)

mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask_inv', mask_inv)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow('img1_bg', img1_bg)

img2_bg = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('img2_bg', img2_bg)

dst = cv2.add(img1_bg, img2_bg)
cv2.imshow('dst', dst)

img_backgroud[0:rows, 0:cols] = dst
cv2.imshow('res', img_backgroud)

# ===========================

cv2.waitKey(0)
cv2.destroyAllWindows()