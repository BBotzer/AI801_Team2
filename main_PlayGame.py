"""
This is the main driver for the Tic Tac Topia AI project.

Author:
    Brandon Botzer-Penn State AI-801, Summer 2022, TEAM 2
    
    

Purpose:
    This code is designed to allow a human player to play against the AI.
    You can play on 3x3, 5x5, 6x6, 7x7, 8x8, 9x9, or 10x10 boards.
    
    
How to use this code:
    Enter the n dimentision of the n x n board you wish to play on.
    
    Enter if the Player is first (yes) or the AI is first (no)
    
    For some reason I still do not understand, the text entry sometimes hangs up
    and freezes.  Stopping the program and then rerunning it will often work to fix the problem.
    However, this may mean that you may not be able to finish a game.  Because of this we've decided not
    to put the human moves into a function call as it seems that the functions hang up on the input()
    more often than just leaving them in the main.
    
    The easier method to run this is to just launch main_PlayGame.py from the file itself and have 
    it play within the terminal.
    
    Not that it matters because you are unable to win BWAHAHAHAHA
    


"""

#import the functions from other file
from displayBoard import *
from winCondition import *
from gameSetup import *
from winConditionsMarks import *
import time

#Modify takeTurns based on what you are testing (abPruning or regular miniMax)
from takeTurns_ab_dls import *




#Series of questions to set up the game
print("Would you like to play Tic-Tac-Topia? (yes/no)")
again = input()


while again == "yes":

    #Query user for the board dimensions
    board = queryBoard()
    
    #Query user for the number needed to win
    #This query is only needed in the general case games which are not implemented
    #ntWin = needWin(board)
    ntWin = len(board)
    
    #Query user for who goes first
    pchoice = queryPlayer()
    
    
    if pchoice == True: 
        player = ' X '
        bot = ' O '
    
        while winCondition(board, ntWin) == False and drawCondition(board) == False:  
            
            #Human Move
            #The human move function hangs up on use inputs --> Unknown as to why
            #humanMove(board, player, ntWin)
            
            #Run the items in the main to prevent hang ups
            #Flag to ensure the player doesn't cheat
            flag1 = False
            flag2 = False
            
            #Player Move
            while flag1 == False or flag2 == False:
                print("\nWhat is the row location to mark?\n")
                x = int(input())
                print("\nWhat is the column location to mark?\n")
                y = int(input())
                
                #Check is move is wihtin the board
                if x < ntWin and y < ntWin and x >=0 and y>=0:
                    flag1 = True
                    
                    if spaceIsFree(board, x, y) == True:
                        makeMove(player, x, y, board, ntWin)
                        flag2 = True
                        showGrid(board)
                    else:
                        print("Stop trying to cheat and pick an open space!\n")
                        showGrid(board)
                else:
                    print("You need to pick something on the board.  Not in space!\n \n")
                    showGrid(board)
            
            #Run winCondition to see if player has won
            if winCondition(board, ntWin) == True:
                print("\nThe player has won.  Don't know how you won but ya did well.\n")
                print("Would you like to play again? (yes / no)\n")
                again = input()
                break
            elif drawCondition(board) == True:
                print("...hmmmm... well that was uneventful... \n")
                print("Would you like to play again? (yes / no)\n")
                again = input()
                break
            
                    
            #The computer goes second
            compMove(board, player, bot, ntWin)
            #Run winCondition to see if compMove has won
            if winCondition(board, ntWin) == True:
                print("\nThe computer has won.  Long live the AI!\n")
                print("Would you like to play again? (yes / no)\n")
                again = input()
                break
            elif drawCondition(board) == True:
                print("...hmmmm... well that was uneventful... \n")
                print("Would you like to play again? (yes / no)\n")
                again = input()
                break
            
    else:
        player = ' X '
        bot = ' O '
    
        while winCondition(board, ntWin) == False and drawCondition(board) == False:  
            
            #Computer holds the first move
            compMove(board, player, bot, ntWin)
            
            #Run winCondition to see if compMove has won
            if winCondition(board, ntWin) == True:
                print("\nThe computer has won.  Long live the AI!\n")
                print("Would you like to play again? (yes / no)\n")
                again = input()
                break
            elif drawCondition(board) == True:
                print("...hmmmm... well that was uneventful... \n")
                print("Would you like to play again? (yes / no)\n")
                again = input()
                break
            
            
            #Human Move
            #The human move function hangs up on use inputs --> Unknown as to why
            #humanMove(board, player, ntWin)
            
            #Run the items in the main to prevent hang ups
            #Flag to ensure the player doesn't cheat
            flag1 = False
            flag2 = False
            
            #Player Move
            while flag1 == False or flag2 == False:
                print("\nWhat is the row location to mark?\n")
                x = int(input())
                print("\nWhat is the column location to mark?\n")
                y = int(input())
                
                #Check is move is wihtin the board
                if x < ntWin and y < ntWin and x >=0 and y>=0:
                    flag1 = True
                    
                    if spaceIsFree(board, x, y) == True:
                        makeMove(player, x, y, board, ntWin)
                        flag2 = True
                        showGrid(board)
                    else:
                        print("Stop trying to cheat and pick an open space!\n")
                        showGrid(board)
                else:
                    print("You need to pick something on the board.  Not in space!\n \n")
                    showGrid(board)

            #Run winCondition to see if player has won
            if winCondition(board, ntWin) == True:
                print("\nThe player has won.  Don't know how you won but ya did well.\n")
                print("Would you like to play again? (yes / no)\n")
                again = input()
                break
            elif drawCondition(board) == True:
                print("...hmmmm... well that was uneventful... \n")
                print("Would you like to play again? (yes / no)\n")
                again = input()
                break





"""
#open the TTT_Data file
file = open("TTT_Data.txt", "a")



#Run loop over all game sizes ( 5x5 through 10x10)
#Running range (5, 11) does sizes 5 -> 10
for q in range (10,11):
    
    
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
        ntWin = len(board)
        pchoice = True
    
        if pchoice == True: 
            player = ' X '
            bot = ' O '
            gameStart = time.perf_counter()
            while winCondition(board, ntWin) == False and drawCondition(board) == False:  
                #playerMove(board, player, bot, ntWin)
                compMove(board, player, bot, ntWin)
                randomMove(board, player, ntWin)
                
            
            gameEnd = time.perf_counter()
            
            totalTime = totalTime + (gameEnd - gameStart)
            playerWin, compWin, tieGame = gameCounter(board, player, bot, playerWin, compWin, tieGame)
        
        print("\nYou are on run: " + str(i) +"/499")
    
    print("\nTotal Calls to miniMax: " + str(int(minimax.totalcalls/numGames)))
    
    avgTime = totalTime / numGames
    print("Average Game Time for a " + str(q) + 'x' + str(q) + " game: " + str(avgTime))  
    out = "For a " + str(q) + "x" + str(q) + " game, " + str(q) + " to win, AI FIRST and Random P1, Forced Moves, abPruning, DLS=2:\n" + "Player Wins: " + str(playerWin) + "\nComputer Wins: " + str(compWin) + "\nTie Games: " + str(tieGame) + "\nAvg. Game Time: " + str(avgTime) + "\nNumber of Calls to miniMax: " + str(int(minimax.totalcalls/numGames))+ "\n\n"
        
    file.write(out)






#Close the File
file.close()
"""       
        



