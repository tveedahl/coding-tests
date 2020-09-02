# Define display pattern list
zero = '###\n#' + ' ' + '#\n#' + ' ' + '#\n#' + ' ' + '#\n###'
one = '#\n#\n#\n#\n#'
two = '###\n  #\n###\n#  \n###'
three = '###\n  #\n###\n  #\n###'
four = '# #\n# #\n###\n  #\n  #'
five = '###\n#  \n###\n  #\n###'
six = '###\n#  \n###\n# #\n###'
seven = '###\n  #\n  #\n  #\n  #'
eight = '###\n# #\n###\n# #\n###'
nine = '###\n# #\n###\n  #\n  #'
patList = [zero, one, two, three, four, five, six, seven, eight, nine]

# Get number input from user
numput = input("Enter a nonzero number:")

# Loop through numput and print display format
for digit in numput:
    print(patList[int(digit)])