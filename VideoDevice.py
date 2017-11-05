import cv2

class VideoDevice:
    camera = None
    def startCapture(self, id):
        self.camera = cv2.VideoCapture(id) 
        #makes camera into a cv2.VideoCapture object, premade by cv, and inputs device id

    def getImage(self):
        ret, image = self.camera.read() #uses read method from cv2.VideoCapture to output image from camera
        return image


	

