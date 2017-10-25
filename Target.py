class Target():
    def _init_ (final)
        
        contour = final
        temp = final[0]
    
    def targetLoad:
        avgX = 0
        avgY = 0
        minX = temp[0][0]
        maxX = temp[0][0]
        minY = temp[0][1]
        maxY = temp[0][1]
        for p in final:
            if p[0][0] < minX:
                minX = p[0][0]
            if p[0][0] > maxX:
                maxX = p[0][0]
            if p[0][1] < minY:
                minY = p[0][1]
            if p[0][1] > maxY:
                maxY = p[0][1]

        width = maxX-minX
        height = maxY-minY
        avgX = (maxX+minX)/2
        avgY = (maxY+minY)/2
        centerPoint = [avgX, avgY]
    
    def getWidth:
        return width
    def getHeight:
        return height
    def getCenter:
        return centerPoint
   
