board = []
validBoard = True

for i in range(9):
    row = input(f"Enter the values for row {i+1}: ")
    while len(row) != 9 or not row.isnumeric():
        row = input(f"Enter the values for row {i+1}: ")
    board.append(row)

#test data
#board = ['295743861','431865927','876192543','387459216','612387495','549216738','763524189','928671354','154938672']
#board = ['111111111','222222222','333333333','444444444','555555555','666666666','777777777','888888888','999999999']

while validBoard:
    #check row and validate board
    for i in board:
        sum = 0
        for n in range(9):
            sum += int(i[n])
        if sum != 45:
            validBoard = False
            break
        else:
            validBoard = True

    for n in range(9):
        col = 0
        for i in board:
            col += int(i[n])
        if col != 45:
            validBoard = False
            break
        else:
            validBoard = True

    #build subsquares
    squares = []
    for row in range(0,9,3):
        for col in range(0,9,3):
            subSquareList = []
            for n in range(row,row+3): #list element which is string
                str = ''
                subSquareContent = []
                for p in range(col,col+3): #string elements
                    str += board[n][p]
                subSquareContent.append(str)
                subSquareList.append(subSquareContent)
            squares.append(subSquareList)
    #check sum of subsqaure value and validate board
    for p in range(9):
        totalForSquare = 0
        for i in range(3):
            sum = 0
            for i in squares[p][i][0]:
                    sum += int(i)
            totalForSquare += sum
        if totalForSquare != 45:
            validBoard = False
            break
        else:
            validBoard = True
    break

if validBoard: print("Yes")
else: print("No")