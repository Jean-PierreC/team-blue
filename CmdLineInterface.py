from AppConfig import AppConfig

class CmdLineInterface:
    #is the logic for breaking down an input from the cmdline and using it to vary an AppConfig object
    def printUsage(self):
        print( "Usage: program (-d <device_num>) [--no-networking] [--headless] [--debug]")
        #if there is an error with the cmdline input, it outputs this string to show the usage of the program

    def __init__(self, inargs):
        self.config = AppConfig() #creates an AppConfig object to store values
        if (inargs[1] == "-d"): #checks if -d was inputted as the first argument
            self.config.setIsDevice(1) #sets that there is a device (1)
            idnum = (int)(inargs[2])
            self.config.setDeviceID(idnum) #sets deviceID to the second input as a integer
        else: #cmdline error
            self.printUsage()

        if (len(inargs) > 3): #if there are more than just -d and int
            count = 0
            for darg in inargs: #for loop to check each input after the -d int
                if (darg == "--no-networking"): #if the argument being checked is no-networking, set it to 0
                    self.config.setIsNetworking(0)

                elif (darg == "--headless"): #if the argument being checked is headless, set it to 1
                    self.config.setIsHeadless(1)

                elif (darg == "--isDebug"): #if the argument being checked is isDebug, set it to 1
                    self.config.setIsDebug(1)

                else: #if an unknown word was entered
                    if (count > 2): #if the for loop is not on -d or int, first 2 arguments, cmdline error
                        self.printUsage()
                        break

        else:
            self.config.setIsNetworking(1)
            self.config.setIsHeadless(0)
            self.config.setIsDebug(0)

    def getConfig(self): #outputs the AppConfig object with all the stored values
        return self.config
