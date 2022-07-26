# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 15:16:32 2022

@author: btb51

Uses the base template of winCondition().  

Applies a final check of == mark at the last step to see if the 'Win' is in line
with the mark (X or O) we are looking for.

"""



        
        
def winRowsMark(board, mark, ntWin=4):
    "Checks for winners in the rows."
    "With a 5x5 grid you need to check 5 rows but only go over 2 columns as the + # searches the rest"
    "The + # could be generalized by some means (board size and # to win needed)"
    "genearlized columns = (blard - needed to win + 1"
    "generalized ros = board size"
    
    brdSize = len(board)
    
    for r in range(brdSize):
        
        #r maps the row here [r,j]
        #j maps the position in the row [r,j]
        
        j = 0
        
        count = 0
        
        #loop through the depth of the board
        #don't worry about checking extra spaces
            #Could minimize checks by looking at 'j' and 'count' and 'ntWin'
        while j < (brdSize - 1):
            
            if board[r][j] == board[r][j+1]:
                count += 1
                
                if count == (ntWin -1) and board[r][j] == mark:
                    return True
            else:
                count = 0
            #check condition to prevent excessive iteration through the board
            #Will stop when it is not possible to win a column
            if (brdSize - j) <= (ntWin - count):
                break
            
            #increment possition across the row
            j += 1
      
        
    return False
   

             
def winColsMark(board, mark, ntWin=4):
    "Checks for winners in the columns"
    "With a 5x5 grid you need to check 5 columns but only two rows as the + # searches the rest"
    "The + # could be generalized by some means (board size and # to win needed)"
    "generalize rows = (board - needed to win + 1"
    "genearalized cols = board size"
    
    
    brdSize = len(board)
    
    for c in range(brdSize):
        
        #c maps the column here [j,c]
        #j maps the position in the colum [j,c]
        
        j = 0
        
        count = 0
        
        #loop through the depth of the board
        #don't worry about checking extra spaces
            #Could minimize checks by looking at 'j' and 'count' and 'ntWin'
        while j < (brdSize - 1):
            
            if board[j][c] == board[j+1][c]:
                count += 1
                
                if count == (ntWin -1) and board[j][c] == mark:
                    return True
            else:
                count = 0
            #check condition to prevent excessive iteration through the board
            #Will stop when it is not possible to win a column
            if (brdSize - j) <= (ntWin - count):
                break
            
            #increment possition down the column
            j += 1
             
                
    return False
            
            
            
def winDiagMark(board, mark, ntWin=4):
    "Checks for winners along the diagonals"
    "General number of solutions for a square board is:"
    "2 * ((board size + 1 - number needed to win)**2)"
    "the 2 * here is due to the mirror symetry of the board"

    

    #end of the board in index
    brdEnd = len(board) - 1
    #Size of the board
    brdSize= len(board)
    "need to Win may be passed later for different game varients"
    "prob need to run all of the checks in a loop on the general condition"
    
    
    "check main diags and center shifts first"
    "genearlized times through = (len board - need + 1)"
    
    "look along the forward main diagonal"
    "only need to check if center square is taken as a quick check for some cases (not implemented)"
    
    #Number of possible wins you have along a main diagonal
    for r in range(brdSize - ntWin + 1):
        
        #position incrementer for the top left diagonal edge
        j = 0
        
        #number in a row counter (how close to win)
        count = 0
        
        #need to increment j to move along
        while j < (ntWin - 1):
            
            if board[r+j][r+j] == board[r+j+1][r+j+1]:
                #need to count the number in a row in case we win and need to return out
                count += 1
                
                if count == (ntWin -1) and board[r+j][r+j] == mark:
                    return True
            else:
                count = 0
                
            j += 1
                     
            
    "Look along the backward main diagonal"
    #Number of possible wins you have along a main diagonal
    for r in range(brdSize - ntWin + 1):
        
        #position incrementer for the bottom left diagonal edge
        j = 0
        
        #number in a row counter (how close to a win)
        count = 0
        
        #need to increment j to move along
        while j < (ntWin - 1):
            
            #Check back one row, and over one column
            if board[brdEnd-r-j][r+j] == board[brdEnd-r-j-1][r+j+1]:
                #need to count the number in a row in case we win and need to return out
                count += 1
                
                if count == (ntWin -1) and board[brdEnd-r-j][r+j] == mark:
                    return True
            else:
                count = 0
                
            j += 1



    #All Minor diagonal (mD) must be looked at.  This can be done with another for loop
    #to move along all of the upper and lower, forward and backward diagonals (4 loops needed)


    "Look along all minor upper forward diagonals"
    
    #The diags follow a pattern of number of possible wins from the main of
    #size - ntWin + 1 - (the amount off from the main diag)
    
    #amount off from the main diagonal
    #mD = minor Diagonals count goes from 1 -> minor diagonals needed
    
    for mD in range(1, (brdSize-ntWin+1)):
    
        #Number of possible wins you have along a  diagonal adjusted for the minor diagonal
        for r in range(brdSize - ntWin + 1 -mD):
            
            #position incrementer for the top left diagonal edge
            j = 0
            
            #number in a row counter (how close to win)
            count = 0
            
            #need to increment j to move along
            while j < (ntWin - 1):
                
                if board[r+j][r+j+mD] == board[r+j+1][r+j+mD+1]:
                    #need to count the number in a row in case we win and need to return out
                    count += 1
                    
                    if count == (ntWin -1) and board[r+j][r+j+mD] == mark:
                        #print("Win along the minor upper forward diagonal: " + str(board[r][r]) + ', ' + str(board[r+3][r+3]))
                        return True
                else:
                    count = 0
                    
                j += 1
    
    
    
    "Look along all minor lower forward diagonals"
    #The diags follow a pattern of number of possible wins from the main of
    #size - ntWin + 1 - (the amount off from the main diag)
    
    #amount off from the main diagonal
    #mD = minor Diagonals count goes from 1 -> minor diagonals needed
    
    for mD in range(1, (brdSize-ntWin+1)):
    
        #Number of possible wins you have along a  diagonal adjusted for the minor diagonal
        for r in range(brdSize - ntWin + 1 -mD):
            
            #position incrementer for the top left diagonal edge
            j = 0
            
            #number in a row counter (how close to win)
            count = 0
            
            #need to increment j to move along
            while j < (ntWin - 1):
                
                if board[r+j+mD][r+j] == board[r+j+mD+1][r+j+1]:
                    #need to count the number in a row in case we win and need to return out
                    count += 1
                    
                    if count == (ntWin -1) and board[r+j+mD][r+j] == mark:
                        #print("Win along the minor upper forward diagonal: " + str(board[r][r]) + ', ' + str(board[r+3][r+3]))
                        return True
                else:
                    count = 0
                    
                j += 1
    
    
    
    
    
    
    
    "Look along all minor upper backward diagonals"
    #The diags follow a pattern of number of possible wins from the main of
    #size - ntWin + 1 - (the amount off from the main diag)
    
    #amount off from the main diagonal
    #mD = minor Diagonals count goes from 1 -> minor diagonals needed
    
    for mD in range(1, (brdSize-ntWin+1)):
    
        #Number of possible wins you have along a  diagonal adjusted for the minor diagonal
        for r in range(brdSize - ntWin + 1 -mD):
            
            #position incrementer for the top left diagonal edge
            j = 0
            
            #number in a row counter (how close to win)
            count = 0
            
            #need to increment j to move along
            while j < (ntWin - 1):
                
                if board[brdEnd-r-j-mD][r+j] == board[brdEnd-r-j-mD-1][r+j+1]:
                    #need to count the number in a row in case we win and need to return out
                    count += 1
                    
                    if count == (ntWin -1) and board[brdEnd-r-j-mD][r+j] == mark:
                        #print("Win along the minor upper forward diagonal: " + str(board[r][r]) + ', ' + str(board[r+3][r+3]))
                        return True
                else:
                    count = 0
                    
                j += 1




    "Look along all minor lower backward diagonals"
    #The diags follow a pattern of number of possible wins from the main of
    #size - ntWin + 1 - (the amount off from the main diag)
    
    #amount off from the main diagonal
    #mD = minor Diagonals count goes from 1 -> minor diagonals needed
    
    for mD in range(1, (brdSize-ntWin+1)):
    
        #Number of possible wins you have along a  diagonal adjusted for the minor diagonal
        for r in range(brdSize - ntWin + 1 -mD):
            
            #position incrementer for the top left diagonal edge
            j = 0
            
            #number in a row counter (how close to win)
            count = 0
            
            #need to increment j to move along
            while j < (ntWin - 1):
                
                if board[brdEnd-r-j][r+j+mD] == board[brdEnd-r-j-1][r+j+mD+1]:
                    #need to count the number in a row in case we win and need to return out
                    count += 1
                    
                    if count == (ntWin -1) and board[brdEnd-r-j][r+j+mD] == mark:
                        #print("Win along the minor upper forward diagonal: " + str(board[r][r]) + ', ' + str(board[r+3][r+3]))
                        return True
                else:
                    count = 0
                    
                j += 1



    #No Diagonal winners
    return False

            
def winConditionMark(board, mark, ntwin = 4):
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
        
     
    if winRowsMark(board, mark, ntwin) == True or winColsMark(board, mark, ntwin) == True or winDiagMark(board, mark, ntwin) == True:
        return True
    else:
        return False
    

def drawCondition(board):
    
    for i in range(len(board)):
        for j in range(len(board)):
            
            #Go through the board until you find a space you can move
            if board[i][j] != ' X ' and board[i][j] != ' O ':
                return False
            
    #No more spaces to move
    print("We have a draw.")
    return True
 
            
    
    
 