"""import numpy as np
import math

from Target import Target
class TargetProcessor:
    RectHeight = 0
    RectWidth = 0
    focalLen = 0
    horizCent = 0
    vertiCent = 0
    imgWidth = 0
    imgHeight = 0
    def __init__(self):
        global RectHeight
        global RectWidth
        global focalLen
        global horizCent
        global vertiCent
        RectHeight = 0.02
        RectWidth = 0.05
        focalLen = 480
        horizCent = 240
        vertiCent = 320
    def loadTarget(self, target):
        global imgWidth
        global imgHeight
        global offsetX
        global offsetY
        imgWidth = target.getWidth()
        imgHeight = target.getHeight()
        imgCenter = target.getCenter()
        RectcentX = imgCenter[0]
        RectcentY = imgCenter[1]
        offsetX = float(RectcentX - horizCent)
        offsetY = float(-1*(RectcentY - vertiCent))
        

    def findDistance(self):
        if imgWidth == 0:
            return (0)
            print("hihih")
        else:
            dist = float(RectWidth * focalLen) / imgWidth
            return (dist)

    def findAzimuth(self):
        azimuth = np.arctan(offsetX/ focalLen)*180/math.pi
        return (azimuth)

    def findAltitude(self):
        altit = np.arctan(offsetY/ focalLen)*180/math.pi
        return (altit)"""
        
import numpy as np
import math

from Target import Target
class TargetProcessor:
    def __init__(self):
        self.RectHeight = 0.02
        self.RectWidth = 0.05
        self.focalLen = 480
        self.horizCent = 240
        self.vertiCent = 320
    def loadTarget(self, target):
        self.imgWidth = target.getWidth()
        self.imgHeight = target.getHeight()
        imgCenter = target.getCenter()
        RectcentX = imgCenter[0]
        RectcentY = imgCenter[1]
        self.offsetX = float(RectcentX - self.horizCent)
        self.offsetY = float(-1*(RectcentY - self.vertiCent))
        

    def findDistance(self):
        if self.imgWidth == 0:
            self.imgWidth = 1
        dist = float(self.RectWidth * self.focalLen) / self.imgWidth
        return (dist)

    def findAzimuth(self):
        azimuth = np.arctan(self.offsetX/ self.focalLen)*180/math.pi
        return (azimuth)

    def findAltitude(self):
        altit = np.arctan(self.offsetY/ self.focalLen)*180/math.pi
        return (altit)