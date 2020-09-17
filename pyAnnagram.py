import sys

phraseOne = input('Enter a phrase or word: ')
phraseTwo = input('Enter a second phrase or word to see if it is an annagram of the first: ')

print('The first phrase or word you entered is: ' + phraseOne)
print('The second phrase or word you entered is: ' + phraseTwo)

# Check if user input is empty
if phraseOne is None or phraseTwo is None:
    print("One or more of phrases or words contains no text. Goodbye")
    sys.exit()
else:
    # Remove whitespace from all phrases and words
    phraseOneStripped = phraseOne.replace(" ", "")
    phraseTwoStripped = phraseTwo.replace(" ", "")

    # Make entered phrases or words lowercase
    phraseOneLower = phraseOneStripped.lower()
    phraseTwoLower = phraseTwoStripped.lower()

    print(phraseOneLower, phraseTwoLower)

    """# Compare phrases or words to verify they are annagrams
    if phraseOneLower == phraseTwoLower:
        print(phraseOne + " and" + phraseTwo + " are anagrams and contain the same characters!")
    else:
        print("The phrases or words you entered are not anagrams and don't contain the same characters. Goodbye")
        sys.exit()"""