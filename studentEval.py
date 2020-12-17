class StudentsDataException(Exception):
	pass

class BadLine(StudentsDataException):
	pass

class FileEmpty(StudentsDataException):
	pass

class StudentEval():

    def readAndSum(self):
        try:
            global aFileName 
            aFileName = input("Enter the name of a text file to get input from: ")
            fileHndl = open(aFileName, 'r')
            studentEvalDict = []
            fileLines = fileHndl.readlines()
            for line in fileLines:
                lineSplt = line.split(" ")
                rplPoints = float(lineSplt[2].replace("\n", ""))
                student = [
                    lineSplt[0],
                    lineSplt[1],
                    rplPoints
                ]
                studentEvalDict.append(student)
                if studentEvalDict.find:
                    print(student)
            #print(studentEvalDict)
        except IOError:
            pass

impStudentEval = StudentEval()
impStudentEval.readAndSum()