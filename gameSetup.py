# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 15:56:51 2022

@author: Brandon Botzer


This will set up the game by asking the user for the n by n square board
as well as determine who gets to go first, the player or the AI
"""


from displayBoard import *
from fastWinConMark import *
from winConditionsMarks import drawCondition


def queryBoard():
    print("\nWelcome to Tic Tac Topia!\n\nEnter an integer to select the size of the square board to play on.")

    bsize = int(input())
    
    #Two values are passed for row / col
    #Currently set up to make a square board
    board = makeGrid(bsize, bsize)

    showGrid(board)
    
    return board
    

def needWin(board):
    print("\nEnter the integer of how many in a row will we need to win the game.  Make sure your number is smaller than the board size.\n")
    ntWin = int(input())
    print()
    
    while ntWin > len(board):
        print("\nIt seems you need a bigger boat.. I mean board.  \nPlease enter an integer of how many in a row will we need to win the game.  Make sure your number smaller than the board size.")
        ntWin = int(input())
    
    return ntWin



def queryPlayer():
    print("\nWould you like to go first?  (yes / no)\n")

    pchoice = input()
    print()
    
    #Validate user entry
    if pchoice == "yes":
        #The player shall start the game
        return True
    else:
        #The AI shall start the game
        return False
    
    
   
    
    
def gameCounter(board, player, comp, playerWin, compWin, tieGame):
    
    
    if len(board) == 3:
        if fastWinCon3Mark(board, player) == True:
            playerWin += 1
        elif fastWinCon3Mark(board, comp) == True:
            compWin += 1     
        if drawCondition(board) == True:
            tieGame += 1
    
    
    elif len(board) == 5:
        if fastWinCon5Mark(board, player) == True:
            playerWin += 1
        elif fastWinCon5Mark(board, comp) == True:
            compWin += 1     
        if drawCondition(board) == True:
            tieGame += 1
            
    elif len(board) == 6:
        if fastWinCon6Mark(board, player) == True:
            playerWin += 1
        elif fastWinCon6Mark(board, comp) == True:
            compWin += 1     
        if drawCondition(board) == True:
            tieGame += 1
            
    elif len(board) == 7:
        if fastWinCon7Mark(board, player) == True:
            playerWin += 1
        elif fastWinCon7Mark(board, comp) == True:
            compWin += 1     
        if drawCondition(board) == True:
            tieGame += 1
            
    elif len(board) == 8:
        if fastWinCon8Mark(board, player) == True:
            playerWin += 1
        elif fastWinCon8Mark(board, comp) == True:
            compWin += 1     
        if drawCondition(board) == True:
            tieGame += 1
            
    elif len(board) == 9:
        if fastWinCon9Mark(board, player) == True:
            playerWin += 1
        elif fastWinCon9Mark(board, comp) == True:
            compWin += 1     
        if drawCondition(board) == True:
            tieGame += 1
            
    elif len(board) == 10:
        if fastWinCon10Mark(board, player) == True:
            playerWin += 1
        elif fastWinCon10Mark(board, comp) == True:
            compWin += 1     
        if drawCondition(board) == True:
            tieGame += 1


    return playerWin, compWin, tieGame


