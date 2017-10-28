from AppConfig import AppConfig

class CmdLineInterface:
	def printUsage(self):
		print( "Usage: program (-d <device_num>) [--no-networking] [--headless] [--debug]")

	def __init__(self, inargs):
		while(True):
			self.arg = inargs[1]
			self.config = AppConfig()
			self.cmdnum = 3
		
			if len(inargs) < 3:
				if (self.arg == "-d" and isinstance(inargs[2], int)):
					self.config.setIsDevice(1)
					self.config.setDeviceID(inargs[2])
				else:
					self.printUsage()
					break

			elif (len(inargs) > 3):
				if (inargs[self.cmdnum] == "--no-networking"):
					self.config.setIsNetworking(0)
					self.cmdnum += 1
					if (self.cmdnum == len(inargs)):
						break
				if (inargs[self.cmdnum] == "--headless"):
					self.config.setIsHeadless(1)
					self.cmdnum += 1
					if (self.cmdnum == len(inargs)):
						break
				if (inargs[self.cmdnum] == "--isDebug"):
					self.config.setIsDebug(1)
					self.cmdnum += 1
					if (self.cmdnum == len(inargs)):
						break
			else:
				self.printUsage()
				break
			
	def getConfig(self):
		return self.config
	