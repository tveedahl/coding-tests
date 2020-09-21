import sys

# Prompt user for needle string
needleStr = input("Enter a string to be searched for: ")

# Prompt user for haystack string
haystackStr = input("Enter a string to search for your last string within: ")

# Determine substring start and end positions
subStart = haystackStr.find(needleStr[:1])
subEnd = len(haystackStr)
subStr = haystackStr[subStart:subEnd]

# Search haystackStr for needleStr
if subStart != -1:
    count = 0
    for char in needleStr:
        if subStr.find(char) != -1:
            count += 1
        else:
            sys.exit("The string, " + needleStr + " does not exist in " + haystackStr)
    print("The string, " + needleStr + ", exists in " + haystackStr)