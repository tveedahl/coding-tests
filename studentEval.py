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
            studentCount = 0
            for line in fileLines:
                lineSplt = line.split(" ")
                rplPoints = float(lineSplt[2].replace("\n", ""))
                student = [
                    lineSplt[0],
                    lineSplt[1],
                    rplPoints
                ]
                #print(student[0], student[1])
                if student[0] not in studentEvalDict and student[1] not in studentEvalDict:
                    studentEvalDict.append(student)
                    if student[0] == studentEvalDict[0][0] and student[1] == studentEvalDict[0][1]:
                        studentEvalDict[studentCount][2] = studentEvalDict[studentCount][2] + studentEvalDict[studentCount][2]
                studentCount = studentCount + 1
                print(studentEvalDict)
        except IOError:
            pass

impStudentEval = StudentEval()
impStudentEval.readAndSum()