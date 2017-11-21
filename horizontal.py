import numpy as np #math libraries
import cv2 #opencv itself

def nothing(x):
	pass


# Callback Function for Trackbar (but do not any work)
def nothing(*arg):
	pass


thresholdLower = (0, 0, 0)
thresholdUpper = (255, 255, 255)

# Creating a window for later use
cv2.namedWindow('Control Panel')

# Creating track bar
#cv.CreateTrackbar(trackbarName, windowName, value, count, onChange)  None
cv2.createTrackbar('hue', 'Control Panel',68,180,nothing)#default 0 205 255 69 8 12
cv2.createTrackbar('sat', 'Control Panel',255,255,nothing)
cv2.createTrackbar('val', 'Control Panel',93,255,nothing)

cv2.createTrackbar('ero', 'Control Panel',0,100,nothing)
cv2.createTrackbar('dil', 'Control Panel',0,100,nothing)

cv2.createTrackbar('Hue Range', 'Control Panel',44,180,nothing)
cv2.createTrackbar('Sat Range', 'Control Panel',70,127,nothing)
cv2.createTrackbar('Val Range', 'Control Panel',70,127,nothing)

cap = cv2.VideoCapture(0)	


def trackRectangle(mask, frame):
	#contours,hierarchy = cv2.findContours(mask, 1, 2)
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)[-2]
	
	
	# only proceed if at least one contour was found
	if len(cnts) > 0:
		cnt = max(cnts, key=cv2.contourArea)
		M = cv2.moments(cnt)
		if M['m00'] > 0:
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			#find center piont of X for cx and turns it into an integer.
			#It turns it into an integer because pixels are whole numbers.
			#cx and cy creat a center point.
			
			area = cv2.contourArea(cnt)
			rows, cols = mask.shape
			#mask.shape finds the  size of (mask = frame)
			#boundingRect is the hugging rectangle found from the contour.
			#x is the x cordinate
			#y is the y corndinate
			x,y,w,h = cv2.boundingRect(cnt)
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
			#to have rectangle follow x and y center points we add the width and hight to the x and  y.


			

			ratioHW = float(1.0*h/w)
			#pass means skip to the next line.

			if ratioHW < 0.51:
				print ("horizontal---------")
			elif ratioHW > 1.9:
				print ("vertical don't shoot||||||||||")
			else:
				pass

			print("x",x,"y", y,"w",w ,"h", h, "ratio", ratioHW)

			#create rect object
			rect = cv2.minAreaRect(cnt)

			#---
			center = rect[0]
			#centerX = int(rect[0][0])
			#centerY = int(rect[0][1])

			#rectWidth = rect [1][0]
			#rectHeight = rect [1][1]

			# Draw a diagonal blue line with thickness of 5 px
			
			# if rectWidth > 0 and rectHeight > 0:

			# 	angleCalculate = np.arctan(rectHeight/rectWidth)*360/(2*3.141592)
			# else:
			# 	angleCalculate = 0


			#ratio = rectHeight/rectWidth



			#angle = rect[2]

			box = cv2.boxPoints(rect)

			#print out the angle it is at
			#print("Angle", angle, "ratio", ratio ,"Area", area, " width ",
			# rectWidth, " height ",rectHeight)
			
			box = np.int0(box)

			#red colored box
			cv2.drawContours(frame,[box],0,(0,0,255),2)
			


	return frame



while True:
	
	e1 = cv2.getTickCount()

	# get info from track bar and appy to result
	h = cv2.getTrackbarPos('hue','Control Panel')
	s = cv2.getTrackbarPos('sat','Control Panel')
	v = cv2.getTrackbarPos('val','Control Panel')

	erodeValue = cv2.getTrackbarPos('ero', 'Control Panel')
	dilateValue = cv2.getTrackbarPos('dil', 'Control Panel')

	hr = cv2.getTrackbarPos('Hue Range', 'Control Panel')
	sr = cv2.getTrackbarPos('Sat Range', 'Control Panel')
	vr = cv2.getTrackbarPos('Val Range', 'Control Panel')

	thresholdLower = (h-hr, s-sr, v-vr)
	thresholdUpper = (h+hr, s+sr, v+vr)

	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	mask = cv2.inRange(hsv, thresholdLower, thresholdUpper)

	res = cv2.bitwise_and(frame,frame, mask= mask)
	finalFrame = trackRectangle(mask, frame)


	#measure time
	e2 = cv2.getTickCount()

 	#seconds
	time = (e2 - e1)/ cv2.getTickFrequency()

	 #wait for keyboard to be pressed store the value as key
	key = cv2.waitKey(1) & 0xFF
 	
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break



	#now display the image to the user
	cv2.imshow("res", res)
	cv2.imshow("finalFrame", finalFrame)

cv2.destroyAllWindows()
