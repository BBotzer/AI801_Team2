# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 15:56:51 2022

@author: Brandon Botzer


This will set up the game by asking the user for the n by n square board
as well as determine who gets to go first, the player or the AI
"""


from displayBoard import *


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
    
