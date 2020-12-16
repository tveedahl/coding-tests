class StudentEval():

    def readAndSum(self):
        try:
            global aFileName 
            aFileName = input("Enter the name of a text file to get input from: ")
            fileHndl = open(aFileName, 'r')
            studentEvalDict = {}
            fileLines = fileHndl.readlines()
            for line in fileLines:
                lineSplt = line.split(" ")
                print(studentEvalDict)
            print(studentEvalDict)
        except IOError:
            pass

impStudentEval = StudentEval()
impStudentEval.readAndSum()