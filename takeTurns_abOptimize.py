# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 19:07:32 2022

@author: btb51
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 19:56:55 2022

@author: btb51
"""

"""
Created on Mon Jul 18 14:32:52 2022
@author: btb51
"""


#THis is this alpha-beta pruning test

from winConditionsMarks import *
from displayBoard import *
import copy
import site

def makeMove(letter, xloc, yloc, gboard, ntWin):
    #take the move letter, the x and y location, and the current board state
   
    #get x, y location
    x, y = (xloc,yloc)
    
    if spaceIsFree(gboard,x,y) == False:
        #print("That space is taken.  Try again.\n")
        return
    else:
        
    
        #Check to see if game ended
        if letter == ' X ':
            check = ' O '
        else:
            check = ' X '
        
        #Check to see if the game ended
        if winConditionMark(gboard, check, ntWin):
            showGrid(gboard)
            return False
        if drawCondition(gboard):
            showGrid(gboard)
            return False
    
    
        #used to update the board
        gboard[x][y] =  letter 
    
        
        #return used to create the board
        return gboard


def playerForcedMoves(board, player, bot, ntWin):
    #Check to see if there is an easy win in the next move
    #Cycle through the spaces
    for i, j in ((ti, tj) for ti in range(len(board)) for tj in range(len(board))):
        
        #Check if space is free
        
        if spaceIsFree(board, i, j):
        
            #keep the restore value
            restoreVal = board[i][j]
            #make a possible winning move
            board[i][j] = player
            #check to see if the move has won
            if winConditionMark(board, player, ntWin):
                #You won
                showGrid(board)
                print("Calls to miniMax: " + str(minimax.counter))
                return True
            #You didn't win, restore the old value
            else:
                board[i][j] = restoreVal
            

    #Check to see if there is a block that you must make to keep the opponent from winning
    #Cycle through the spaces
    for i, j in ((ti, tj) for ti in range(len(board)) for tj in range(len(board))):
        
        #Check if space is free
        
        if spaceIsFree(board, i, j):
            
            #keep the restore value
            restoreVal = board[i][j]
            #Move the computer into that spot (a turn ahead)
            board[i][j] = bot
            #Check to see if that caused the computer to win
            if winConditionMark(board, bot, ntWin):
                #The computer will win if it goes there, take the spot from them
                board[i][j] = player
                showGrid(board)
                print("Calls to miniMax: " + str(minimax.counter))
                return True
            #The computer won't win there, you can leave it for now
            else:
                board[i][j] = restoreVal


def compForcedMoves(board, player, bot, ntWin):
    #Check to see if there is an easy win in the next move
    #Cycle through the spaces
   for i, j in ((ti, tj) for ti in range(len(board)) for tj in range(len(board))):
        
       #Check if space is free
       
       if spaceIsFree(board, i, j):
       
            #keep the restore value
            restoreVal = board[i][j]
            #make a possible winning move
            board[i][j] = bot
            #check to see if the move has won
            if winConditionMark(board, bot, ntWin):
                #You won
                showGrid(board)
                print("Calls to miniMax: " + str(minimax.counter))
                return True
            #You didn't win, restore the old value
            else:
                board[i][j] = restoreVal
            

    #Check to see if there is a block that you must make to keep the opponent from winning
    #Cycle through the spaces
   for i, j in ((ti, tj) for ti in range(len(board)) for tj in range(len(board))):
        
       #Check if space is free
       
       if spaceIsFree(board, i, j):
       
            #keep the restore value
            restoreVal = board[i][j]
            #Move the computer into that spot (a turn ahead)
            board[i][j] = player
            #Check to see if that caused the computer to win
            if winConditionMark(board, player, ntWin):
                #The computer will win if it goes there, take the spot from them
                board[i][j] = bot
                showGrid(board)
                print("Calls to miniMax: " + str(minimax.counter))
                return True
            #The computer won't win there, you can leave it for now
            else:
                board[i][j] = restoreVal




def playerMove(board, player, bot, ntWin):
    player = player
    bot = bot
    bestMax = -1000
    minimax.counter = 0

    
    xloc = 0
    yloc = 0
    
    #Look for forced moves.  If one is made, return without running miniMax
    if playerForcedMoves(board, player, bot, ntWin) == True:
        return
              
        
    #No move will win for us or for the opponent (next turn).  Choose optimal play via miniMax_abpruning
    for i in range(len(board)):
        for j in range(len(board)):
            
            if ((board[i][j] != ' X ' and board[i][j] != ' O ') or board[i][j] == ''):
                restoreVal = board[i][j]
                board[i][j] = player
                score = minimax(board, 0, False, player, bot, ntWin, alpha = -1000, beta = 1000)
                board[i][j] = restoreVal  #This might not be needed as it undoes the move.  We are doing this is a funciton (pass by value) so it may should be a different board...???
                if score > bestMax:
                    bestMax = score
                    xloc = i
                    yloc = j

    makeMove(player, xloc, yloc, board, ntWin)
    showGrid(board)
    print("Calls to miniMax: " + str(minimax.counter))
    return 


def compMove(board, player, bot, ntWin):
    player = player
    bot = bot
    bestMin = 1000
    minimax.counter = 0


    xloc = 0
    yloc = 0

     #Look for forced moves.  If one is made, return without running miniMax
    if compForcedMoves(board, player, bot, ntWin) == True:
        return
               
         
     #No move will win for us or for the opponent (next turn).  Choose optimal play via miniMax_abpruning

    for i in range(len(board)):
        for j in range(len(board)):
            
            if ((board[i][j] != ' X ' and board[i][j] != ' O ') or board[i][j] == ''):
                restoreVal = board[i][j]
                board[i][j] = bot
                score = minimax(board, 0, True, player, bot, ntWin, alpha = -1000, beta = 1000)
                board[i][j] = restoreVal  #This might not be needed as it undoes the move.  We are doing this is a funciton (pass by value) so it may should be a different board...???
                if score < bestMin:
                    bestMin = score
                    xloc = i
                    yloc = j

    makeMove(bot, xloc, yloc, board, ntWin)
    showGrid(board)
    print("Calls to miniMax: " + str(minimax.counter))
    return 



def minimax(board, depth, isMaximizing, player, bot, ntWin, alpha, beta):
    
    #Create a counter for how many times miniMax is called
    minimax.counter += 1
    
    
    #Set the various win conditions based on the depth.  ie. find the fastest solution
    if winConditionMark(board, player, ntWin):
        return ((len(board)**2) - depth)

    elif winConditionMark(board, bot, ntWin):
        return (depth - (len(board)**2))

    elif drawCondition(board):
        return 0

    if isMaximizing:
        bestMax = -1000


        #Check for the forced moves for the player
       # if playerForcedMoves(board, player, bot, ntWin) == True:
       #     return 

        #Cool use of generator expression to generate double loop as single loop for break statement
        for i, j in ((ti, tj) for ti in range(len(board)) for tj in range(len(board))):
            if ((board[i][j] != ' X ' and board[i][j] != ' O ') or board[i][j] == ''):
                resVal = board[i][j]
                board[i][j] = player
                #There is an issue here when we pass miniMax the board (which is really the temp board).  It keeps cycling on the same location
                score = minimax(board, depth + 1, False, player, bot, ntWin, alpha, beta)
                board[i][j] = resVal
                if (score > bestMax):
                    bestMax = score
                alpha = max(bestMax, alpha)
            if alpha >= beta:
                break
            
        return bestMax

    else:
        bestMin = 1000
        
        #Check for the forced moves for the bot
        #if compForcedMoves(board, player, bot, ntWin) == True:
        #    return 
        
        for i, j in ((ti, tj) for ti in range(len(board)) for tj in range(len(board))):
            if ((board[i][j] != ' X ' and board[i][j] != ' O ') or board[i][j] == ''):
                resVal = board[i][j]
                board[i][j] = bot
                #There is an issue here when we pass miniMax the board (which is really the temp board).  It keeps cycling on the same location
                score = minimax(board, depth + 1, True, player, bot, ntWin, alpha, beta)
                board[i][j] = resVal
                if (score < bestMin):
                    bestMin = score
                beta = min(bestMin, beta)
            if alpha >= beta:
                break
            
        return bestMin
    
