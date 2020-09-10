import sys

try:
    # Prompt user for line of text
    userTxt = input("Enter a line of text:")

    # Prompt user for a shift value and check for exceptions
    userShiftVal = int(input("Enter an integer between 1 and 25:"))

    # Encrypt user entered text using user entered shift value
    cipher = ''
    if 1 <= userShiftVal <= 25:
        for i in userTxt:
            # If i is whitespace
            if i == ' ':
                cipher = cipher + i
            # If i is uppercase
            elif i.isupper():
                cipher = cipher + chr((ord(i) + userShiftVal - 65) % 26 + 65)
            # If i is otherwise
            else:
                cipher = cipher + chr((ord(i) + userShiftVal - 97) % 26 + 97)
        print(cipher)
    else:
        sys.exit("Entered value is not in range. Goodbye")
except ValueError:
    sys.exit("The value you entered is not valid")