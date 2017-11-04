from CmdLineInterface import CmdLineInterface
from Target import Target
from TargetDetector import TargetDetector
from TargetProcessor import TargetProcessor
from VideoDevice import VideoDevice
from GUIManager import GUIManager
from AppConfig import AppConfig

import cv2
import sys

detector = TargetDetector()
processor = TargetProcessor()
camera = VideoDevice()
cmdinp = ["main.py", "-d", "0", "--no-networking", "--isDebug"]

interface = CmdLineInterface(cmdinp)
config = interface.getConfig()
gui = GUIManager()

camera.startCapture(config.getDeviceID())


if(config.getIsDebug()):
    print("Camera is ready\n")
    #gui.threshWindow()

loop = 1

while(cv2.waitKey(30) != 27):
    print ("While Loop %s \n") % loop
    thIn = [0, 180, 228, 255]
    detector.threshInputs(thIn)

    image = camera.getImage()
		
    if(config.getIsDebug()):
        print("Image Read\n")

    detected = detector.TargetDetect(image)
    
    if(config.getIsDebug()):
        print("Image Analyzed\n")
        
    
    if (detector.getFound() == True):
        
        target = Target(detected)
    	
        if(config.getIsDebug()):
            print("Image Processed by Target Detector\n")
    
        if(config.getIsDebug()):
            print ("Image Being Processed by Target Processor\n")
    
        processor.loadTarget(target)
        
        if(config.getIsDebug()):
            print("Target Loaded\n")
    
        distance = processor.findDistance()
    
        if(config.getIsDebug()):
            print("Distance Calculated\n")
    
        azimuth = processor.findAzimuth()
    
        if(config.getIsDebug()):
            print("Azimuth Calculated\n")
    
        altitude = processor.findAltitude()
    
        if(config.getIsDebug()):
            print("Altitude Calculated\n")
    
        if(config.getIsDebug()):
            print("Image Processed by TargetProcessor\n")
    
        dis = "distance: %s" % distance
        azi = "azimuth: %s" % azimuth
        alt = "altitude: %s" % altitude
        
    else:
        dis = "Not Found"
        azi = "Not Found"
        alt = "Not Found"
        wid = "Image Width: %s" % target.getWidth()
        hue = "Hue: %s - %s" % (thIn[0], thIn[1])
        val = "Value: %s - %s" % (thIn[2], thIn[3])
    
    gui.setImage(image)
    gui.setText(hue, -2)
    gui.setText(val, -1)
    gui.setText(wid, 0)
    gui.setText(dis, 1)
    gui.setText(azi, 2)
    gui.setText(alt, 3)
    cv2.imshow("Targeting", gui.getImage())
    loop += 1

cv2.destroyAllWindows()
