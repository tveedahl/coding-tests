class StudentEval():

    def readAndSum(self):
        try:
            global aFileName 
            aFileName = input("Enter the name of a text file to get input from: ")
            fileHndl = open(aFileName, 'r')
            studentEvalDict = {"Student": []}
            fileLines = fileHndl.readlines()
            for line in fileLines:
                lineSplt = line.split(" ")
                studentEvalDict["Student"].append([lineSplt[0], lineSplt[1], lineSplt[2]])
            print(studentEvalDict)
        except IOError:
            pass

impStudentEval = StudentEval()
impStudentEval.readAndSum()