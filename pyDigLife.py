import sys

# Prompt user for birthdate
userBDate = input("Enter your birthdate (i.e. YYYYMMDD, YYYYDDMM, or MMDDYYYY): ")

# Iterate through and sum entered birthday by digit
bDateSum = 0
for digit in userBDate:
    bDateSum += int(digit)

# Check if sum is greater than one digit and if so sum again, else print sum
if len(str(bDateSum)) > 1:
    bDateSumTwo = 0
    for sumDig in str(bDateSum):
        bDateSumTwo += int(sumDig)
    print("Your digit of life is: " + str(bDateSumTwo))
else:
    print("Your digit of life is: " + str(bDateSum))