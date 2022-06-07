"""
This displays the board for the TicTacTopia base game.

Authors:
    Brandon Botzer

    
Revision 1.0 (06/05/2022) - Botzer - Creation of baseBoard and gridBoard functions
"""

"counting each square on the board 0 - 24"
def baseBoard():

    print()
    print(' ' + '0 ' + ' | ' + '1 ' + ' | ' + '2 ' + ' | ' + '3 ' + ' | ' + '4')
    print('------------------')
    print(' ' + '5 ' + ' | ' + '6 ' + ' | ' + '7 ' + ' | ' + '8 ' + ' | ' + '9')
    print('------------------')
    print(' ' + '10' + ' | ' + '11' + ' | ' + '12' + ' | ' + '13' + ' | ' + '14')
    print('------------------')
    print(' ' + '15' + ' | ' + '16' + ' | ' + '17' + ' | ' + '18' + ' | ' + '19')
    print('------------------')
    print(' ' + '20' + ' | ' + '21' + ' | ' + '22' + ' | ' + '23' + ' | ' + '24')
    print()
   
    
"displaying the current game state from the passed board list 0 - 24"
def showBase(board):

    print()
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ' + board[4])
    print('------------------')
    print(' ' + board[5] + ' | ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('------------------')
    print(' ' + board[10] + ' | ' + board[11] + ' | ' + board[12] + ' | ' + board[13] + ' | ' + board[14])
    print('------------------')
    print(' ' + board[15] + ' | ' + board[16] + ' | ' + board[17] + ' | ' + board[18] + ' | ' + board[19])
    print('------------------')
    print(' ' + board[20] + ' | ' + board[21] + ' | ' + board[22] + ' | ' + board[23] + ' | ' + board[24])   
    print()
    


"counting each square as a grid location (might be easier to check winners)"
def gridBoard():

    print()
    print(' ' + '0,0 ' + ' | ' + '0,1 ' + ' | ' + '0,2 ' + ' | ' + '0,3 ' + ' | ' + '0,4')
    print('----------------------------------')
    print(' ' + '1,0 ' + ' | ' + '1,1 ' + ' | ' + '1,2 ' + ' | ' + '1,3 ' + ' | ' + '1,4')
    print('----------------------------------')
    print(' ' + '2,0 ' + ' | ' + '2,1 ' + ' | ' + '2,2 ' + ' | ' + '2,3 ' + ' | ' + '2,4')
    print('----------------------------------')
    print(' ' + '3,0 ' + ' | ' + '3,1 ' + ' | ' + '3,2 ' + ' | ' + '3,3 ' + ' | ' + '3,4')
    print('----------------------------------')
    print(' ' + '4,0 ' + ' | ' + '4,1 ' + ' | ' + '4,2 ' + ' | ' + '4,3 ' + ' | ' + '4,4')
    print()


def showGrid(gboard):

    print()
    print(' ' + gboard[0][0] + '  |  ' + gboard[0][1] + '  |  ' + gboard[0][2] + '  |  ' + gboard[0][3] + '  |  ' + gboard[0][4])
    print('--------------------------------------')
    print(' ' + gboard[1][0] + '  |  ' + gboard[1][1] + '  |  ' + gboard[1][2] + '  |  ' + gboard[1][3] + '  |  ' + gboard[1][4])
    print('--------------------------------------')
    print(' ' + gboard[2][0] + '  |  ' + gboard[2][1] + '  |  ' + gboard[2][2] + '  |  ' + gboard[2][3] + '  |  ' + gboard[2][4])
    print('--------------------------------------')
    print(' ' + gboard[3][0] + '  |  ' + gboard[3][1] + '  |  ' + gboard[3][2] + '  |  ' + gboard[3][3] + '  |  ' + gboard[3][4])
    print('--------------------------------------')
    print(' ' + gboard[4][0] + '  |  ' + gboard[4][1] + '  |  ' + gboard[4][2] + '  |  ' + gboard[4][3] + '  |  ' + gboard[4][4])
    print()
    

def gameGrid(xgrid=5, ygrid=5):
    
    "builds a default 5x5 grid for tictactoe"
    row, col = (xgrid,ygrid)
    
    "builds grid"
    gboard = [['' for i in range(col)] for j in range(row)]
    
    "Assigns intial values to each space, probably could have done in a loop but I didn't..."
    gboard[0][0] = '0,0'
    gboard[0][1] = '0,1'
    gboard[0][2] = '0,2'
    gboard[0][3] = '0,3'
    gboard[0][4] = '0,4'
    gboard[1][0] = '1,0'
    gboard[1][1] = '1,1'
    gboard[1][2] = '1,2'
    gboard[1][3] = '1,3'
    gboard[1][4] = '1,4'
    gboard[2][0] = '2,0'
    gboard[2][1] = '2,1'
    gboard[2][2] = '2,2'
    gboard[2][3] = '2,3'
    gboard[2][4] = '2,4'
    gboard[3][0] = '3,0'
    gboard[3][1] = '3,1'
    gboard[3][2] = '3,2'
    gboard[3][3] = '3,3'
    gboard[3][4] = '3,4'
    gboard[4][0] = '4,0'
    gboard[4][1] = '4,1'
    gboard[4][2] = '4,2'
    gboard[4][3] = '4,3'
    gboard[4][4] = '4,4'
    
    "returns the built grid"
    "should we also return the board size to pass into the win condition?"
    return gboard
    
        
    
def makeMove(letter, xloc, yloc, gboard):
    "take the move letter, the x and y location, and the current board state"
    
    "get x, y location"
    x, y = (xloc,yloc)
    
    "update the board postion"
    "!!!!!THIS NEEDS A CHECK ON VALID LOCATIONS THAT HAVEN'T BEEN TAKEN"
    gboard[x][y] = ' ' + letter + ' '
    
    "return the updated board to check for wins and the next move"
    return gboard
    




    
    
    
"Junk just to test things"
def testdisplayBoard(board):
    
    showGrid(board)
    
    board = makeMove('O', 2, 3, board)
    board = makeMove('X', 1, 1, board)
    showGrid(board)
    
    

    
    
    