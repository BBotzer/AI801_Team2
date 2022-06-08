# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 14:33:47 2022

@author: Brandon Botzer

Win condition function to check if the win condition is met

Trying to make the grid to check values
"""



def winCondition(board, nSame = 4):

    
    "need to try: exception for index out of range"
    "or... I can run this as three cycles... On searches for rows, one for columns, one for diags"
    
    i = 0
    j = 0
    for i in range(5):     
        for j in range(5): 
            if board[i][j] == " X " or " O " or " x " or " o ":   
                if board[i][j] == board[i][j+1] and board[i][j] == board[i][j+2] and board[i][j] == board[i][j+3]:
                    print("Return Winner Rw ")
                    break
                elif board[i][j] == board[i+1][j] and board[i][j] == board[i+2][j] and board[i][j] == board[i+3][j]:
                    print("return Winner Column")
                    break
                elif board[i][j] == board[i+1][j+1] and board[i][j] == board[i+2][j+2] and board[i][j] == board[i+3][j+3]:
                    print("return winner Diagonal")
                    break
                else:
                    print("Return No winners")
                
            j+=j
            print('Jay' + str(j))
        i+=i
        print('Eye'+str(i))
        
        
def winRows(r,c,board):
    "Checks for winners in the rows."
    "With a 5x5 grid you need to check 5 rows but only go over 2 columns as the + # searches the rest"
    "The + # could be generalized by some means (board size and # to win needed)"
    for r in range(5):
        for c in range(2):
            if board[r][c] == board[r][c+1] and board[r][c] == board[r][c+2] and board[r][c] == board[r][c+3]:
                print("Row Winner in Row" + str(r))
                return True
            else:
                return False
                
def winCols(r,c,board):
    "Checks for winners in the columns"
    "With a 5x5 grid you need to check 5 columns but only two rows as the + # searches the rest"
    "The + # could be generalized by some means (board size and # to win needed)"
    
    for r in range(2):
        for c in range(5):
            if board[r][c] == board[r+1][c] and board[r][c] == board[r+2][c] and board[r][c] == board[r+3][c]:
                print("Column winnin in Col: " + str(c))
                return True
            else:
                return False
            
            
def winDiag(r,c,board):
    "Checks for winners along the diagonals"
    "General number of solutions for a square board is:"
    "2 * ((board size + 1 - number needed to win)**2)"
    "the 2 * here is due to the mirror symetry of the board"
    "The diagonals run in both directions, need to think about a"
    "quick solver for that..."
    
    "check center diags and shifts along the center to the edge"
    "check the off diags  using +/- counts"
    
    
    
                
            
        

                    
                        
    "check to see if a proper value has been filled into a piece of the board"
    "use this location as a starting point (may need to check so that we don't break bounds of the grid"

"""
This works

    tempboard = board
    if tempboard[0][0] == (tempboard[0][1] and tempboard[0][2] and tempboard[0][3]):
        print("winner")
    else:
        return False
"""  
        
       
"""
Still working on this to cycle a grid through the space to run the checks
"""
                    

    


