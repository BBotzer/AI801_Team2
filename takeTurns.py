# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:32:52 2022

@author: btb51
"""


from winConditionsMarks import *
from displayBoard import *
import copy

def makeMove(letter, xloc, yloc, gboard, ntWin):
    #take the move letter, the x and y location, and the current board state
   
    #get x, y location
    x, y = (xloc,yloc)
    


    gboard[x][y] =  letter 
    
    #Check to see if the game ended
    if winConditionMark(gboard, letter, ntWin):
        showGrid(gboard)
        sys.exit(mark+ " has won!")
    if drawCondition(gboard):
        showGrid(gboard)
        sys.exit("This game is a draw!")
    
    #return the updated board to check for wins and the next move
    return gboard


def playerMove(board, player, bot, ntWin):
    player = player
    bot = bot
    bestScore = 1000

    tempboard = copy.deepcopy(board)
    
    xloc = 0
    yloc = 0

    for i in range(len(tempboard)):
        for j in range(len(tempboard)):
            
            if ((tempboard[i][j] != ' X ' and tempboard[i][j] != ' O ') or tempboard[i][j] == ''):
                tempboard[i][j] = player
                score = minimax(tempboard, 0, False, player, bot, ntWin)
                #board[i][j] = ' '  #This might not be needed as it undoes the move.  We are doing this is a funciton (pass by value) so it may should be a different board...???
                if score < bestScore:
                    bestScore = score
                    xloc = i
                    yloc = j

    makeMove(player, xloc, yloc, board, ntWin)
    showGrid(board)
    return 


def compMove(board, player, bot, ntWin):
    player = player
    bot = bot
    bestScore = -1000

    tempboard = copy.deepcopy(board)

    xloc = 0
    yloc = 0

    for i in range(len(tempboard)):
        for j in range(len(tempboard)):
            
            if ((tempboard[i][j] != ' X ' and tempboard[i][j] != ' O ') or tempboard[i][j] == ''):
                tempboard[i][j] = bot
                score = minimax(tempboard, 0, True, player, bot, ntWin)
                #board[i][j] = ' '  #This might not be needed as it undoes the move.  We are doing this is a funciton (pass by value) so it may should be a different board...???
                if score > bestScore:
                    bestScore = score
                    xloc = i
                    yloc = j

    makeMove(bot, xloc, yloc, board, ntWin)
    showGrid(board)
    return 


def minimaxz(board, depth, isMaximizing, player, bot, ntWin):
    return 1


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
                if ((board[i][j] != ' X ' and board[i][j] != ' O ') or board[i][j] == ''): 
                    board[i][j] = bot
                    #There is an issue here when we pass miniMax the board (which is really the temp board).  It keeps cycling on the same location
                    score = minimax(board, depth + 1, False, player, bot, ntWin)
                    #board[i][j] = ' '
                    if (score > bestScore):
                        bestScore = score
        return bestScore

    else:
        bestScore = 1000
        for i in range(len(board)):
            for j in range(len(board)):
                if ((board[i][j] != ' X ' and board[i][j] != ' O ') or board[i][j] == ''):
                    board[i][j] = player
                    #There is an issue here when we pass miniMax the board (which is really the temp board).  It keeps cycling on the same location
                    score = minimax(board, depth + 1, True, player, bot, ntWin)
                    #board[i][j] = ' '
                    if (score < bestScore):
                        bestScore = score
        return bestScore

