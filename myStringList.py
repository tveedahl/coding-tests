def mysplit(strng):
    if strng:
        splitWordList = []
        combChars = ''
        for char in strng:
            #if char is not whitespace
            if not char.isspace() and char.isalpha():
                combChars = combChars + char
            else:
                continue
            splitWordList.append(combChars)
    else:
        return []
    return splitWordList

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))