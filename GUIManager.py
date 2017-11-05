import cv2

class GUIManager:
    
    def __init__(self): #creates a targeting window to place the live feed
        cv2.namedWindow("Targeting", cv2.WINDOW_AUTOSIZE)
    
    def threshWindow(self): #creates a threshholding window to place threshholding image
        cv2.namedWindow("Thresh", cv2.WINDOW_AUTOSIZE)

    def setImage(self, inputImage): #adds an image to the object
        self.image = inputImage
        
    def setText(self, imageText, row): #adds text to the image based on inputted text
        cv2.putText(self.image, imageText, (10, 400 + (row*20)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 0, 255), 1)
        #the words are placed in the bottom left, using row to move the words further down. row = 0 is somewhere in the middle of the image
    def getImage(self): #returns the image from the object
        return self.image