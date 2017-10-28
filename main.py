from CmdLineInterface import CmdLineInterface
from Target import Target
from TargetDetector import TargetDetector
from TargetProcessor import TargetProcessor
from VideoDevice import VideoDevice
from GUIManager import GUIManager

import cv2

detector = TargetDetector.TargetDetector()
processor = TargetProcessor.TargetProcessor()
camera = VideoDevice.VideoDevice()
cmdinp = ["name", "-d", "0", "--no-networking", "--debug"]
interface = CmdLineInterface.CmdLineInterface(cmdinp)
config = interface.getConfig()
gui = GUIManager.GUIManager()

if(config.getIsDevice()):
	camera.startCapture(config.getDeviceID())

	if(config.getIsDebug()):
		print("Camera is ready\n")

	loop = 1

	while(cv2.waitKey(30) != 27):
		
		print "While Loop # %s \n" % loop

		image = camera.getImage()
		
		if(config.getIsDebug()):
			print("Image Read\n")

		target = Target(detector.TargetDetect(image))
	
		if(config.getIsDebug()):
			print("Image Processed by Target Detector\n")

          	if(config.getIsDebug()):
           		print "Image Being Processed by Target Processor\n"

		processor.loadTarget(target)

  	        if(config.getIsDebug()):
  	           	print("Target Loaded\n")

  	        distance = processor.getDistance()

  	        if(config.getIsDebug()):
			print("Distance Calculated\n")

		azimuth = processor.getAzimuth()

           	if(config.getIsDebug()):
                	print("Azimuth Calculated\n")

		altitude = processor.getAltitude()

           	if(config.getIsDebug()):
            		print("Altitude Calculated\n")

  	        if(config.getIsDebug()):
			print("Image Processed by TargetProcessor\n")

		dis = "distance: %s" % distance
		azi = "azimuth: %s" % azimuth
		alt = "altitude: %s" % altitude
		target.drawCnts(image)

		gui.setImage(image)
		gui.setText(dis, 1)
		gui.setText(azi, 2)
		gui.setText(alt, 3)
		
