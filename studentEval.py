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
            aFileName = input("Enter the name of a text file to get input from:")
            fileHndl = open(aFileName, 'r')
            stuEvalIntl = {}
            stuEvalSummed = {}
            nameList = []
            fileLines = fileHndl.readlines()
            count = 0
            for line in fileLines:
                lineSplt = line.split(" ")
                rplPoints = float(lineSplt[2].replace("\n", ""))
                stuEvalIntl = {
                    count: {
                        "first": lineSplt[0],
                        "last": lineSplt[1],
                        "points": rplPoints
                    }
                }
                names = [
                    lineSplt[0],
                    lineSplt[1]
                ]
                if names not in nameList:
                    nameList.append(names)
                else:
                    stuEvalSum = rplPoints + stuEvalIntl[count]["points"]
                    stuEvalSummed = {
                        count: {
                            "first": lineSplt[0],
                            "last": lineSplt[1],
                            "points": stuEvalSum
                        }
                    }
                    for k, v in stuEvalSummed.items():
                        print(k, v)
                    count += 1
            # print(stuEvalSummed)
        except IOError:
            print("No file by that name exists in your current directory")


impStudentEval = StudentEval()

impStudentEval.readAndSum()
