import cv2

class Target:
    
    def __init__ (self, temp):
        

        avgX = 0

        avgY = 0
  
        minX = temp[0][0][0]

        maxX = temp[0][0][0]
   
        minY = temp[0][0][1]

        maxY = temp[0][0][1]
        
        for p in temp:
            
            if p[0][0] < minX:
                minX = p[0][0]
                print(minX)
            
            if p[0][0] > maxX:
                maxX = p[0][0]
                print(maxX)
			
            if p[0][1] < minY:
                minY = p[0][1]
            
            if p[0][1] > maxY:
                maxY = p[0][1]
        print("spaace")
        print(maxX)
        print(minX)
        self.width = maxX-minX
        
        self.height = maxY-minY
        
        avgX = (maxX+minX)/2
        
        avgY = (maxY+minY)/2
        
        self.centerPoint = [avgX, avgY]
    
   
    def getWidth(self):
        
        return self.width
    
    def getHeight(self):
        
        return self.height
    
    def getCenter(self):
        
        return self.centerPoint

        