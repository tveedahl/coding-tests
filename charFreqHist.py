from os import strerror

class CharFreqHist():
    
    def readAndCount(self):
        try:
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
            for x, y in latCharDictCnt.items():
                if y > 0:
                    print(x + " -> " + str(y))
        except IOError:
            print("Could not read file: ", aFileName)

impCharFreqHist = CharFreqHist()
impCharFreqHist.readAndCount()