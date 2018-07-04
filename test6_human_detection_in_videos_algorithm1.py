# Opening, playing, detectin human, saving a video

# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

#####################################################################
# Settings
save_video = False
video_width = 400
video_height = 225
fps = 20.0 # fps = frames per second
#FourCC code is passed as cv2.VideoWriter_fourcc('M','J','P','G') or cv2.VideoWriter_fourcc(*'MJPG') for MJPG.
fourcc_format = 'XVID' # 'XVID', 'MJPG', 'MP4V'
show_frame_size = True
use_original_frame_size = False
use_web_cam = False
input_video_path_and_name = 'diving.mp4'
output_video_path_and_name = 'output.avi'
#####################################################################

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

if use_web_cam:
	cap = cv2.VideoCapture(0) # computer camera 0
	#cap = cv2.VideoCapture(1) # computer camera 1, and so on
else:
	cap = cv2.VideoCapture(input_video_path_and_name)

# Define the codec and create VideoWriter object
if save_video:
	fourcc = cv2.VideoWriter_fourcc(*FourCC_format)
	out = cv2.VideoWriter(output_video_path_and_name,fourcc, fps, (video_width, video_height))

# count = 0
while True:
	ret, frame = cap.read() # ret = True or False, frame = video frame

	if use_original_frame_size:
		# Original image
		image = frame.copy()
	else:
		# Image resized
		image = imutils.resize(frame, width=min(400, frame.shape[1]))
	
	# Print image height, image width, and image channels
	if show_frame_size:
		height, width, channels = image.shape
		print("height, width, channels: ", height, width, channels)
		show_frame_size = False
	
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
	
	if save_video:
		out.write(image)

	# To get out of the loop, press any keyboard key
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
if save_video:
	out.release()
cv2.destroyAllWindows()