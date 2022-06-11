"""

This is the main driver for the Tic Tac Topia AI project.

Authors:
    Penn State AI-801, Summer 2022, TEAM 2
    Brandon Botzer
    Ambika Chundru
    Nick Bartkowiak
    

Purpose:
    TEXT
    
How to use this code:
    TEXT


"""

"import the functions from displayBoard file"
from displayBoard import *


board = gameGrid(5,5)


"test the displayBoard code"
testdisplayBoard(board)


"Do we need a function to count the number of turns?"


"""
Functions we still need:
    
    Check for win condition (probably easier with the grid)
    
    Check for which grid positions are open (no moves on that location yet)
<<<<<<< Updated upstream
=======
        Update the makeMove() function run a check for possibleMoves()
        if possibleMoves are none and the board is full, a tie must be called
        
    makeGrid() needs to be built so that it will automatically create the n by n
        grid without having to hard code the strings "0,0" etc.
>>>>>>> Stashed changes
    
    AI Solvers:
        MiniMax
        A*
        Breadth
        Depth
        
    OTHERS???
"""



