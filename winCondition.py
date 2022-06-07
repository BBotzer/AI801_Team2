# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 14:33:47 2022

@author: Brandon Botzer

Win condition function to check if the win condition is met

Trying to make the grid to check values
"""



def winCondition(board, nSame = 4):

    "transfered the board to tempbaord because python won't run the board due to types"
    "need to try: exception for index out of range"
    
    i = 0
    j = 0
    for row in board:     
        for entry in row: 
            if entry == " X " or " O " or " x " or " o ":   
                if entry == (board[i][j+1] and board[i][j+2] and board[i][j+3]):
                    print("Return Winner Row - This is incorrectly printing... don't know why")
                    break
                elif entry == (board[i+1][j] and board[i+2][j] and board[i+3][j]):
                    print("return Winner Column")
                    break
                elif entry == (board[i+1][j+1] and board[i+2][j+2] and board[i+3][j+3]):
                    print("return winner Diagonal")
                    break
                else:
                    print("Return No winners")
                    break
                break
            break
        break

                    
                        
    "check to see if a proper value has been filled into a piece of the board"
    "use this location as a starting point (may need to check so that we don't break bounds of the grid"

"""
This works

    tempboard = board
    if tempboard[0][0] == (tempboard[0][1] and tempboard[0][2] and tempboard[0][3]):
        print("winner")
    else:
        return False
"""  
        
       
"""
Still working on this to cycle a grid through the space to run the checks
"""
                    

    


