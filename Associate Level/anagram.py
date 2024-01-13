textOne = input("Enter first word: ")
textTwo = input("Enter second word: ")
anagram = True

if not textOne.isspace() and not textTwo.isspace():
    textOne = textOne.lower().replace(' ','')
    textTwo = textTwo.lower().replace(' ','')

listOne = list(textOne)
listTwo = list(textTwo)

if len(listOne) == len(listTwo):
    for i in listOne:
        if i not in listTwo: 
            anagram = False
            break
    for i in listTwo:
        if i not in listOne:
            anagram = False
            break
else: 
    anagram = False

if anagram: print("Anagrams")
else: print("Not anagrams")