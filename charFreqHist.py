from os import strerror

class CharFreqHist():
    
    def readAndCount(self):
        try:
            aFileName = input("Enter the name of a file to get input from: ")
            fileContents = open(aFileName, 'r')
            latCharCount = 0
            for line in fileContents:
                lowerLine = line.lower()
                for char in lowerLine:
                    print(char)
            fileContents.close()
        except IOError:
            print("Could not read file: ", aFileName)

impCharFreqHist = CharFreqHist()
impCharFreqHist.readAndCount()