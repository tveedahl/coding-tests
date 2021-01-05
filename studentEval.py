class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    pass


class FileEmpty(StudentsDataException):
    pass


class StudentEval:

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
                # print(student[0], student[1])
                studentEvalDict.append(student)
                print(studentEvalDict[studentCount][0])
                if student[0] in studentEvalDict[studentCount] and student[1] == studentEvalDict[studentCount]:
                    print("in")
                studentCount = studentCount + 1
            # print(studentEvalDict)
        except IOError:
            pass


impStudentEval = StudentEval()

impStudentEval.readAndSum()
