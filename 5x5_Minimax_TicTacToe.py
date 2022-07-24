board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ',
         6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ',
         11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ',
         16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ',
         21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ',}

def printBoard(board):
    print(board[1]+ '|' + board[2]+ '|'+ board[3]+ '|'+ board[4]+ '|'+ board[5])
    print('-+-+-+-+-')
    print(board[6]+ '|' + board[7]+ '|'+ board[8]+ '|'+ board[9]+ '|'+ board[10])
    print('-+-+-+-+-')
    print(board[11]+ '|' + board[12]+ '|'+ board[13]+ '|'+ board[14]+ '|'+ board[15])
    print('-+-+-+-+-')
    print(board[16]+ '|' + board[17]+ '|'+ board[18]+ '|'+ board[19]+ '|'+ board[20])
    print('-+-+-+-+-')
    print(board[21]+ '|' + board[22]+ '|'+ board[23]+ '|'+ board[24]+ '|'+ board[25])
    print("\n")

printBoard(board)
print("Computer goes first! Good luck.")
print("Positions are as follows:")
print("1, 2, 3, 4, 5")
print("6, 7, 8, 9, 10")
print("11, 12, 13, 14, 15")
print("16, 17, 18, 19, 20")
print("21, 22, 23, 24, 25) \n")
print("player = O")
print("bot = X \n")

def spaceIsFree(position):
    if(board[position]== ' '):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


def checkWin():
    #Top row
    if (board[1] == board[2] and board[1] == board[3] and board[1] == board[4] and board[1] == board[5] and board[1] != ' '):
        return True
    #Second row
    elif (board[6] == board[7] and board[6] == board[8] and board[6] == board[9] and board[6] == board[10] and board[6] != ' '):
        return True
    #Third row
    elif (board[10] == board[11] and board[12] == board[13] and board[12] == board[14] and board[12] == board[15] and board[10] != ' '):
        return True
    #Fourth row
    elif (board[16] == board[17] and board[16] == board[18] and board[16] == board[19] and board[16] == board[20] and board[16] != ' '):
        return True
    #Bottom row
    elif (board[21] == board[22] and board[21] == board[23] and board[21] == board[24] and board[21] == board[25] and board[21] != ' '):
        return True
    #Top left to Bottom right diagonal
    elif (board[1] == board[7] and board[1] == board[13] and board[1] == board[19] and board[1] == board[25] and board[1] != ' '):
        return True
    #Top right to Bottom left diagonal
    elif (board[5] == board[9] and board[5] == board[13] and board[5] == board[17] and board[5] == board[21] and board[5] != ' '):
        return True
    #Left column
    elif (board[1] == board[6] and board[1] == board[11] and board[1] == board[16] and board[1] == board[21] and board[1] != ' '):
        return True
    #Second column
    elif (board[2] == board[7] and board[2] == board[12] and board[2] == board[17] and board[2] == board[22] and board[2] != ' '):
        return True
    #Third column
    elif (board[3] == board[8] and board[3] == board[13] and board[3] == board[18] and board[3] == board[23] and board[3] != ' '):
        return True
    #Fourth column
    elif (board[4] == board[9] and board[4] == board[14] and board[4] == board[19] and board[4] == board[24] and board[4] != ' '):
        return True
    #Right column
    elif (board[5] == board[10] and board[5] == board[15] and board[5] == board[20] and board[5] == board[25] and board[5] != ' '):
        return True
    else:
        return False

def checkWhichMarkWon(mark):
    #Top row
    if (board[1] == board[2] and board[1] == board[3] and board[1] == board[4] and board[1] == board[5] and board[1] == mark):
        return True
    #Second row
    elif (board[6] == board[7] and board[6] == board[8] and board[6] == board[9] and board[6] == board[10] and board[4] == mark):
        return True
    #Third row
    elif (board[10] == board[11] and board[12] == board[13] and board[12] == board[14] and board[12] == board[15] and board[10] == mark):
        return True
    #Fourth row
    elif (board[16] == board[17] and board[16] == board[18] and board[16] == board[19] and board[16] == board[20] and board[16] == mark):
        return True
    #Bottom row
    elif (board[21] == board[22] and board[21] == board[23] and board[21] == board[24] and board[21] == board[25] and board[21] == mark):
        return True
    #Top left to Bottom right diagonal
    elif (board[1] == board[7] and board[1] == board[13] and board[1] == board[19] and board[1] == board[25] and board[1] == mark):
        return True
    #Top right to Bottom left diagonal
    elif (board[5] == board[9] and board[5] == board[13] and board[5] == board[17] and board[5] == board[21] and board[5] == mark):
        return True
    #Left column
    elif (board[1] == board[6] and board[1] == board[11] and board[1] == board[16] and board[1] == board[21] and board[1] == mark):
        return True
    #Second column
    elif (board[2] == board[7] and board[2] == board[12] and board[2] == board[17] and board[2] == board[22] and board[2] == mark):
        return True
    #Third column
    elif (board[3] == board[8] and board[3] == board[13] and board[3] == board[18] and board[3] == board[23] and board[3] == mark):
        return True
    #Fourth column
    elif (board[4] == board[9] and board[4] == board[14] and board[4] == board[19] and board[4] == board[24] and board[4] == mark):
        return True
    #Right column
    elif (board[5] == board[10] and board[5] == board[15] and board[5] == board[20] and board[5] == board[25] and board[5] == mark):
        return True
    else:
        return False

def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)

        if checkWin():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()

        if checkDraw():
            print("Draw!")
            exit()
        return

    else:
        print("Can't insert there!")
        position = int(input("Enter new position: "))
        insertLetter(letter, position)
        return

player = 'O'
bot = 'X'

def playerMove5():
    position = int(input("Enter the position for 'O': "))
    insertLetter(player, position)
    return

def compMove5():
    bestScore = -800
    bestMove = 0

    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return


def minimax(board, depth, isMaximizing, alpha = -800, beta = 800):

    if checkWhichMarkWon(bot):
        return 1

    elif checkWhichMarkWon(player):
        return -1

    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = 800

        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
                alpha = max(bestScore, alpha)
                if alpha >= beta:
                    return bestScore
        return bestScore

    else:
        bestScore = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
                beta = min(bestScore, beta)
                if alpha >= beta:
                    return bestScore
        return bestScore

while not checkWin():
    compMove5()
    playerMove5()