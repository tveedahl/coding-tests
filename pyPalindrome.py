import sys

# Prompt user for text to check for palindrome
userTxt = input('Enter some text and check if it is a palindrome:')

# Check userTxt to see if it is a palindrome
if not userTxt:
    print('You entered nothing. Goodbye')
    sys.exit()
else:
    # Strip whitespace from userTxt
    userTxtStripped = userTxt.replace(" ", "")

    # Make userTxtStripped all lowercase
    userTxtLower = userTxtStripped.lower()

    if not userTxtLower.isalpha():
        print('You entered non alphabetic text. Goodbye')
        sys.exit()
    else:
        if userTxtLower == userTxtLower[::-1]:
            print('Yay, you entered a palindrome!')
        else:
            print('The text you entered is not a palindrome. Goodbye')
            sys.exit()