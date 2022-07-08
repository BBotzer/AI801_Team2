"""

This is the main driver for the Tic Tac Topia AI project.

Authors:
    Penn State AI-801, Summer 2022, TEAM 2
    Brandon Botzer
    Ambika Chundru
    Nick Bartkowiak
    

Purpose:
    This is a generalized n by n TicTacToe game played against an AI
    
How to use this code:
    Enter the n dimentision of the n x n board.
    Enter how many 'in a row' it takes to win the game.
    Enter if the Player is first (yes) or the AI is first (no)
    
    For some reason I still do not understand, the text entry sometimes hangs up
    and freezes.  Ctrl-x and then rerunning it will often work to fix the problem.
    This will need to be fixed or just hard coded when we do our trials.


"""

#import the functions from other file
from displayBoard import *
from winCondition import *
from gameSetup import *



#Query user for the board dimensions
board = queryBoard()

#Query user for the number needed to win
ntWin = needWin(board)

#Query user for who goes first
playerFirst = queryPlayer()







#Do we need a function to count the number of turns?


"""

Functions we still need:
    
    
    Check for which grid positions are open (no moves on that location yet)
        Update the makeMove() function run a check for possibleMoves() - Nick?
        
    
    AI Solvers:
        MiniMax - Ambika
        A*
        Breadth
        Depth
        
    OTHERS???
"""


