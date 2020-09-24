import sys

# Prompt user to enter completed sudoku and create 2 copies
print("Enter a 9 x 9 completed sudoku puzzle to check for its correctness (Press Ctrl-D when done): ")
sudokuList = sys.stdin.readlines()
print(sudokuList)
sudokuListTwo = sudokuList
sudokuListThree = sudokuList

# Cast sudokuList elements to int
sudokuListCount = 0
for element in sudokuList:
    sudokuList[sudokuListCount] = int(sudokuList[sudokuListCount])
    sudokuListCount += 1

# Iterate through and validate sudokuList for correctness
sudokuIntList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for iterOne in sudokuList:
    # Cast row ints to lists
    rowList = list(map(int, str(iterOne)))
    # Check if numbers 1-9 are in user entered rows
    if all(item in sudokuIntList for item in rowList):
        pass
    else:
        sys.exit("The sudoku puzzle you entered is not correct. Goodbye")

# Iterate through sudokuList columns
"""for iterTwo in sudokuListTwo:
    for column in iterTwo:
        print(column)"""

# Print sudokuList validation report
# print("All rows of your entered sudoku puzzle contain numbers 1-9")