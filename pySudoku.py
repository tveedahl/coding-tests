import sys
import numpy

# Prompt user to enter completed sudoku and create 2 copies
print("Enter a 9 x 9 completed sudoku puzzle to check for its correctness (Press Ctrl-D when done): ")
sudokuList = sys.stdin.readlines()
sudokuListTwo = sudokuList
sudokuListThree = sudokuList

# Cast sudokuList elements to int
sudokuListCount = 0
for element in sudokuList:
    sudokuList[sudokuListCount] = int(sudokuList[sudokuListCount])
    sudokuListCount += 1

# Iterate through and validate sudokuList rows for correctness
sudokuIntList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for iterOne in sudokuList:
    # Cast row ints to lists
    rowList = list(map(int, str(iterOne)))
    # Check if numbers 1-9 are in user entered rows
    if all(item in sudokuIntList for item in rowList):
        pass
    else:
        sys.exit("The sudoku puzzle you entered is not correct. Goodbye")

# Iterate through and validate sudokuListTwo columns for correctness
for iterTwo in sudokuListTwo:
    # Cast row ints to lists
    columnList = list(map(int, str(iterTwo)))
    for column in columnList:
        # Check if numbers 1-9 are in user entered rows
        if all(item in sudokuIntList for item in columnList):
            pass
        else:
            sys.exit("The sudoku puzzle you entered is not correct. Goodbye")

# Iterate through and validate sudokuListThree 3 x 3 tiles for correctness
tileCount = 1
threeByThree = numpy.array([[], [], []])
for tileRow in sudokuListThree:
    # Cast row ints to lists
    tileList = list(map(int, str(tileRow)))
    if tileCount < 4:
        for tileCol in tileList[0:3]:
            tileColList = numpy.array(tileCol)
            print(type(tileColList))
            threeByThree.append([[tileColList[0:3]], [tileColList[3:6]], [tileColList[6:9]]])
            print(threeByThree)
    elif 4 <= tileCount < 7:
        continue
    elif 7 <= tileCount < 10:
        continue
    tileCount += 1

# Print sudokuList validation report
# print("All rows of your entered sudoku puzzle contain numbers 1-9\n")
# print("All columns of your entered sudoku puzzle contain numbers 1-9")