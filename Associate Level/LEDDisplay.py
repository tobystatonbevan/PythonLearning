def generateDisplay(display = []):
    display = [[' ' for i in range(3)] for p in range(5)]
    display[1][1] = ' '
    display[3][1] = ' '
    return display

def updateDisplayTuple(listGiven):    
    display = generateDisplay()
    for i in listGiven:
        if i == (1,1) or i == (3,1):
            continue
        display[i[0]][i[1]] = '#'
    return display

def getUserChoice(userChoice=''):
    while type(userChoice) != int:
        try:
            userChoice = int(input("Enter value: "))
            if userChoice < 0:
                userChoice = int(input("Enter value greater than 0: "))
        except (ValueError):
            print("Enter a numerical value.")
    return userChoice

def displayUserChoice(userChoice):
    line1 = line2 = line3 = line4 = line5= ''
    for n in str(userChoice):
        n = int(n)
        line1 += ''.join(updateDisplayTuple(numList[n])[0])+' '
        line2 += ''.join(updateDisplayTuple(numList[n])[1])+' '
        line3 += ''.join(updateDisplayTuple(numList[n])[2])+' '
        line4 += ''.join(updateDisplayTuple(numList[n])[3])+' '
        line5 += ''.join(updateDisplayTuple(numList[n])[4])+' '
    return line1,line2,line3,line4,line5

zero = [(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,2),(3,0),(3,2),(4,0),(4,1),(4,2)]
one = [(0,2),(1,2),(2,2),(3,2),(4,2)]
two = [(0,0),(0,1),(0,2),(1,2),(2,0),(2,1),(2,2),(3,0),(4,0),(4,1),(4,2)]
three = [(0,0),(0,1),(0,2),(1,2),(2,0),(2,1),(2,2),(3,2),(4,0),(4,1),(4,2)]
four = [(0,0),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2),(3,2),(4,2)]
five = [(0,0),(0,1),(0,2),(1,0),(2,0),(2,1),(2,2),(3,2),(4,0),(4,1),(4,2)]
six = [(0,0),(0,1),(0,2),(1,0),(2,0),(2,1),(2,2),(3,0),(3,2),(4,0),(4,1),(4,2)]
seven = [(0,0),(0,1),(0,2),(1,2),(2,2),(3,2),(4,2)]
eight = [(i,p) for i in range(5) for p in range(3)]
nine = [(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2),(3,2),(4,0),(4,1),(4,2)]
numList = [zero, one, two, three, four, five, six, seven, eight, nine]

display = generateDisplay()
userChoice = getUserChoice()
line1,line2,line3,line4,line5 = displayUserChoice(userChoice)

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)    
           
#fix random # that appears...