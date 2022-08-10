"""

This is the main driver for the Tic Tac Topia AI project.

Authors:
    Brandon Botzer - Penn State AI-801, Summer 2022, TEAM 2
    
Purpose:
    To run multiple games of TTT for testing results.
    
How to use this code:
    
    Please note, this code was written for tests and as such, a base knowledge
    of how the code should function is needed.  The following information shall
    help you determine what needs to change depending on what test you are running.
    
    In line 42, select which board sizes you'd like to test.
        NOTE: If testing the 3x3 board, enter: range(3,4)
        NOTE: If testing larger board sizes: range(5,7)
                This will test board sizes 5 and 6
                You are able to test boards 5 --> 10
                To do so, enter: range(5,11)
                THERE IS NO TEST FOR A BOARD SIZE OF 4
                
    In line 53, select the number of games you'd like to simulate at each baord size
        NOTE: Large board sizes take considerable amount of time to run tests on
                It is best practice to run large boards by themselves and at a lower
                number of games.
                
    
    Lines 85 - 95 contain the various move sets for the tests:
        Line 8 contains the AI miniMax Player.
        Line 9 contains the AI miniMax Computer.
        Line 9 continas the random Player.
        
        These players can be commented out to determine what the AI computer is up against
        They can also be shuffled in their order to determine the starting player
        
        
    To assign the proper Depth Limit for the searching algormithm, you must go into 'takeTurns_ab_dls.py'
        in the miniMax function, you will see a value for the depth limit.
        this value represents how deep the search tree will go before it ignores win conditions and returns the heuristic
            NOTE: FOR LARGE BOARD SIZES, VALUES ABOVE ONE FOR THE DLS WILL CAUSE EXTREAMLY LONG RUNTIMES
            
    Please ensure that the TTT_Data.txt file has been created in your repository.  This is where the run data will be stored.
    
    In the last few lines, make sure you have updated your output to reflect what tests you are running.
    
    Once ready, you are free to run the code and test.

"""

#import the functions from other file
from displayBoard import *
from winCondition import *
from gameSetup import *
from winConditionsMarks import *
import time


#Modify takeTurns based on what you are testing (abPruning or regular miniMax)
from takeTurns_ab_dls import *


#open the TTT_Data file
file = open("TTT_Data.txt", "a")


#Run loop over all game sizes ( 5x5 through 10x10)
#Running range (5, 11) does sizes 5 -> 10
for q in range (5,11):
    
    
    #Reset record values
    playerWin = 0
    compWin = 0
    tieGame = 0 
    totalTime = 0
    avgTime = 0
    minimax.totalcalls = 0
    
    #Number of games to play for the test of each board
    numGames = 250

    for i in range(numGames):
        
        #Set / Reset the board for multiple game runs
        board = makeGrid(q,q)
        ntWin = q
        #A relic of the playGame scenario to determine first player
        pchoice = True
        
        
        if pchoice == True: 
            player = ' X '
            bot = ' O '
            #Begin timing the game
            gameStart = time.perf_counter()
            while winCondition(board, ntWin) == False and drawCondition(board) == False:
                #THIS IS THE AI PLAYER
                #playerMove(board, player, bot, ntWin)
                
                #THIS IS THE AI COMPUTER
                compMove(board, player, bot, ntWin)
                
                #THIS IS THE RANDOM PLAYER
                randomMove(board, player, ntWin)
                
            #end time on a single game
            gameEnd = time.perf_counter()
            
            #Store times to find an average later
            totalTime = totalTime + (gameEnd - gameStart)
            #Update the counts -> Seems to be an issue with tieGames (unsure where)
            playerWin, compWin, tieGame = gameCounter(board, player, bot, playerWin, compWin, tieGame)
        
        print("\nYou are on run: " + str(i+1) +"/" + str(numGames))
    
    print("\nTotal Calls to miniMax: " + str(int(minimax.totalcalls/numGames)))
    
    avgTime = totalTime / numGames
    
    
    #UPDATE THE OUTPUT FOR THE TESTS YOU ARE RUNNING
    print("Average Game Time for a " + str(q) + 'x' + str(q) + " game: " + str(avgTime))  
    out = "For a " + str(q) + "x" + str(q) + " game, " + str(q) + " to win, AI FIRST and Random P1, Forced Moves, abPruning, DLS=2:\n" + "Player Wins: " + str(playerWin) + "\nComputer Wins: " + str(compWin) + "\nTie Games: " + str(tieGame) + "\nAvg. Game Time: " + str(avgTime) + "\nNumber of Calls to miniMax: " + str(int(minimax.totalcalls/numGames))+ "\n\n"
        
    file.write(out)






#Close the File
file.close()
        
        



