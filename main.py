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

#Modify takeTurns based on what you are testing (abPruning or regular miniMax)
from takeTurns_ab_dls import *

from winConditionsMarks import *
import time




#Query user for the board dimensions
#board = queryBoard()

#Query user for the number needed to win
#ntWin = needWin(board)

#Query user for who goes first
#playerFirst = queryPlayer()

#I made up the winConditions method, but it would be easier to run this loop
#if we combine all the win condition methods into one so only one method needs to be false here.


#force the game to run a 3x3 to test miniMax..


playerWin = 0
compWin = 0
tieGame = 0 
#testing single loop

        
#for i, j in ((ti, tj) for ti in range(len(board)) for tj in range(len(board))):
#    print(str(i) +", " +  str(j))
#    if j == 2:
#        break
    
#print("I am freeee")


#open the TTT_Data file
file = open("TTT_Data.txt", "a")



#Run loop over all game sizes ( 5x5 through 10x10)
for q in range (5,6):
    
    playerWin = 0
    compWin = 0
    tieGame = 0 
    totalTime = 0
    avgTime = 0

    for i in range(10):
        
        #Set / Reset the board for multiple game runs
        board = makeGrid(q,q)
        ntWin = q
        pchoice = True
    
        if pchoice == True: 
            player = ' X '
            bot = ' O '
            gameStart = time.perf_counter()
            while winCondition(board, ntWin) == False and drawCondition(board) == False:  #Fix exit game
                playerMove(board, player, bot, ntWin)
                compMove(board, player, bot, ntWin)
            
            gameEnd = time.perf_counter()
            
            totalTime = totalTime + (gameEnd - gameStart)
            playerWin, compWin, tieGame = gameCounter(board, player, bot, playerWin, compWin, tieGame)
        
        
    avgTime = totalTime / 10
    
    print("Average Game Time for a " + str(q) + 'x' + str(q) + " game: " + str(avgTime))  
    out = "For a " + str(q) + "x" + str(q) + " game, " + str(q) + " to win, Forced Moves, abPruning, DLS=1:\n" + "Player Wins: " + str(playerWin) + "\nComputer Wins: " + str(compWin) + "\nTie Games: " + str(tieGame) + "\nAvg. Game Time: " + str(avgTime) + "\n\n"
        
    file.write(out)






#Close the File
file.close()
        
        
"""
else:
    player = ' O '
    bot = ' X '
    while winCondition(board, ntWin) == False:
       compMove(board, player, bot, ntWin)
       playerMove(board, player, bot, ntWin) 
"""

"""
if playerFirst:
    player = ' X '
    bot = ' O '
    while not winCondition(board, ntWin):
        playerMove(board, player, bot, ntWin)
        compMove(board, player, bot, ntWin)
else:
    player = ' O '
    bot = ' X '
    while not winCondition(board, ntWin):
        compMove(board, player, bot, ntWin)
        playerMove(board, player, bot, ntWin)

"""


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


