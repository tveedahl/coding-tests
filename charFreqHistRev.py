class CharFreqHist():
    
    def readAndCount(self):
        try:
            global aFileName 
            aFileName = input("Enter the name of a file to get input from: ")
            fileContents = open(aFileName, 'r')
            latCharDictCnt = {
                "a": 0, 
                "b": 0,
                "c": 0,
                "d": 0,
                "e": 0,
                "f": 0,
                "g": 0,
                "h": 0,
                "i": 0,
                "j": 0,
                "k": 0,
                "l": 0,
                "m": 0,
                "n": 0,
                "o": 0,
                "p": 0,
                "q": 0,
                "r": 0,
                "s": 0,
                "t": 0,
                "u": 0,
                "v": 0,
                "w": 0,
                "x": 0,
                "y": 0,
                "z": 0
            }
            for line in fileContents:
                lowerLine = line.lower()
                for char in lowerLine:
                    for i, j in latCharDictCnt.items():
                        if char == str(i):
                            latCharDictCnt[char] += 1 
            fileContents.close()
            return latCharDictCnt
        except IOError:
            print("Could not read file: ", aFileName)
    
    def sortHist(self, histDict):
        latCharDicSort = sorted(histDict.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
        return latCharDicSort

    def writeHist(self):
        hist = self.readAndCount()
        sortedHist = self.sortHist(hist)
        fileToWrite = open(aFileName + ".hist", "w") 
        for item in sortedHist:
            if item[1] > 0:
                try:
                    fileToWrite.write(item[0] + " -> " + str(item[1]) + "\n")
                except IOError:
                    print("Could not write to file: ", fileToWrite)
        print(fileToWrite.name, " has been written!")
        fileToWrite.close()

impCharFreqHist = CharFreqHist()
impCharFreqHist.writeHist()