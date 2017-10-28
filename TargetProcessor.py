import numpy as np
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
    def __init__():
        global RectHeight
        global RectWidth
        global focalLen
        global horizCent
        global vertiCent
        RectHeight = 500
        RectWidth = 200
        focalLen = 486
        horizCent = 200
        vertiCent = 333
    def loadTarget(target):
        global imgWidth
        global imgHeight
        global offsetX
        global offsetY
        imgWidth = Target.target.getWidth()
        imgHeight = Target.target.getHeight()
        imgCenter = target.getCenter()
        RectcentX = imgCenter[0]
        RectcentY = imgCenter[1]
        offsetX = math.fabs(RectcentX - horizCent)
        offsetY = math.fabs(RectcentY - vertiCent)

    def findDistance():
        dist = RectWidth * focalLen / imgWidth
        return (dist)

    def findAzimuth():
        azimuth = np.arctan(offsetX/ focalLen)*180/math.pi
        return (azimuth)

    def findAltitude():
        altit = np.arctan(offsetY/ focalLen)*180/math.pi
        return (altit)