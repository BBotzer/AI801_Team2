"""
This displays the board for the TicTacTopia base game.

Authors:
    Brandon Botzer

    
Revision 1.0 (06/05/2022) - Botzer - Creation of baseBoard and gridBoard function
Revision 2.0 (06/16/2022) - Botzer - Created a generalized board for n x n play
"""

"""
Not using these grid designs
#counting each square on the board 0 - 24
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
   
    
#displaying the current game state from the passed board list 0 - 24
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
    


#counting each square as a grid location (might be easier to check winners)
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
"""

def showGrid(gboard):
    """
    Parameters
    ----------
    gboard : list
        the game board to pass in

    Returns
    -------
    None.
    
    Prints the current game board for n x n tic tac toe
    """
    size = len(gboard)
    linestr = ''
    
    print()
    
    for i in range(size):
        for j in range(size):
            linestr = linestr + gboard[i][j] + ' | '
        print(linestr)
        print("-" * len(linestr))
        linestr = ''
    
    print()
    

def makeGrid(xgrid=5, ygrid=5):
    
    #builds a general sized grid
    #Currently this is a square board!
    row, col = (xgrid,ygrid)
    
    #builds grid
    gboard = [['' for i in range(col)] for j in range(row)]
    
    #Assigns intial values to each space (0 - n)
    
    for i in range(row):
        for j in range (col):
            
            gboard[i][j] = str(i) + ',' + str(j)
            
    
    #returns the built grid
    #should we also return the board size to pass into the win condition?
    return gboard

#Checks if the space was taken or free for a move. Returns True or False   
def spaceIsFree(gboard, x, y):
    if(gboard[x][y]== 'X' or 'Y'):
        return False
    else:
        return True


def aiMove():
    #Minimax to make move
    
    return


#We need a getter method to get these values so we can call it from main.
def playerMove(letter, xloc, yloc, gboard):
    #take the move letter, the x and y location, and the current board state
    
    #get x, y location
    x, y = (xloc,yloc)
    
    #update the board postion
    #!!!!!THIS NEEDS A CHECK ON VALID LOCATIONS THAT HAVEN'T BEEN TAKEN
    gboard[x][y] = ' ' + letter + ' '
    
    #return the updated board to check for wins and the next move
    return gboard
    




    
    

    
    
    