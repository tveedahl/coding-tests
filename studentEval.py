import os


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
            if os.stat(aFileName).st_size == 0:
                raise FileEmpty("File is empty")
            else:
                fileHndl = open(aFileName, 'r')
                stuEvalIntl = {}
                stuEvalSummed = {}
                nameList = []
                stuReport = []
                fileLines = fileHndl.readlines()
                count = 0
                for line in fileLines:
                    if line == "\n":
                        raise BadLine("Line is empty")
                    else:
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
                            lineSplt[1],
                        ]
                        if names not in nameList:
                            nameList.append(names)
                            stuReport.append(stuEvalIntl)
                        else:
                            # stuEvalSum = rplPoints + stuEvalIntl[count]["points"]
                            stuEvalSum = rplPoints + names[2]                    
                            print(rplPoints, stuEvalSum)
                            stuEvalSummed = {
                                count: {
                                    "first": lineSplt[0],
                                    "last": lineSplt[1],
                                    "points": stuEvalSum
                                }
                            }
                            stuReport.append(stuEvalSum)
                            count += 1
                    """for i in stuReport:
                        if type(i) != float:
                            for k, v in i.items():
                                print(v["first"], v["last"], v["points"])"""
        except IOError:
            print("No file by that name exists in your current directory")


impStudentEval = StudentEval()

impStudentEval.readAndSum()
