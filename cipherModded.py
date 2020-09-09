import sys

# Prompt user for line of text
userTxt = input("Enter a line of text:")
print(userTxt)
sys.exit()

# Prompt user for a shift value and check for exceptions
try:
    userShiftVal = int(input("Enter an integer between 1 and 25:"))
    if 1 <= userShiftVal <= 25:
        print(userTxt, userShiftVal)
        for i in userTxt:
            # Find character unicode value
            iUni = ord(i)
            # print(iUni + " ")
    else:
        sys.exit("Entered value is not in range. Goodbye")
except ValueError:
    print("The value you entered is not valid")