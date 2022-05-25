def PrintBoard (board): #function to print board
    print(' + - + - + - +')
    print(' | ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ')
    print(' + - + - + - +')
    print(' | ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' | ')
    print(' + - + - + - +')
    print(' | ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' | ')
    print(' + - + - + - +')
    print ('------------------')

def SpaceIsFree(position): # checking if current space is free
    if board[position]==' ':
        return True
    else:
        return False

def InsertLetter(letter,position): # how PC inserts letters
    if SpaceIsFree(position):
        board[position] = letter
        PrintBoard(board)
        if (CheckDraw()):
            print ("It's a Draw")
            exit()
        if CheckWin():
            if letter == 'X':
                print ("PC Wins!")
                exit()
            else:
                print ("You Win!")
                exit()       
        return
    else:
        print ("that space isn't free")
        position = int(input("Enter new position: "))
        InsertLetter(letter, position)
        return

def CheckWin(): #checking if someone won the game
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def CheckWhoWon(mark): # checking who won the game
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

def CheckDraw(): # checking if game is draw
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

def PlayerMove(): #how player makes move
    position = int(input("Enter position for 'O' :"))
    InsertLetter(player,position)
    return

def PcMove(): # how PC makes move
    BestScore = -800
    BestMove = 0
    for key in board.keys():
        if (board[key]== ' '):
            board[key] = Pc
            Score = MiniMax(board,0,False)
            board[key] = ' '
            if (Score > BestScore):
                BestScore = Score
                BestMove = key
    InsertLetter(Pc, BestMove)
    return

def MiniMax(board, depth, isMaximizing): # minimax algorithm
    if (CheckWhoWon(Pc)):
        return 1
    elif (CheckWhoWon(player)):
        return -1
    elif (CheckDraw()):
        return 0

    if (isMaximizing):
        BestScore = -800
        for key in board.keys():
            if (board[key]== ' '):
                board[key] = Pc
                Score = MiniMax(board,0 ,False)
                board[key] = ' '
                if (Score > BestScore):
                    BestScore = Score
        return BestScore
    
    else:
        BestScore = 800
        for key in board.keys():
            if (board[key]== ' '):
                board[key] = player
                Score = MiniMax(board,0,True)
                board[key] = ' '
                if (Score < BestScore):
                    BestScore = Score
        return BestScore

board = {1: ' ', 2: ' ', 3: ' ', 
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '} # drawting a board

PrintBoard(board)
print("Computer goes first! ")
print("\n")
player = 'O'
Pc = 'X'

global firstComputerMove
firstComputerMove = True

while not CheckWin():
    PcMove()
    PlayerMove()