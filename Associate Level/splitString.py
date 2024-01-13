def mysplit(strng):
    words = []
    lastSpace = 0
    
    if strng.isspace():
        return words
    
    for i,n in enumerate(strng):
        if ord(n) == 32:
            words.append(strng[lastSpace:i])
            lastSpace = i+1
        elif i+1 == len(strng):
            words.append(strng[lastSpace:])
    
    return words

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))