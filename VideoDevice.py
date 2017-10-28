import cv2

class VideoDevice:

	def startCapture(self, id):
    		self.camera = VideoDevice(id)

	def getImage(self):
    		self.camera.takeImage()
    		return self.image


	def takeImage(self):
    		self.image = cv2.VideoCapture(self.id)

