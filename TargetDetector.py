import cv2
import numpy as np
class TargetDectector:
    def TargetDetect(img):
        count = -1
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        THRESHOLD_MIN = np.array([0, 0, 0],np.uint8)
        THRESHOLD_MAX = np.array([50, 255,255],np.uint8)

        frame = cv2.inRange(img_hsv, THRESHOLD_MIN,THRESHOLD_MAX)
        image, contours, count, = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


        for cont in contours:
            count = count +1
            epsilon = 0.1*cv2.arcLength(cont,True)
            approx = cv2.approxPolyDp(cont, epsilon, True)

            if cv2.contourArea(approx) > 5000 and len(approx) == 4:
                cv2.drawContours(image, contours, count,(255,255,255), 10)
                return approx
