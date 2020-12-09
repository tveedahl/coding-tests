from os import strerror

class CharFreqHist():

    def usrFilePrompt(self):
        global fileName = input("Enter the name of a file to get input from: ")
        return fileName
    
    def readAndCount(self):
        try:
            aFile = self.usrFilePrompt()
            aFileHandle = open(aFile, 'rb')
        except IOError:
            print("Could not read file: ", aFile)

impCharFreqHist = CharFreqHist()
impCharFreqHist.readAndCount()