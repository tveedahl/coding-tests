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
            studentEvalList = []
            nameList = []
            fileLines = fileHndl.readlines()
            count = 0
            for line in fileLines:
                lineSplt = line.split(" ")
                rplPoints = float(lineSplt[2].replace("\n", ""))
                studentIntl = [
                    lineSplt[0],
                    lineSplt[1],
                    rplPoints
                ]
                names = [
                    lineSplt[0],
                    lineSplt[1]
                ]
                if names not in nameList:
                    nameList.append(names)
                    studentEvalList.append(studentIntl)
                else:
                    stuEvalSum = rplPoints + studentEvalList[count][2]
                    studentSummed = [
                        lineSplt[0],
                        lineSplt[1],
                        stuEvalSum
                    ]
                    if lineSplt[0] not in studentEvalList:
                        studentEvalList.append(studentSummed)
                        # studentEvalList.pop(count)
                    count += 1
            stuCount = 0
            while stuCount < len(studentEvalList):
                print(studentEvalList[stuCount][0], studentEvalList[stuCount][1], studentEvalList[stuCount][2])
                stuCount += 1
        except IOError:
            print("No file by that name exists in your current directory")


impStudentEval = StudentEval()

impStudentEval.readAndSum()
