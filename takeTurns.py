# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:32:52 2022

@author: btb51
"""


from winConditionsMarks import *
from displayBoard import *

def makeMove(letter, xloc, yloc, gboard):
    #take the move letter, the x and y location, and the current board state
    
    #get x, y location
    x, y = (xloc,yloc)
    
    #update the board postion
    #!!!!!THIS NEEDS A CHECK ON VALID LOCATIONS THAT HAVEN'T BEEN TAKEN
    gboard[x][y] = ' ' + letter + ' '
    
    #return the updated board to check for wins and the next move
    return gboard


def playerMove(board, player, bot, ntWin):
    player = player
    bot = bot
    bestScore = 1000

    xloc = 0
    yloc = 0

    for i in range(len(board)):
        for j in range(len(board)):
            
            if board[i][j] != 'X' and board[i][j] != 'O':
                board[i][j] = player
                score = minimax(board, 0, True, player, bot, ntWin)
                board[i][j] = ' '  #This might not be needed as it undoes the move.  We are doing this is a funciton (pass by value) so it may should be a different board...???
                if score > bestScore:
                    bestScore = score
                    xloc = i
                    yloc = j

    makeMove(bot, xloc, yloc, board)
    showGrid(board)
    return


def compMove(board, player, bot, ntWin):
    player = player
    bot = bot
    bestScore = -1000

    xloc = 0
    yloc = 0

    for i in range(len(board)):
        for j in range(len(board)):
            
            if board[i][j] != 'X' and board[i][j] != 'O':
                board[i][j] = bot
                score = minimax(board, 0, False, player, bot, ntWin)
                board[i][j] = ' '  #This might not be needed as it undoes the move.  We are doing this is a funciton (pass by value) so it may should be a different board...???
                if score > bestScore:
                    bestScore = score
                    xloc = i
                    yloc = j

    makeMove(bot, xloc, yloc, board)
    showGrid(board)
    return



def minimax(board, depth, isMaximizing, player, bot, ntWin):

    if winConditionMark(board, bot, ntWin):
        return 1

    elif winConditionMark(board, player, ntWin):
        return -1

    elif drawCondition(board):
        return 0

    if isMaximizing:
        bestScore = -1000

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 'X' and board[i][j] != 'O': 
                    board[i][j] = bot
                    score = minimax(board, depth + 1, False, player, bot, ntWin)
                    board[i][j] = ' '
                    if (score > bestScore):
                        bestScore = score
        return bestScore

    else:
        bestScore = 1000
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    board[i][j] = player
                    score = minimax(board, depth + 1, True, player, bot, ntWin)
                    board[i][j] = ' '
                    if (score < bestScore):
                        bestScore = score
        return bestScore

