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
                student = [
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
                    studentEvalList.append(student)
                else:
                    stuEvalSum = rplPoints + studentEvalList[count][2]
                    student = [
                        lineSplt[0],
                        lineSplt[1],
                        stuEvalSum
                    ]
                    if lineSplt[0] not in studentEvalList:
                        studentEvalList.append(student)
                    count += 1     
            counter = 0
            while counter < len(studentEvalList):
                print(studentEvalList[counter][0], studentEvalList[counter][1], studentEvalList[counter][2])
                counter += 1
        except IOError:
            print("No file by that name exists in your current directory")


impStudentEval = StudentEval()

impStudentEval.readAndSum()
