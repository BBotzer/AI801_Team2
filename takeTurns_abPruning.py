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


def playerMove(board, player, bot, ntWin):
    player = player
    bot = bot
    bestScore = -1000


    
    xloc = 0
    yloc = 0

    for i in range(len(board)):
        for j in range(len(board)):
            
            if ((board[i][j] != ' X ' and board[i][j] != ' O ') or board[i][j] == ''):
                restoreVal = board[i][j]
                board[i][j] = player
                score = minimax(board, 0, False, player, bot, ntWin)
                board[i][j] = restoreVal  #This might not be needed as it undoes the move.  We are doing this is a funciton (pass by value) so it may should be a different board...???
                if score > bestScore:
                    bestScore = score
                    xloc = i
                    yloc = j

    makeMove(player, xloc, yloc, board, ntWin)
    showGrid(board)
    return 


def compMove(board, player, bot, ntWin):
    player = player
    bot = bot
    bestScore = 1000



    xloc = 0
    yloc = 0

    for i in range(len(board)):
        for j in range(len(board)):
            
            if ((board[i][j] != ' X ' and board[i][j] != ' O ') or board[i][j] == ''):
                restoreVal = board[i][j]
                board[i][j] = bot
                score = minimax(board, 0, True, player, bot, ntWin)
                board[i][j] = restoreVal  #This might not be needed as it undoes the move.  We are doing this is a funciton (pass by value) so it may should be a different board...???
                if score < bestScore:
                    bestScore = score
                    xloc = i
                    yloc = j

    makeMove(bot, xloc, yloc, board, ntWin)
    showGrid(board)
    return 

#Junk test minimax (delete)
def minimaxz(board, depth, isMaximizing, player, bot, ntWin):
    return 1


def minimax(board, depth, isMaximizing, player, bot, ntWin, alpha = 1000, beta = -1000):

    if winConditionMark(board, player, ntWin):
        return 1

    elif winConditionMark(board, bot, ntWin):
        return -1

    elif drawCondition(board):
        return 0

    if isMaximizing:
        bestScore = -1000

        for i in range(len(board)):
            for j in range(len(board)):
                if ((board[i][j] != ' X ' and board[i][j] != ' O ') or board[i][j] == ''):
                    resVal = board[i][j]
                    board[i][j] = player
                    #There is an issue here when we pass miniMax the board (which is really the temp board).  It keeps cycling on the same location
                    score = minimax(board, depth + 1, False, player, bot, ntWin)
                    board[i][j] = resVal
                    if (score > bestScore):
                        bestScore = score
                    alpha = max(bestScore, alpha)
                    if alpha >= beta:
                        return bestScore
                        
                        
                        
        return bestScore

    else:
        bestScore = 1000
        for i in range(len(board)):
            for j in range(len(board)):
                if ((board[i][j] != ' X ' and board[i][j] != ' O ') or board[i][j] == ''):
                    resVal = board[i][j]
                    board[i][j] = bot
                    #There is an issue here when we pass miniMax the board (which is really the temp board).  It keeps cycling on the same location
                    score = minimax(board, depth + 1, True, player, bot, ntWin)
                    board[i][j] = resVal
                    if (score < bestScore):
                        bestScore = score
                    beta = min(bestScore, beta)
                    if alpha >= beta:
                        return bestScore
        return bestScore