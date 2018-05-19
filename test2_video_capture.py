# 

import cv2
import numpy as np

# cap = cv2.VideoCapture(0) # computer camera 0
#cap = cv2.VideoCapture(1) # computer camera 1, and so on
cap = cv2.VideoCapture('diving.mp4')

count = 0
while True:
	ret, frame = cap.read() # ret = True or False, frame = video frame
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow('frame', frame)
	cv2.imshow('gray', gray)

	if (count % 10 == 0):
		# To save an image
		imgname = "frame_" + str(count) + ".png"
		cv2.imwrite("frames2/"+imgname, frame)
	
	count = count + 1

	# To get out of the loop, press any keyboard key
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()