from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    boardDisp = (f"""
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+      
""")
    return boardDisp


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    
    userChoice = 0
    while not userChoice:
        try: 
            tuple = ()
            userChoice = int(input("Enter your move: "))
            userBoardPosition = userChoice%3
            if userBoardPosition == 0: userBoardPosition = 3
            if userChoice < 1 or userChoice > 9:
                print("Enter a value between 1 and 9.")
                userChoice = 0
                continue

            if userChoice >= 1 and userChoice <= 3:
              tuple = (1,userChoice)
            elif userChoice >= 4 and userChoice <=6:
              tuple = (2, userBoardPosition)
            elif userChoice >= 7 and userChoice <=9:
              tuple = (3, userBoardPosition) 

            if tuple in make_list_of_free_fields(board):
              board[tuple[0]-1][tuple[1]-1] = "O"
            else:
              print("That position is not available.")
              userChoice = 0
              continue
        except:
            print("Value must be a number.")
            exitCondition = input("Do you wish to exit? Y/N")
            if exitCondition == "Y" or exitCondition == "y":
                exit()
            userChoice = 0
            continue
        
    return userChoice


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    freeSquares = []
    for i,n in enumerate(board):
        for p,m in enumerate(board):
            if type(board[i][p]) is int:
                freePosition = (i+1,p+1)
                freeSquares.append(freePosition)
    return freeSquares


def victory_for(board, sign=""):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    #check rows, columns, diag and reverse diag
    winner = ""
    
    for i in board: #row
        if i[0] == i[1] and i[1] == i[2]:
            winner = i[0]
    for i in range(len(board[0])): #column
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            winner = board[0][i]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]: #diagonal
        winner = board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]: #reverse diagonal
        winner = board[0][2]
    
    #didn't want to limit check to only one player, but was told to use a sign argument and didn't want to not use the parameter
    if sign:
        pass
    
    return winner


def draw_move(board):
    # The function draws the computer's move and updates the board.
    
    availableList = make_list_of_free_fields(board)
    computerMove = availableList[randrange(len(availableList))]
    row = computerMove[0]
    column = computerMove[1]

    while computerMove:
      computerMove = board[row-1][column-1]
      board[row-1][column-1] = "X"
      break
    
    return computerMove

def endGame(board,player):
    if victory_for(board, player):
        print(f"Winner is {victory_for(board,player)}")
        return True
    if not make_list_of_free_fields(board):
        print("It's a draw!")
        return True

board = [[i for i in range(1,4)] for j in range(1,4)]
board[1] = [i for i in range(4,7)]
board[2] = [i for i in range(7,10)]

player = "O"

while True:
    print(f"Computer move is: {draw_move(board)}")
    print(display_board(board))
    if endGame(board,player): break
    enter_move(board)
    print(display_board(board))
    if endGame(board,player): break
    
print("Terminating...")