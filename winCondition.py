# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 14:33:47 2022

@author: Brandon Botzer

Win condition function to check if the win condition is met

Trying to make the grid to check values
"""



        
        
def winRows(board, ntWin=4):
    "Checks for winners in the rows."
    "With a 5x5 grid you need to check 5 rows but only go over 2 columns as the + # searches the rest"
    "The + # could be generalized by some means (board size and # to win needed)"
    "genearlized columns = (blard - needed to win + 1"
    "generalized ros = board size"
    
    brdSize = len(board)
    
    for r in range(brdSize):
        for c in range(brdSize - ntWin +1):
            if board[r][c] == board[r][c+1] and board[r][c] == board[r][c+2] and board[r][c] == board[r][c+3]:
                print("Row Winner in Row: " + str(r))
                return True
            
    return False
                
def winCols(board,  ntWin=4):
    "Checks for winners in the columns"
    "With a 5x5 grid you need to check 5 columns but only two rows as the + # searches the rest"
    "The + # could be generalized by some means (board size and # to win needed)"
    "generalize rows = (board - needed to win + 1"
    "genearalized cols = board size"
    
    
    brdSize = len(board)
    
    for r in range(brdSize):
        
        j = 0
        
        count = 0
        
        #loop through the depth of the board
        #don't worry about checking extra spaces
            #Could minimize checks by looking at 'j' and 'count' and 'ntWin'
        while j < (brdSize - 1):
            
            if board[j][r] == board[j+1][r]:
                count += 1
                
                if count == (ntWin -1):
                    print("Column win in Col: " + str(r))
                    return True
                
            j += 1
                
        
        """
        for c in range(brdSize):
            if board[r][c] == board[r+1][c] and board[r][c] == board[r+2][c] and board[r][c] == board[r+3][c]:
                print("Column win in Col: " + str(c))
                return True
        """   
                
    return False
            
            
def winDiag(board, ntWin=4):
    "Checks for winners along the diagonals"
    "General number of solutions for a square board is:"
    "2 * ((board size + 1 - number needed to win)**2)"
    "the 2 * here is due to the mirror symetry of the board"
    "The diagonals run in both directions, need to think about a"
    "quick solver for that..."
    
    "check center diags and shifts along the center to the edge"
    "check the off diags  using +/- counts"
    
    


    "end of the board"
    brdEnd = len(board) - 1
    brdSize= len(board)
    "need to Win may be passed later for different game varients"
    "prob need to run all of the checks in a loop on the general condition"
    
    
    "check main diags and center shifts first"
    "genearlized times through = (len board - need + 1)"
    
    "look along the forward main diagonal"
    "only need to check if center square is taken"
    for r in range(brdSize - ntWin + 1):
        
        #position incrementer
        j = 0
        
        #number in a row counter
        count = 0
        
        while j < (ntWin - 1):
            
            if board[r+j][r+j] == board[r+j+1][r+j+1]:
                count += 1
                
                if count == (ntWin -1):
                    print("Win along the main forward diagonal: " + str(board[r][r]) + ', ' + str(board[r+3][r+3]))
                    return True
                
            j += 1
                
            
            
            
    "Look along the backward main diagonal"
    for r in range(2):
        if board[brdEnd-r][r] == board[brdEnd-r-1][r+1] and board[brdEnd-r][r] == board[brdEnd-r-2][r+2] and board[brdEnd-r][r] == board[brdEnd-r-3][r+3]:
            print("Win along the main backward diagonal: " + str(board[brdEnd-r][r]) + ', ' + str(board[brdEnd-r-3][r+3]))
            return True



    "Look along the smaller diagonals, forward and backward "
    for r in range(1):
        if board[r][r+1] == board[r+1][r+2] and board[r][r+1] == board[r+2][r+3] and board[r][r+1] == board[r+3][r+4]:
            print("Win along an upper minor forward diagonal")
            return True
        
        if board[r+1][r] == board[r+2][r+1] and board[r+1][r] == board[r+3][r+2] and board[r+1][r] == board[r+4][r+3]:
            print("Win along a lower minor forward diagonal")
            return True
        
        

    

            
def winCondition(board, ntwin = 4):
    """
    Checks the rows, columns, and diagonals for possible winners of a 5x5
    game of TicTacToe with 4 needed to secure vicotry

    Parameters
    ----------
    board : list
        the board grid.
    nSame : int, optional
        The number of same marks it takes to win the game. The default is 4.

    Returns
    -------
    True on a Win
    False on no Wins

    """
        
     #need to try: exception for index out of range
     #or... I can run this as three cycles... On searches for rows, one for columns, one for diags#
     
    if winRows(board, ntwin) == True or winCols(board, ntwin) == True or winDiag(board, ntwin) == True:

        return True
    
        
            
    
    
                
            
        

  

    


