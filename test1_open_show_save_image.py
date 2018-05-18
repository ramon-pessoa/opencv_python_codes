# Opening, showing, and saving an image

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('frame_130_imgcropped.png', cv2.IMREAD_GRAYSCALE) # cv2.IMREAD_GRAYSCALE = 0
# img = cv2.imread('diving.jpg', cv2.IMREAD_COLOR) # cv2.IMREAD_GRAYSCALE = 1
# img = cv2.imread('diving.jpg', cv2.IMREAD_UNCHANGED) # cv2.IMREAD_GRAYSCALE = -1

# Total number of pixels
img = cv2.imread('frame_130_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_130_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_170_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_170_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_200_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_200_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_230_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_230_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_260_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_260_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_290_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_290_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_320_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_320_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_350_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_350_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_380_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_380_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_410_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_410_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_440_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_440_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_470_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_470_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_500_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_500_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_530_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_530_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_560_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_560_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_570_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_570_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_580_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_580_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_590_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_590_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_600_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_600_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_610_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_610_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_620_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_620_imgcropped.png. Total number of pixels = ", nPixels)

img = cv2.imread('frame_630_imgcropped.png', cv2.IMREAD_GRAYSCALE)
nPixels = img.size;
print("frame_630_imgcropped.png. Total number of pixels = ", nPixels)

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