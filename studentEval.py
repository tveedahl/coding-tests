import os
from collections import Counter


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
                repStu = []
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
                            pointsTemp = rplPoints
                            nameList.append(names)
                            stuReport.append(stuEvalIntl)
                        else:
                            stuEvalSum = rplPoints + pointsTemp
                            stuEvalSummed = {
                                count: {
                                    "first": lineSplt[0],
                                    "last": lineSplt[1],
                                    "points": stuEvalSum
                                }
                            }
                            stuReport.append(stuEvalSummed)
                            repStu.append(stuEvalIntl)
                            count += 1    
                repStuCount = 0
                while repStuCount < len(repStu):
                    if repStuCount == 1:
                        stuUptKey = {
                            0: {
                                "first": repStu[1][1]["first"],
                                "last": repStu[1][1]["last"],
                                "points": repStu[1][1]["points"] 
                            }
                        }
                        repStu.append(stuUptKey)
                        del repStu[1]
                    repStuCount += 1
                for i in stuReport:
                    if type(i) != float:
                        for k, v in i.items():
                            # print(v["first"], v["last"], v["points"])
                            pass
        except IOError:
            print("No file by that name exists in your current directory")


impStudentEval = StudentEval()

impStudentEval.readAndSum()
