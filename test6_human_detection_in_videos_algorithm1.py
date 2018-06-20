# Opening, playing, detectin human, saving a video

# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# cap = cv2.VideoCapture(0) # computer camera 0
#cap = cv2.VideoCapture(1) # computer camera 1, and so on
cap = cv2.VideoCapture('diving.avi')

# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

# count = 0
while True:
	ret, frame = cap.read() # ret = True or False, frame = video frame

	# Original image
	image = frame.copy()
	# Image resized
	#image = imutils.resize(frame, width=min(400, frame.shape[1]))
	
	orig = image.copy()

	# detect human in the image
	(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
		padding=(8, 8), scale=1.05)

	# draw the original bounding boxes
	for (x, y, w, h) in rects:
		cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

	# apply non-maxima suppression to the bounding boxes using a
	# fairly large overlap threshold to try to maintain overlapping
	# boxes that are still people
	rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

	# draw the final bounding boxes
	for (xA, yA, xB, yB) in pick:
		cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

	# show the output images
	cv2.imshow("Human Detection Before Non-Maxima Suppression", orig)
	cv2.imshow("Human Detection After Non-Maxima Suppression", image)
	
	#out.write(image)

	# To get out of the loop, press any keyboard key
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
#out.release()
cv2.destroyAllWindows()