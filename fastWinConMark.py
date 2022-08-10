# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 06:53:44 2022

@author: btb51
"""

#3x3 Board Conditions

def fastWinCon3Mark(board, mark):
    if (board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] == mark):
        return True
    elif (board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] == mark):
        return True
    elif (board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] == mark):
        return True
    elif (board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] == mark):
        return True
    elif (board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] == mark):
        return True
    elif (board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] == mark):
        return True
    elif (board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == mark):
        return True
    elif (board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[2][0] == mark):
        return True
    else:
        return False
    
def heuristic3(board):
    
    
    #mark is the first player looking to maximize the score
    mark = ' X '
    #Opp is the second player looking to minimize the score
    opp= ' O '
    
    xlines = 0
    olines = 0
    
    #X Player
    if (board[0][0] != opp and board[0][1] != opp and board[0][2] != opp):
        xlines +=1
    if (board[1][0] != opp and board[1][1] != opp and board[1][2] != opp):
        xlines +=1
    if (board[2][0] != opp and board[2][1] != opp and board[2][2] != opp):
        xlines +=1
    if (board[0][0] != opp and board[1][0] != opp and board[2][0] != opp):
       xlines +=1
    if (board[0][1] != opp and board[1][1] != opp and board[2][1] != opp):
        xlines +=1
    if (board[0][2] != opp and board[1][2] != opp and board[2][2] != opp):
        xlines +=1
    if (board[0][0] != opp and board[1][1] != opp and board[2][2] != opp):
        xlines +=1
    if (board[2][0] != opp and board[1][1] != opp and board[0][2] != opp):
        xlines +=1
        
        
        
    #O player
    if (board[0][0] != mark and board[0][1] != mark and board[0][2] != mark):
        olines +=1
    if (board[1][0] != mark and board[1][1] != mark and board[1][2] != mark):
        olines +=1
    if (board[2][0] != mark and board[2][1] != mark and board[2][2] != mark):
        olines +=1
    if (board[0][0] != mark and board[1][0] != mark and board[2][0] != mark):
       olines +=1
    if (board[0][1] != mark and board[1][1] != mark and board[2][1] != mark):
        olines +=1
    if (board[0][2] != mark and board[1][2] != mark and board[2][2] != mark):
        olines +=1
    if (board[0][0] != mark and board[1][1] != mark and board[2][2] != mark):
        olines +=1
    if (board[2][0] != mark and board[1][1] != mark and board[0][2] != mark):
        olines +=1
    
    heuristic = xlines - olines
    
    return heuristic
    
    
#5x5 Board conditions 


def fastWinCon5Mark(board, mark):
    if (board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] == board[0][3] and board[0][0] == board[0][4] and board[0][0] == mark):
        return True
    elif (board[1][0] == board[2][1] and board[1][0] == board[1][2] and board[1][0] == board[1][3] and board[1][0] == board[1][4] and board[1][0] == mark):
        return True
    elif (board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] == board[2][3] and board[2][0] == board[2][4] and board[2][0] == mark):
        return True
    elif (board[3][0] == board[3][1] and board[3][0] == board[3][2] and board[3][0] == board[3][3] and board[3][0] == board[3][4] and board[3][0] == mark):
        return True
    elif (board[4][0] == board[4][1] and board[4][0] == board[4][2] and board[4][0] == board[4][3] and board[4][0] == board[4][4] and board[4][0] == mark):
        return True
    elif (board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] == board[3][0] and board[0][0] == board[4][0] and board[0][0] == mark):
        return True
    elif (board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] == board[3][1] and board[0][1] == board[4][1] and board[0][1] == mark):
        return True
    elif (board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] == board[3][2] and board[0][2] == board[4][2] and board[0][2] == mark):
        return True
    elif (board[0][3] == board[1][3] and board[0][3] == board[2][3] and board[0][3] == board[3][3] and board[0][3] == board[4][3] and board[0][3] == mark):
        return True
    elif (board[0][4] == board[1][4] and board[0][4] == board[2][4] and board[0][4] == board[3][4] and board[0][4] == board[4][4] and board[0][4] == mark):
        return True
    elif (board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == board[3][3] and board[0][0] == board[4][4] and board[0][0] == mark):
        return True
    elif (board[4][0] == board[3][1] and board[4][0] == board[2][2] and board[4][0] == board[1][3] and board[4][4] == board[0][4] and board[4][0] == mark):
        return True
    else:
        return False
    
    
    
def heuristic5(board):
    
    
    #mark is the first player looking to maximize the score
    mark = ' X '
    #Opp is the second player looking to minimize the score
    opp= ' O '
    
    xlines = 0
    olines = 0
    
    #check how many open lines exist for the X player
    if (board[0][0] != opp and board[0][1] != opp and board[0][2] != opp and board[0][3] != opp and board[0][4] != opp):
        xlines +=1
    if (board[1][0] != opp and board[1][1] != opp and board[1][2] != opp and board[1][3] != opp and board[1][4] != opp):
        xlines +=1
    if (board[2][0] != opp and board[2][1] != opp and board[2][2] != opp and board[2][3] != opp and board[2][4] != opp):
        xlines +=1
    if (board[3][0] != opp and board[3][1] != opp and board[3][2] != opp and board[3][3] != opp and board[3][4] != opp):
        xlines +=1
    if (board[4][0] != opp and board[4][1] != opp and board[4][2] != opp and board[4][3] != opp and board[4][4] != opp):
        xlines +=1
    if (board[0][0] != opp and board[1][0] != opp and board[2][0] != opp and board[3][0] != opp and board[4][0] != opp):
       xlines +=1
    if (board[0][1] != opp and board[1][1] != opp and board[2][1] != opp and board[3][1] != opp and board[4][1] != opp):
        xlines +=1
    if (board[0][2] != opp and board[1][2] != opp and board[2][2] != opp and board[3][2] != opp and board[4][2] != opp):
        xlines +=1
    if (board[0][3] != opp and board[1][3] != opp and board[2][3] != opp and board[3][3] != opp and board[4][3] != opp):
        xlines +=1
    if (board[0][4] != opp and board[1][4] != opp and board[2][4] != opp and board[3][4] != opp and board[4][4] != opp):
        xlines +=1
    if (board[0][0] != opp and board[1][1] != opp and board[2][2] != opp and board[3][3] != opp and board[4][4] != opp):
        xlines +=1
    if (board[4][0] != opp and board[3][1] != opp and board[2][2] != opp and board[1][3] != opp and board[0][4] != opp):
        xlines +=1
    
    
    
    
    #Check how many open lines exist for the O player
    if (board[0][0] != mark and board[0][1] != mark and board[0][2] != mark and board[0][3] != mark and board[0][4] != mark):
        olines +=1
    if (board[1][0] != mark and board[1][1] != mark and board[1][2] != mark and board[1][3] != mark and board[1][4] != mark):
        olines +=1
    if (board[2][0] != mark and board[2][1] != mark and board[2][2] != mark and board[2][3] != mark and board[2][4] != mark):
        olines +=1
    if (board[3][0] != mark and board[3][1] != mark and board[3][2] != mark and board[3][3] != mark and board[3][4] != mark):
        olines +=1
    if (board[4][0] != mark and board[4][1] != mark and board[4][2] != mark and board[4][3] != mark and board[4][4] != mark):
        olines +=1
    if (board[0][0] != mark and board[1][0] != mark and board[2][0] != mark and board[3][0] != mark and board[4][0] != mark):
       olines +=1
    if (board[0][1] != mark and board[1][1] != mark and board[2][1] != mark and board[3][1] != mark and board[4][1] != mark):
        olines +=1
    if (board[0][2] != mark and board[1][2] != mark and board[2][2] != mark and board[3][2] != mark and board[4][2] != mark):
        olines +=1
    if (board[0][3] != mark and board[1][3] != mark and board[2][3] != mark and board[3][3] != mark and board[4][3] != mark):
        olines +=1
    if (board[0][4] != mark and board[1][4] != mark and board[2][4] != mark and board[3][4] != mark and board[4][4] != mark):
        olines +=1
    if (board[0][0] != mark and board[1][1] != mark and board[2][2] != mark and board[3][3] != mark and board[4][4] != mark):
        olines +=1
    if (board[4][0] != mark and board[3][1] != mark and board[2][2] != mark and board[1][3] != mark and board[0][4] != mark):
        olines += 1
    
    
           
    heuristic = xlines - olines
    
    return heuristic
    
    
    
    
    
#6x6 Board Conditions

def fastWinCon6Mark(board, mark):
    if (board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] == board[0][3] and board[0][0] == board[0][4] and board[0][0] == board[0][5] and board[0][0] == mark):
        return True
    elif (board[1][0] == board[2][1] and board[1][0] == board[1][2] and board[1][0] == board[1][3] and board[1][0] == board[1][4] and board[1][0] == board[1][5] and board[1][0] == mark):
        return True
    elif (board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] == board[2][3] and board[2][0] == board[2][4] and board[2][0] == board[2][5] and board[2][0] == mark):
        return True
    elif (board[3][0] == board[3][1] and board[3][0] == board[3][2] and board[3][0] == board[3][3] and board[3][0] == board[3][4] and board[3][0] == board[3][5] and board[3][0] == mark):
        return True
    elif (board[4][0] == board[4][1] and board[4][0] == board[4][2] and board[4][0] == board[4][3] and board[4][0] == board[4][4] and board[4][0] == board[4][5] and board[4][0] == mark):
        return True
    elif (board[5][0] == board[5][1] and board[5][0] == board[5][2] and board[5][0] == board[5][3] and board[5][0] == board[5][4] and board[5][0] == board[5][5] and board[5][0] == mark):
        return True
    elif (board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] == board[3][0] and board[0][0] == board[4][0] and board[0][0] == board[5][0] and board[0][0] == mark):
        return True
    elif (board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] == board[3][1] and board[0][1] == board[4][1] and board[0][1] == board[5][1] and board[0][1] == mark):
        return True
    elif (board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] == board[3][2] and board[0][2] == board[4][2] and board[0][2] == board[5][2] and board[0][2] == mark):
        return True
    elif (board[0][3] == board[1][3] and board[0][3] == board[2][3] and board[0][3] == board[3][3] and board[0][3] == board[4][3] and board[0][3] == board[5][3] and board[0][3]== mark):
        return True
    elif (board[0][4] == board[1][4] and board[0][4] == board[2][4] and board[0][4] == board[3][4] and board[0][4] == board[4][4] and board[0][4] == board[5][4] and board[0][4]== mark):
        return True
    elif (board[0][5] == board[1][5] and board[0][5] == board[2][5] and board[0][5] == board[3][5] and board[0][5] == board[4][5] and board[0][5] == board[5][5] and board[0][5]== mark):
        return True
    elif (board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == board[3][3] and board[0][0] == board[4][4] and board[0][0] == board[5][5] and board[0][0] == mark):
        return True
    elif (board[5][0] == board[4][1] and board[5][0] == board[3][2] and board[5][0] == board[2][3] and board[5][0] == board[1][4] and board[5][0] == board[0][5] and board[5][0] == mark):
        return True
    else:
        return False
    
    
    
def heuristic6(board):
    
    
    #mark is the first player looking to maximize the score
    mark = ' X '
    #Opp is the second player looking to minimize the score
    opp= ' O '
    
    xlines = 0
    olines = 0
    
    #check how many open lines exist for the X player
    if (board[0][0] != opp and board[0][1] != opp and board[0][2] != opp and board[0][3] != opp and board[0][4] != opp and board[0][5] != opp):
        xlines +=1
    if (board[1][0] != opp and board[1][1] != opp and board[1][2] != opp and board[1][3] != opp and board[1][4] != opp and board[1][5] != opp):
        xlines +=1
    if (board[2][0] != opp and board[2][1] != opp and board[2][2] != opp and board[2][3] != opp and board[2][4] != opp and board[2][5] != opp):
        xlines +=1
    if (board[3][0] != opp and board[3][1] != opp and board[3][2] != opp and board[3][3] != opp and board[3][4] != opp and board[3][5] != opp):
        xlines +=1
    if (board[4][0] != opp and board[4][1] != opp and board[4][2] != opp and board[4][3] != opp and board[4][4] != opp and board[4][5] != opp):
        xlines +=1
    if (board[5][0] != opp and board[5][1] != opp and board[5][2] != opp and board[5][3] != opp and board[5][4] != opp and board[5][5] != opp):
        xlines +=1
    if (board[0][0] != opp and board[1][0] != opp and board[2][0] != opp and board[3][0] != opp and board[4][0] != opp and board[5][0] != opp):
       xlines +=1
    if (board[0][1] != opp and board[1][1] != opp and board[2][1] != opp and board[3][1] != opp and board[4][1] != opp and board[5][1] != opp):
        xlines +=1
    if (board[0][2] != opp and board[1][2] != opp and board[2][2] != opp and board[3][2] != opp and board[4][2] != opp and board[5][2] != opp):
        xlines +=1
    if (board[0][3] != opp and board[1][3] != opp and board[2][3] != opp and board[3][3] != opp and board[4][3] != opp and board[5][3] != opp):
        xlines +=1
    if (board[0][4] != opp and board[1][4] != opp and board[2][4] != opp and board[3][4] != opp and board[4][4] != opp and board[5][4] != opp):
        xlines +=1
    if (board[0][5] != opp and board[1][5] != opp and board[2][5] != opp and board[3][5] != opp and board[4][5] != opp and board[5][5] != opp):
        xlines +=1
    if (board[0][0] != opp and board[1][1] != opp and board[2][2] != opp and board[3][3] != opp and board[4][4] != opp and board[5][5] != opp):
        xlines +=1
    if (board[5][0] != opp and board[4][1] != opp and board[3][2] != opp and board[2][3] != opp and board[1][4] != opp and board[0][5] != opp):
        xlines +=1
    
    
    #Check open lines for the O player    
    if (board[0][0] != mark and board[0][1] != mark and board[0][2] != mark and board[0][3] != mark and board[0][4] != mark and board[0][5] != mark):
       olines += 1
    if (board[1][0] != mark and board[1][1] != mark and board[1][2] != mark and board[1][3] != mark and board[1][4] != mark and board[1][5] != mark):
       olines += 1
    if (board[2][0] != mark and board[2][1] != mark and board[2][2] != mark and board[2][3] != mark and board[2][4] != mark and board[2][5] != mark):
       olines += 1
    if (board[3][0] != mark and board[3][1] != mark and board[3][2] != mark and board[3][3] != mark and board[3][4] != mark and board[3][5] != mark):
       olines += 1
    if (board[4][0] != mark and board[4][1] != mark and board[4][2] != mark and board[4][3] != mark and board[4][4] != mark and board[4][5] != mark):
       olines += 1
    if (board[5][0] != mark and board[5][1] != mark and board[5][2] != mark and board[5][3] != mark and board[5][4] != mark and board[5][5] != mark):
       olines += 1
    if (board[0][0] != mark and board[1][0] != mark and board[2][0] != mark and board[3][0] != mark and board[4][0] != mark and board[5][0] != mark):
       olines += 1
    if (board[0][1] != mark and board[1][1] != mark and board[2][1] != mark and board[3][1] != mark and board[4][1] != mark and board[5][1] != mark):
       olines += 1
    if (board[0][2] != mark and board[1][2] != mark and board[2][2] != mark and board[3][2] != mark and board[4][2] != mark and board[5][2] != mark):
       olines += 1
    if (board[0][3] != mark and board[1][3] != mark and board[2][3] != mark and board[3][3] != mark and board[4][3] != mark and board[5][3] != mark):
       olines += 1
    if (board[0][4] != mark and board[1][4] != mark and board[2][4] != mark and board[3][4] != mark and board[4][4] != mark and board[5][4] != mark):
       olines += 1
    if (board[0][5] != mark and board[1][5] != mark and board[2][5] != mark and board[3][5] != mark and board[4][5] != mark and board[5][5] != mark):
       olines += 1
    if (board[0][0] != mark and board[1][1] != mark and board[2][2] != mark and board[3][3] != mark and board[4][4] != mark and board[5][5] != mark):
       olines += 1
    if (board[5][0] != mark and board[4][1] != mark and board[3][2] != mark and board[2][3] != mark and board[1][4] != mark and board[0][5] != mark):
       olines += 1
    
           
    heuristic = xlines - olines
    
    return heuristic
    
    
    
    
#7x7 Board Conditions:
    
def fastWinCon7Mark(board, mark):
    if (board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] == board[0][3] and board[0][0] == board[0][4] and board[0][0] == board[0][5] and board[0][0] == board[0][6] and board[0][0] == mark):
        return True
    elif (board[1][0] == board[2][1] and board[1][0] == board[1][2] and board[1][0] == board[1][3] and board[1][0] == board[1][4] and board[1][0] == board[1][5] and board[1][0] == board[1][6] and board[1][0] == mark):
        return True
    elif (board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] == board[2][3] and board[2][0] == board[2][4] and board[2][0] == board[2][5] and board[2][0] == board[2][6] and board[2][0] == mark):
        return True
    elif (board[3][0] == board[3][1] and board[3][0] == board[3][2] and board[3][0] == board[3][3] and board[3][0] == board[3][4] and board[3][0] == board[3][5] and board[3][0] == board[3][6] and board[3][0] == mark):
        return True
    elif (board[4][0] == board[4][1] and board[4][0] == board[4][2] and board[4][0] == board[4][3] and board[4][0] == board[4][4] and board[4][0] == board[4][5] and board[4][0] == board[4][6] and board[4][0] == mark):
        return True
    elif (board[5][0] == board[5][1] and board[5][0] == board[5][2] and board[5][0] == board[5][3] and board[5][0] == board[5][4] and board[5][0] == board[5][5] and board[5][0] == board[5][6] and board[5][0] == mark):
        return True
    elif (board[6][0] == board[6][1] and board[6][0] == board[6][2] and board[6][0] == board[6][3] and board[6][0] == board[6][4] and board[6][0] == board[6][5] and board[6][0] == board[6][6] and board[6][0] == mark):
        return True
    elif (board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] == board[3][0] and board[0][0] == board[4][0] and board[0][0] == board[5][0] and board[0][0] == board[6][0] and board[0][0] == mark):
        return True
    elif (board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] == board[3][1] and board[0][1] == board[4][1] and board[0][1] == board[5][1] and board[0][1] == board[6][1] and board[0][1] == mark):
        return True
    elif (board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] == board[3][2] and board[0][2] == board[4][2] and board[0][2] == board[5][2] and board[0][2] == board[6][2] and board[0][2] == mark):
        return True
    elif (board[0][3] == board[1][3] and board[0][3] == board[2][3] and board[0][3] == board[3][3] and board[0][3] == board[4][3] and board[0][3] == board[5][3] and board[0][3] == board[6][3] and board[0][3] == mark):
        return True
    elif (board[0][4] == board[1][4] and board[0][4] == board[2][4] and board[0][4] == board[3][4] and board[0][4] == board[4][4] and board[0][4] == board[5][4] and board[0][4] == board[6][4] and board[0][4] == mark):
        return True
    elif (board[0][5] == board[1][5] and board[0][5] == board[2][5] and board[0][5] == board[3][5] and board[0][5] == board[4][5] and board[0][5] == board[5][5] and board[0][5] == board[6][5] and board[0][5] == mark):
        return True
    elif (board[0][6] == board[1][6] and board[0][6] == board[2][6] and board[0][6] == board[3][6] and board[0][6] == board[4][6] and board[0][6] == board[5][6] and board[0][6] == board[6][6] and board[0][6] == mark):
        return True
    elif (board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == board[3][3] and board[0][0] == board[4][4] and board[0][0] == board[5][5] and board[0][0] == board[6][6] and board[0][0] == mark):
        return True
    elif (board[6][0] == board[5][1] and board[6][0] == board[4][2] and board[6][0] == board[3][3] and board[6][0] == board[2][4] and board[6][0] == board[1][5] and board[6][0] == board[0][6] and board[6][0] == mark):
        return True
    else:
        return False
    
    
    
def heuristic7(board):
    
    
    #mark is the first player looking to maximize the score
    mark = ' X '
    #Opp is the second player looking to minimize the score
    opp= ' O '
    
    xlines = 0
    olines = 0
    
    #check how many open lines exist for the X player
    if (board[0][0] != opp and board[0][1] != opp and board[0][2] != opp and board[0][3] != opp and board[0][4] != opp and board[0][5] != opp and board[0][6] != opp):
        xlines +=1
    if (board[1][0] != opp and board[1][1] != opp and board[1][2] != opp and board[1][3] != opp and board[1][4] != opp and board[1][5] != opp and board[1][6] != opp):
        xlines +=1
    if (board[2][0] != opp and board[2][1] != opp and board[2][2] != opp and board[2][3] != opp and board[2][4] != opp and board[2][5] != opp and board[2][6] != opp):
        xlines +=1
    if (board[3][0] != opp and board[3][1] != opp and board[3][2] != opp and board[3][3] != opp and board[3][4] != opp and board[3][5] != opp and board[3][6] != opp):
        xlines +=1
    if (board[4][0] != opp and board[4][1] != opp and board[4][2] != opp and board[4][3] != opp and board[4][4] != opp and board[4][5] != opp and board[4][6] != opp):
        xlines +=1
    if (board[5][0] != opp and board[5][1] != opp and board[5][2] != opp and board[5][3] != opp and board[5][4] != opp and board[5][5] != opp and board[5][6] != opp):
        xlines +=1
    if (board[6][0] != opp and board[6][1] != opp and board[6][2] != opp and board[6][3] != opp and board[6][4] != opp and board[6][5] != opp and board[6][6] != opp):
        xlines +=1    
    if (board[0][0] != opp and board[1][0] != opp and board[2][0] != opp and board[3][0] != opp and board[4][0] != opp and board[5][0] != opp and board[6][0] != opp):
       xlines +=1
    if (board[0][1] != opp and board[1][1] != opp and board[2][1] != opp and board[3][1] != opp and board[4][1] != opp and board[5][1] != opp and board[6][1] != opp):
        xlines +=1
    if (board[0][2] != opp and board[1][2] != opp and board[2][2] != opp and board[3][2] != opp and board[4][2] != opp and board[5][2] != opp and board[6][2] != opp):
        xlines +=1
    if (board[0][3] != opp and board[1][3] != opp and board[2][3] != opp and board[3][3] != opp and board[4][3] != opp and board[5][3] != opp and board[6][3] != opp):
        xlines +=1
    if (board[0][4] != opp and board[1][4] != opp and board[2][4] != opp and board[3][4] != opp and board[4][4] != opp and board[5][4] != opp and board[6][4] != opp):
        xlines +=1
    if (board[0][5] != opp and board[1][5] != opp and board[2][5] != opp and board[3][5] != opp and board[4][5] != opp and board[5][5] != opp and board[6][5] != opp):
        xlines +=1
    if (board[0][6] != opp and board[1][6] != opp and board[2][6] != opp and board[3][6] != opp and board[4][6] != opp and board[5][6] != opp and board[6][6] != opp):
        xlines +=1    
    if (board[0][0] != opp and board[1][1] != opp and board[2][2] != opp and board[3][3] != opp and board[4][4] != opp and board[5][5] != opp and board[6][6] != opp):
        xlines +=1
    if (board[6][0] != opp and board[5][1] != opp and board[4][2] != opp and board[3][3] != opp and board[2][4] != opp and board[1][5] != opp and board[0][6] != opp):
        xlines +=1
    
    
    #Check open lines for the O player    
    if (board[0][0] != mark and board[0][1] != mark and board[0][2] != mark and board[0][3] != mark and board[0][4] != mark and board[0][5] != mark and board[0][6] != mark):
        olines +=1
    if (board[1][0] != mark and board[1][1] != mark and board[1][2] != mark and board[1][3] != mark and board[1][4] != mark and board[1][5] != mark and board[1][6] != mark):
        olines +=1
    if (board[2][0] != mark and board[2][1] != mark and board[2][2] != mark and board[2][3] != mark and board[2][4] != mark and board[2][5] != mark and board[2][6] != mark):
        olines +=1
    if (board[3][0] != mark and board[3][1] != mark and board[3][2] != mark and board[3][3] != mark and board[3][4] != mark and board[3][5] != mark and board[3][6] != mark):
        olines +=1
    if (board[4][0] != mark and board[4][1] != mark and board[4][2] != mark and board[4][3] != mark and board[4][4] != mark and board[4][5] != mark and board[4][6] != mark):
        olines +=1
    if (board[5][0] != mark and board[5][1] != mark and board[5][2] != mark and board[5][3] != mark and board[5][4] != mark and board[5][5] != mark and board[5][6] != mark):
        olines +=1
    if (board[6][0] != mark and board[6][1] != mark and board[6][2] != mark and board[6][3] != mark and board[6][4] != mark and board[6][5] != mark and board[6][6] != mark):
        olines +=1    
    if (board[0][0] != mark and board[1][0] != mark and board[2][0] != mark and board[3][0] != mark and board[4][0] != mark and board[5][0] != mark and board[6][0] != mark):
       olines +=1
    if (board[0][1] != mark and board[1][1] != mark and board[2][1] != mark and board[3][1] != mark and board[4][1] != mark and board[5][1] != mark and board[6][1] != mark):
        olines +=1
    if (board[0][2] != mark and board[1][2] != mark and board[2][2] != mark and board[3][2] != mark and board[4][2] != mark and board[5][2] != mark and board[6][2] != mark):
        olines +=1
    if (board[0][3] != mark and board[1][3] != mark and board[2][3] != mark and board[3][3] != mark and board[4][3] != mark and board[5][3] != mark and board[6][3] != mark):
        olines +=1
    if (board[0][4] != mark and board[1][4] != mark and board[2][4] != mark and board[3][4] != mark and board[4][4] != mark and board[5][4] != mark and board[6][4] != mark):
        olines +=1
    if (board[0][5] != mark and board[1][5] != mark and board[2][5] != mark and board[3][5] != mark and board[4][5] != mark and board[5][5] != mark and board[6][5] != mark):
        olines +=1
    if (board[0][6] != mark and board[1][6] != mark and board[2][6] != mark and board[3][6] != mark and board[4][6] != mark and board[5][6] != mark and board[6][6] != mark):
        olines +=1    
    if (board[0][0] != mark and board[1][1] != mark and board[2][2] != mark and board[3][3] != mark and board[4][4] != mark and board[5][5] != mark and board[6][6] != mark):
        olines +=1
    if (board[6][0] != mark and board[5][1] != mark and board[4][2] != mark and board[3][3] != mark and board[2][4] != mark and board[1][5] != mark and board[0][6] != mark):
        olines +=1
    
           
    heuristic = xlines - olines
    
    return heuristic
    
    
    
    
#8x8 Board Conditions
def fastWinCon8Mark(board, mark):
    if (board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] == board[0][3] and board[0][0] == board[0][4] and board[0][0] == board[0][5] and board[0][0] == board[0][6] and board[0][0] == board[0][7] and board[0][0] == mark):
        return True
    elif (board[1][0] == board[2][1] and board[1][0] == board[1][2] and board[1][0] == board[1][3] and board[1][0] == board[1][4] and board[1][0] == board[1][5] and board[1][0] == board[1][6] and board[1][0] == board[1][7] and board[1][0] == mark):
        return True
    elif (board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] == board[2][3] and board[2][0] == board[2][4] and board[2][0] == board[2][5] and board[2][0] == board[2][6] and board[2][0] == board[2][7] and board[2][0] == mark):
        return True
    elif (board[3][0] == board[3][1] and board[3][0] == board[3][2] and board[3][0] == board[3][3] and board[3][0] == board[3][4] and board[3][0] == board[3][5] and board[3][0] == board[3][6] and board[3][0] == board[3][7] and board[3][0] == mark):
        return True
    elif (board[4][0] == board[4][1] and board[4][0] == board[4][2] and board[4][0] == board[4][3] and board[4][0] == board[4][4] and board[4][0] == board[4][5] and board[4][0] == board[4][6] and board[4][0] == board[4][7] and board[4][0] == mark):
        return True
    elif (board[5][0] == board[5][1] and board[5][0] == board[5][2] and board[5][0] == board[5][3] and board[5][0] == board[5][4] and board[5][0] == board[5][5] and board[5][0] == board[5][6] and board[5][0] == board[5][7] and board[5][0] == mark):
        return True
    elif (board[6][0] == board[6][1] and board[6][0] == board[6][2] and board[6][0] == board[6][3] and board[6][0] == board[6][4] and board[6][0] == board[6][5] and board[6][0] == board[6][6] and board[6][0] == board[6][7] and board[6][0] == mark):
        return True
    elif (board[7][0] == board[7][1] and board[7][0] == board[7][2] and board[7][0] == board[7][3] and board[7][0] == board[7][4] and board[7][0] == board[7][5] and board[7][0] == board[7][6] and board[7][0] == board[7][7] and board[7][0] == mark):
        return True
    elif (board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] == board[3][0] and board[0][0] == board[4][0] and board[0][0] == board[5][0] and board[0][0] == board[6][0] and board[0][0] == board[7][0] and board[0][0] == mark):
        return True
    elif (board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] == board[3][1] and board[0][1] == board[4][1] and board[0][1] == board[5][1] and board[0][1] == board[6][1] and board[0][1] == board[7][1] and board[0][1] == mark):
        return True
    elif (board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] == board[3][2] and board[0][2] == board[4][2] and board[0][2] == board[5][2] and board[0][2] == board[6][2] and board[0][2] == board[7][2] and board[0][2] == mark):
        return True
    elif (board[0][3] == board[1][3] and board[0][3] == board[2][3] and board[0][3] == board[3][3] and board[0][3] == board[4][3] and board[0][3] == board[5][3] and board[0][3] == board[6][3] and board[0][3] == board[7][3] and board[0][3] == mark):
        return True
    elif (board[0][4] == board[1][4] and board[0][4] == board[2][4] and board[0][4] == board[3][4] and board[0][4] == board[4][4] and board[0][4] == board[5][4] and board[0][4] == board[6][4] and board[0][4] == board[7][4] and board[0][4] == mark):
        return True
    elif (board[0][5] == board[1][5] and board[0][5] == board[2][5] and board[0][5] == board[3][5] and board[0][5] == board[4][5] and board[0][5] == board[5][5] and board[0][5] == board[6][5] and board[0][5] == board[7][5] and board[0][5] == mark):
        return True
    elif (board[0][6] == board[1][6] and board[0][6] == board[2][6] and board[0][6] == board[3][6] and board[0][6] == board[4][6] and board[0][6] == board[5][6] and board[0][6] == board[6][6] and board[0][6] == board[7][6] and board[0][6] == mark):
        return True
    elif (board[0][7] == board[1][7] and board[0][7] == board[2][7] and board[0][7] == board[3][7] and board[0][7] == board[4][7] and board[0][7] == board[5][7] and board[0][7] == board[6][7] and board[0][7] == board[7][7] and board[0][7] == mark):
        return True
    elif (board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == board[3][3] and board[0][0] == board[4][4] and board[0][0] == board[5][5] and board[0][0] == board[6][6] and board[0][0] == board[7][7] and board[0][0] == mark):
        return True
    elif (board[7][0] == board[6][1] and board[7][0] == board[5][2] and board[7][0] == board[4][3] and board[7][0] == board[3][4] and board[7][0] == board[2][5] and board[7][0] == board[1][6] and board[7][0] == board[0][7] and board[7][0] == mark):
        return True
    else:
        return False
    
    
    
def heuristic8(board):
    
    
    #mark is the first player looking to maximize the score
    mark = ' X '
    #Opp is the second player looking to minimize the score
    opp= ' O '
    
    xlines = 0
    olines = 0
    
    #check how many open lines exist for the X player
    if (board[0][0] != opp and board[0][1] != opp and board[0][2] != opp and board[0][3] != opp and board[0][4] != opp and board[0][5] != opp and board[0][6] != opp and board[0][7] != opp):
        xlines +=1
    if (board[1][0] != opp and board[1][1] != opp and board[1][2] != opp and board[1][3] != opp and board[1][4] != opp and board[1][5] != opp and board[1][6] != opp and board[1][7] != opp):
        xlines +=1
    if (board[2][0] != opp and board[2][1] != opp and board[2][2] != opp and board[2][3] != opp and board[2][4] != opp and board[2][5] != opp and board[2][6] != opp and board[2][7] != opp):
        xlines +=1
    if (board[3][0] != opp and board[3][1] != opp and board[3][2] != opp and board[3][3] != opp and board[3][4] != opp and board[3][5] != opp and board[3][6] != opp and board[3][7] != opp):
        xlines +=1
    if (board[4][0] != opp and board[4][1] != opp and board[4][2] != opp and board[4][3] != opp and board[4][4] != opp and board[4][5] != opp and board[4][6] != opp and board[4][7] != opp):
        xlines +=1
    if (board[5][0] != opp and board[5][1] != opp and board[5][2] != opp and board[5][3] != opp and board[5][4] != opp and board[5][5] != opp and board[5][6] != opp and board[5][7] != opp):
        xlines +=1
    if (board[6][0] != opp and board[6][1] != opp and board[6][2] != opp and board[6][3] != opp and board[6][4] != opp and board[6][5] != opp and board[6][6] != opp and board[6][7] != opp):
        xlines +=1
    if (board[7][0] != opp and board[7][1] != opp and board[7][2] != opp and board[7][3] != opp and board[7][4] != opp and board[7][5] != opp and board[7][6] != opp and board[7][7] != opp):
        xlines +=1    
    if (board[0][0] != opp and board[1][0] != opp and board[2][0] != opp and board[3][0] != opp and board[4][0] != opp and board[5][0] != opp and board[6][0] != opp and board[7][0] != opp):
       xlines +=1
    if (board[0][1] != opp and board[1][1] != opp and board[2][1] != opp and board[3][1] != opp and board[4][1] != opp and board[5][1] != opp and board[6][1] != opp and board[7][1] != opp):
        xlines +=1
    if (board[0][2] != opp and board[1][2] != opp and board[2][2] != opp and board[3][2] != opp and board[4][2] != opp and board[5][2] != opp and board[6][2] != opp and board[7][2] != opp):
        xlines +=1
    if (board[0][3] != opp and board[1][3] != opp and board[2][3] != opp and board[3][3] != opp and board[4][3] != opp and board[5][3] != opp and board[6][3] != opp and board[7][3] != opp):
        xlines +=1
    if (board[0][4] != opp and board[1][4] != opp and board[2][4] != opp and board[3][4] != opp and board[4][4] != opp and board[5][4] != opp and board[6][4] != opp and board[7][4] != opp):
        xlines +=1
    if (board[0][5] != opp and board[1][5] != opp and board[2][5] != opp and board[3][5] != opp and board[4][5] != opp and board[5][5] != opp and board[6][5] != opp and board[7][5] != opp):
        xlines +=1
    if (board[0][6] != opp and board[1][6] != opp and board[2][6] != opp and board[3][6] != opp and board[4][6] != opp and board[5][6] != opp and board[6][6] != opp and board[7][6] != opp):
        xlines +=1   
    if (board[0][7] != opp and board[1][7] != opp and board[2][7] != opp and board[3][7] != opp and board[4][7] != opp and board[5][7] != opp and board[6][7] != opp and board[7][7] != opp):
        xlines +=1    
    if (board[0][0] != opp and board[1][1] != opp and board[2][2] != opp and board[3][3] != opp and board[4][4] != opp and board[5][5] != opp and board[6][6] != opp and board[7][7] != opp):
        xlines +=1
    if (board[7][0] != opp and board[6][1] != opp and board[5][2] != opp and board[4][3] != opp and board[3][4] != opp and board[2][5] != opp and board[1][6] != opp and board[0][7] != opp):
        xlines +=1
    
    
    #Check open lines for the O player    
    if (board[0][0] != mark and board[0][1] != mark and board[0][2] != mark and board[0][3] != mark and board[0][4] != mark and board[0][5] != mark and board[0][6] != mark and board[0][7] != mark):
        olines +=1
    if (board[1][0] != mark and board[1][1] != mark and board[1][2] != mark and board[1][3] != mark and board[1][4] != mark and board[1][5] != mark and board[1][6] != mark and board[1][7] != mark):
        olines +=1
    if (board[2][0] != mark and board[2][1] != mark and board[2][2] != mark and board[2][3] != mark and board[2][4] != mark and board[2][5] != mark and board[2][6] != mark and board[2][7] != mark):
        olines +=1
    if (board[3][0] != mark and board[3][1] != mark and board[3][2] != mark and board[3][3] != mark and board[3][4] != mark and board[3][5] != mark and board[3][6] != mark and board[3][7] != mark):
        olines +=1
    if (board[4][0] != mark and board[4][1] != mark and board[4][2] != mark and board[4][3] != mark and board[4][4] != mark and board[4][5] != mark and board[4][6] != mark and board[4][7] != mark):
        olines +=1
    if (board[5][0] != mark and board[5][1] != mark and board[5][2] != mark and board[5][3] != mark and board[5][4] != mark and board[5][5] != mark and board[5][6] != mark and board[5][7] != mark):
        olines +=1
    if (board[6][0] != mark and board[6][1] != mark and board[6][2] != mark and board[6][3] != mark and board[6][4] != mark and board[6][5] != mark and board[6][6] != mark and board[6][7] != mark):
        olines +=1
    if (board[7][0] != mark and board[7][1] != mark and board[7][2] != mark and board[7][3] != mark and board[7][4] != mark and board[7][5] != mark and board[7][6] != mark and board[7][7] != mark):
        olines +=1    
    if (board[0][0] != mark and board[1][0] != mark and board[2][0] != mark and board[3][0] != mark and board[4][0] != mark and board[5][0] != mark and board[6][0] != mark and board[7][0] != mark):
       olines +=1
    if (board[0][1] != mark and board[1][1] != mark and board[2][1] != mark and board[3][1] != mark and board[4][1] != mark and board[5][1] != mark and board[6][1] != mark and board[7][1] != mark):
        olines +=1
    if (board[0][2] != mark and board[1][2] != mark and board[2][2] != mark and board[3][2] != mark and board[4][2] != mark and board[5][2] != mark and board[6][2] != mark and board[7][2] != mark):
        olines +=1
    if (board[0][3] != mark and board[1][3] != mark and board[2][3] != mark and board[3][3] != mark and board[4][3] != mark and board[5][3] != mark and board[6][3] != mark and board[7][3] != mark):
        olines +=1
    if (board[0][4] != mark and board[1][4] != mark and board[2][4] != mark and board[3][4] != mark and board[4][4] != mark and board[5][4] != mark and board[6][4] != mark and board[7][4] != mark):
        olines +=1
    if (board[0][5] != mark and board[1][5] != mark and board[2][5] != mark and board[3][5] != mark and board[4][5] != mark and board[5][5] != mark and board[6][5] != mark and board[7][5] != mark):
        olines +=1
    if (board[0][6] != mark and board[1][6] != mark and board[2][6] != mark and board[3][6] != mark and board[4][6] != mark and board[5][6] != mark and board[6][6] != mark and board[7][6] != mark):
        olines +=1   
    if (board[0][7] != mark and board[1][7] != mark and board[2][7] != mark and board[3][7] != mark and board[4][7] != mark and board[5][7] != mark and board[6][7] != mark and board[7][7] != mark):
        olines +=1    
    if (board[0][0] != mark and board[1][1] != mark and board[2][2] != mark and board[3][3] != mark and board[4][4] != mark and board[5][5] != mark and board[6][6] != mark and board[7][7] != mark):
        olines +=1
    if (board[7][0] != mark and board[6][1] != mark and board[5][2] != mark and board[4][3] != mark and board[3][4] != mark and board[2][5] != mark and board[1][6] != mark and board[0][7] != mark):
        olines +=1
    
           
    heuristic = xlines - olines
    
    return heuristic






#9x9 Board Conditions:
    
def fastWinCon9Mark(board, mark):
    if (board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] == board[0][3] and board[0][0] == board[0][4] and board[0][0] == board[0][5] and board[0][0] == board[0][6] and board[0][0] == board[0][7] and board[0][0] == board[0][8] and board[0][0] == mark):
        return True
    elif (board[1][0] == board[2][1] and board[1][0] == board[1][2] and board[1][0] == board[1][3] and board[1][0] == board[1][4] and board[1][0] == board[1][5] and board[1][0] == board[1][6] and board[1][0] == board[1][7] and board[1][0] == board[1][8] and board[1][0] == mark):
        return True
    elif (board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] == board[2][3] and board[2][0] == board[2][4] and board[2][0] == board[2][5] and board[2][0] == board[2][6] and board[2][0] == board[2][7] and board[2][0] == board[2][8] and board[2][0] == mark):
        return True
    elif (board[3][0] == board[3][1] and board[3][0] == board[3][2] and board[3][0] == board[3][3] and board[3][0] == board[3][4] and board[3][0] == board[3][5] and board[3][0] == board[3][6] and board[3][0] == board[3][7] and board[3][0] == board[3][8] and board[3][0] == mark):
        return True
    elif (board[4][0] == board[4][1] and board[4][0] == board[4][2] and board[4][0] == board[4][3] and board[4][0] == board[4][4] and board[4][0] == board[4][5] and board[4][0] == board[4][6] and board[4][0] == board[4][7] and board[4][0] == board[4][8] and board[4][0] == mark):
        return True
    elif (board[5][0] == board[5][1] and board[5][0] == board[5][2] and board[5][0] == board[5][3] and board[5][0] == board[5][4] and board[5][0] == board[5][5] and board[5][0] == board[5][6] and board[5][0] == board[5][7] and board[5][0] == board[5][8] and board[5][0] == mark):
        return True
    elif (board[6][0] == board[6][1] and board[6][0] == board[6][2] and board[6][0] == board[6][3] and board[6][0] == board[6][4] and board[6][0] == board[6][5] and board[6][0] == board[6][6] and board[6][0] == board[6][7] and board[6][0] == board[6][8] and board[6][0] == mark):
        return True
    elif (board[7][0] == board[7][1] and board[7][0] == board[7][2] and board[7][0] == board[7][3] and board[7][0] == board[7][4] and board[7][0] == board[7][5] and board[7][0] == board[7][6] and board[7][0] == board[7][7] and board[7][0] == board[7][8] and board[7][0] == mark):
        return True
    elif (board[8][0] == board[8][1] and board[8][0] == board[8][2] and board[8][0] == board[8][3] and board[8][0] == board[8][4] and board[8][0] == board[8][5] and board[8][0] == board[8][6] and board[8][0] == board[8][7] and board[8][0] == board[8][8] and board[8][0] == mark):
        return True
    elif (board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] == board[3][0] and board[0][0] == board[4][0] and board[0][0] == board[5][0] and board[0][0] == board[6][0] and board[0][0] == board[7][0] and board[0][0] == board[8][0] and board[0][0] == mark):
        return True
    elif (board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] == board[3][1] and board[0][1] == board[4][1] and board[0][1] == board[5][1] and board[0][1] == board[6][1] and board[0][1] == board[7][1] and board[0][1] == board[8][1] and board[0][1] == mark):
        return True
    elif (board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] == board[3][2] and board[0][2] == board[4][2] and board[0][2] == board[5][2] and board[0][2] == board[6][2] and board[0][2] == board[7][2] and board[0][2] == board[8][2] and board[0][2] == mark):
        return True
    elif (board[0][3] == board[1][3] and board[0][3] == board[2][3] and board[0][3] == board[3][3] and board[0][3] == board[4][3] and board[0][3] == board[5][3] and board[0][3] == board[6][3] and board[0][3] == board[7][3] and board[0][3] == board[8][3] and board[0][3] == mark):
        return True
    elif (board[0][4] == board[1][4] and board[0][4] == board[2][4] and board[0][4] == board[3][4] and board[0][4] == board[4][4] and board[0][4] == board[5][4] and board[0][4] == board[6][4] and board[0][4] == board[7][4] and board[0][4] == board[8][4] and board[0][4] == mark):
        return True
    elif (board[0][5] == board[1][5] and board[0][5] == board[2][5] and board[0][5] == board[3][5] and board[0][5] == board[4][5] and board[0][5] == board[5][5] and board[0][5] == board[6][5] and board[0][5] == board[7][5] and board[0][5] == board[8][5] and board[0][5] == mark):
        return True
    elif (board[0][6] == board[1][6] and board[0][6] == board[2][6] and board[0][6] == board[3][6] and board[0][6] == board[4][6] and board[0][6] == board[5][6] and board[0][6] == board[6][6] and board[0][6] == board[7][6] and board[0][6] == board[8][6] and board[0][6] == mark):
        return True
    elif (board[0][7] == board[1][7] and board[0][7] == board[2][7] and board[0][7] == board[3][7] and board[0][7] == board[4][7] and board[0][7] == board[5][7] and board[0][7] == board[6][7] and board[0][7] == board[7][7] and board[0][7] == board[8][7] and board[0][7] == mark):
        return True
    elif (board[0][8] == board[1][8] and board[0][8] == board[2][8] and board[0][8] == board[3][8] and board[0][8] == board[4][8] and board[0][8] == board[5][8] and board[0][8] == board[6][8] and board[0][8] == board[7][8] and board[0][8] == board[8][8] and board[0][8] == mark):
        return True
    elif (board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == board[3][3] and board[0][0] == board[4][4] and board[0][0] == board[5][5] and board[0][0] == board[6][6] and board[0][0] == board[7][7] and board[0][0] == board[8][8] and board[0][0] == mark):
        return True
    elif (board[8][0] == board[7][1] and board[8][0] == board[6][2] and board[8][0] == board[5][3] and board[8][0] == board[4][4] and board[8][0] == board[3][5] and board[8][0] == board[2][6] and board[8][0] == board[1][7] and board[8][0] == board[0][8] and board[8][0] == mark):
        return True
    else:
        return False
    
    
    
def heuristic9(board):
    
    
    #mark is the first player looking to maximize the score
    mark = ' X '
    #Opp is the second player looking to minimize the score
    opp= ' O '
    
    xlines = 0
    olines = 0
    
    #check how many open lines exist for the X player
    if (board[0][0] != opp and board[0][1] != opp and board[0][2] != opp and board[0][3] != opp and board[0][4] != opp and board[0][5] != opp and board[0][6] != opp and board[0][7] != opp and board[0][8] != opp):
        xlines +=1
    if (board[1][0] != opp and board[1][1] != opp and board[1][2] != opp and board[1][3] != opp and board[1][4] != opp and board[1][5] != opp and board[1][6] != opp and board[1][7] != opp and board[1][8] != opp):
        xlines +=1
    if (board[2][0] != opp and board[2][1] != opp and board[2][2] != opp and board[2][3] != opp and board[2][4] != opp and board[2][5] != opp and board[2][6] != opp and board[2][7] != opp and board[2][8] != opp):
        xlines +=1
    if (board[3][0] != opp and board[3][1] != opp and board[3][2] != opp and board[3][3] != opp and board[3][4] != opp and board[3][5] != opp and board[3][6] != opp and board[3][7] != opp and board[3][8] != opp):
        xlines +=1
    if (board[4][0] != opp and board[4][1] != opp and board[4][2] != opp and board[4][3] != opp and board[4][4] != opp and board[4][5] != opp and board[4][6] != opp and board[4][7] != opp and board[4][8] != opp):
        xlines +=1
    if (board[5][0] != opp and board[5][1] != opp and board[5][2] != opp and board[5][3] != opp and board[5][4] != opp and board[5][5] != opp and board[5][6] != opp and board[5][7] != opp and board[5][8] != opp):
        xlines +=1
    if (board[6][0] != opp and board[6][1] != opp and board[6][2] != opp and board[6][3] != opp and board[6][4] != opp and board[6][5] != opp and board[6][6] != opp and board[6][7] != opp and board[6][8] != opp):
        xlines +=1
    if (board[7][0] != opp and board[7][1] != opp and board[7][2] != opp and board[7][3] != opp and board[7][4] != opp and board[7][5] != opp and board[7][6] != opp and board[7][7] != opp and board[7][8] != opp):
        xlines +=1  
    if (board[8][0] != opp and board[8][1] != opp and board[8][2] != opp and board[8][3] != opp and board[8][4] != opp and board[8][5] != opp and board[8][6] != opp and board[8][7] != opp and board[8][8] != opp):
        xlines +=1    
    if (board[0][0] != opp and board[1][0] != opp and board[2][0] != opp and board[3][0] != opp and board[4][0] != opp and board[5][0] != opp and board[6][0] != opp and board[7][0] != opp and board[8][0] != opp):
       xlines +=1
    if (board[0][1] != opp and board[1][1] != opp and board[2][1] != opp and board[3][1] != opp and board[4][1] != opp and board[5][1] != opp and board[6][1] != opp and board[7][1] != opp and board[8][1] != opp):
        xlines +=1
    if (board[0][2] != opp and board[1][2] != opp and board[2][2] != opp and board[3][2] != opp and board[4][2] != opp and board[5][2] != opp and board[6][2] != opp and board[7][2] != opp and board[8][2] != opp):
        xlines +=1
    if (board[0][3] != opp and board[1][3] != opp and board[2][3] != opp and board[3][3] != opp and board[4][3] != opp and board[5][3] != opp and board[6][3] != opp and board[7][3] != opp and board[8][3] != opp):
        xlines +=1
    if (board[0][4] != opp and board[1][4] != opp and board[2][4] != opp and board[3][4] != opp and board[4][4] != opp and board[5][4] != opp and board[6][4] != opp and board[7][4] != opp and board[8][4] != opp):
        xlines +=1
    if (board[0][5] != opp and board[1][5] != opp and board[2][5] != opp and board[3][5] != opp and board[4][5] != opp and board[5][5] != opp and board[6][5] != opp and board[7][5] != opp and board[8][5] != opp):
        xlines +=1
    if (board[0][6] != opp and board[1][6] != opp and board[2][6] != opp and board[3][6] != opp and board[4][6] != opp and board[5][6] != opp and board[6][6] != opp and board[7][6] != opp and board[8][6] != opp):
        xlines +=1   
    if (board[0][7] != opp and board[1][7] != opp and board[2][7] != opp and board[3][7] != opp and board[4][7] != opp and board[5][7] != opp and board[6][7] != opp and board[7][7] != opp and board[8][7] != opp):
        xlines +=1  
    if (board[0][8] != opp and board[1][8] != opp and board[2][8] != opp and board[3][8] != opp and board[4][8] != opp and board[5][8] != opp and board[6][8] != opp and board[7][8] != opp and board[8][8] != opp):
        xlines +=1    
    if (board[0][0] != opp and board[1][1] != opp and board[2][2] != opp and board[3][3] != opp and board[4][4] != opp and board[5][5] != opp and board[6][6] != opp and board[7][7] != opp and board[8][8] != opp):
        xlines +=1
    if (board[8][0] != opp and board[7][1] != opp and board[6][2] != opp and board[5][3] != opp and board[4][4] != opp and board[3][5] != opp and board[2][6] != opp and board[1][7] != opp and board[0][8] != opp):
        xlines +=1
    
    
    #Check open lines for the O player    
    if (board[0][0] != mark and board[0][1] != mark and board[0][2] != mark and board[0][3] != mark and board[0][4] != mark and board[0][5] != mark and board[0][6] != mark and board[0][7] != mark and board[0][8] != mark):
        olines +=1
    if (board[1][0] != mark and board[1][1] != mark and board[1][2] != mark and board[1][3] != mark and board[1][4] != mark and board[1][5] != mark and board[1][6] != mark and board[1][7] != mark and board[1][8] != mark):
        olines +=1
    if (board[2][0] != mark and board[2][1] != mark and board[2][2] != mark and board[2][3] != mark and board[2][4] != mark and board[2][5] != mark and board[2][6] != mark and board[2][7] != mark and board[2][8] != mark):
        olines +=1
    if (board[3][0] != mark and board[3][1] != mark and board[3][2] != mark and board[3][3] != mark and board[3][4] != mark and board[3][5] != mark and board[3][6] != mark and board[3][7] != mark and board[3][8] != mark):
        olines +=1
    if (board[4][0] != mark and board[4][1] != mark and board[4][2] != mark and board[4][3] != mark and board[4][4] != mark and board[4][5] != mark and board[4][6] != mark and board[4][7] != mark and board[4][8] != mark):
        olines +=1
    if (board[5][0] != mark and board[5][1] != mark and board[5][2] != mark and board[5][3] != mark and board[5][4] != mark and board[5][5] != mark and board[5][6] != mark and board[5][7] != mark and board[5][8] != mark):
        olines +=1
    if (board[6][0] != mark and board[6][1] != mark and board[6][2] != mark and board[6][3] != mark and board[6][4] != mark and board[6][5] != mark and board[6][6] != mark and board[6][7] != mark and board[6][8] != mark):
        olines +=1
    if (board[7][0] != mark and board[7][1] != mark and board[7][2] != mark and board[7][3] != mark and board[7][4] != mark and board[7][5] != mark and board[7][6] != mark and board[7][7] != mark and board[7][8] != mark):
        olines +=1  
    if (board[8][0] != mark and board[8][1] != mark and board[8][2] != mark and board[8][3] != mark and board[8][4] != mark and board[8][5] != mark and board[8][6] != mark and board[8][7] != mark and board[8][8] != mark):
        olines +=1    
    if (board[0][0] != mark and board[1][0] != mark and board[2][0] != mark and board[3][0] != mark and board[4][0] != mark and board[5][0] != mark and board[6][0] != mark and board[7][0] != mark and board[8][0] != mark):
       olines +=1
    if (board[0][1] != mark and board[1][1] != mark and board[2][1] != mark and board[3][1] != mark and board[4][1] != mark and board[5][1] != mark and board[6][1] != mark and board[7][1] != mark and board[8][1] != mark):
        olines +=1
    if (board[0][2] != mark and board[1][2] != mark and board[2][2] != mark and board[3][2] != mark and board[4][2] != mark and board[5][2] != mark and board[6][2] != mark and board[7][2] != mark and board[8][2] != mark):
        olines +=1
    if (board[0][3] != mark and board[1][3] != mark and board[2][3] != mark and board[3][3] != mark and board[4][3] != mark and board[5][3] != mark and board[6][3] != mark and board[7][3] != mark and board[8][3] != mark):
        olines +=1
    if (board[0][4] != mark and board[1][4] != mark and board[2][4] != mark and board[3][4] != mark and board[4][4] != mark and board[5][4] != mark and board[6][4] != mark and board[7][4] != mark and board[8][4] != mark):
        olines +=1
    if (board[0][5] != mark and board[1][5] != mark and board[2][5] != mark and board[3][5] != mark and board[4][5] != mark and board[5][5] != mark and board[6][5] != mark and board[7][5] != mark and board[8][5] != mark):
        olines +=1
    if (board[0][6] != mark and board[1][6] != mark and board[2][6] != mark and board[3][6] != mark and board[4][6] != mark and board[5][6] != mark and board[6][6] != mark and board[7][6] != mark and board[8][6] != mark):
        olines +=1   
    if (board[0][7] != mark and board[1][7] != mark and board[2][7] != mark and board[3][7] != mark and board[4][7] != mark and board[5][7] != mark and board[6][7] != mark and board[7][7] != mark and board[8][7] != mark):
        olines +=1  
    if (board[0][8] != mark and board[1][8] != mark and board[2][8] != mark and board[3][8] != mark and board[4][8] != mark and board[5][8] != mark and board[6][8] != mark and board[7][8] != mark and board[8][8] != mark):
        olines +=1    
    if (board[0][0] != mark and board[1][1] != mark and board[2][2] != mark and board[3][3] != mark and board[4][4] != mark and board[5][5] != mark and board[6][6] != mark and board[7][7] != mark and board[8][8] != mark):
        olines +=1
    if (board[8][0] != mark and board[7][1] != mark and board[6][2] != mark and board[5][3] != mark and board[4][4] != mark and board[3][5] != mark and board[2][6] != mark and board[1][7] != mark and board[0][8] != mark):
        olines +=1
    
           
    heuristic = xlines - olines
    
    return heuristic




#10x10 Board Conditions

def fastWinCon10Mark(board, mark):
    if (board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] == board[0][3] and board[0][0] == board[0][4] and board[0][0] == board[0][5] and board[0][0] == board[0][6] and board[0][0] == board[0][7] and board[0][0] == board[0][8] and board[0][0] == board[0][9] and board[0][0] == mark):
        return True
    elif (board[1][0] == board[2][1] and board[1][0] == board[1][2] and board[1][0] == board[1][3] and board[1][0] == board[1][4] and board[1][0] == board[1][5] and board[1][0] == board[1][6] and board[1][0] == board[1][7] and board[1][0] == board[1][8] and board[1][0] == board[0][9] and board[1][0] == mark):
        return True
    elif (board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] == board[2][3] and board[2][0] == board[2][4] and board[2][0] == board[2][5] and board[2][0] == board[2][6] and board[2][0] == board[2][7] and board[2][0] == board[2][8] and board[2][0] == board[0][9] and board[2][0] == mark):
        return True
    elif (board[3][0] == board[3][1] and board[3][0] == board[3][2] and board[3][0] == board[3][3] and board[3][0] == board[3][4] and board[3][0] == board[3][5] and board[3][0] == board[3][6] and board[3][0] == board[3][7] and board[3][0] == board[3][8] and board[3][0] == board[0][9] and board[3][0] == mark):
        return True
    elif (board[4][0] == board[4][1] and board[4][0] == board[4][2] and board[4][0] == board[4][3] and board[4][0] == board[4][4] and board[4][0] == board[4][5] and board[4][0] == board[4][6] and board[4][0] == board[4][7] and board[4][0] == board[4][8] and board[4][0] == board[0][9] and board[4][0] == mark):
        return True
    elif (board[5][0] == board[5][1] and board[5][0] == board[5][2] and board[5][0] == board[5][3] and board[5][0] == board[5][4] and board[5][0] == board[5][5] and board[5][0] == board[5][6] and board[5][0] == board[5][7] and board[5][0] == board[5][8] and board[5][0] == board[0][9] and board[5][0] == mark):
        return True
    elif (board[6][0] == board[6][1] and board[6][0] == board[6][2] and board[6][0] == board[6][3] and board[6][0] == board[6][4] and board[6][0] == board[6][5] and board[6][0] == board[6][6] and board[6][0] == board[6][7] and board[6][0] == board[6][8] and board[6][0] == board[0][9] and board[6][0] == mark):
        return True
    elif (board[7][0] == board[7][1] and board[7][0] == board[7][2] and board[7][0] == board[7][3] and board[7][0] == board[7][4] and board[7][0] == board[7][5] and board[7][0] == board[7][6] and board[7][0] == board[7][7] and board[7][0] == board[7][8] and board[7][0] == board[0][9] and board[7][0] == mark):
        return True
    elif (board[8][0] == board[8][1] and board[8][0] == board[8][2] and board[8][0] == board[8][3] and board[8][0] == board[8][4] and board[8][0] == board[8][5] and board[8][0] == board[8][6] and board[8][0] == board[8][7] and board[8][0] == board[8][8] and board[8][0] == board[0][9] and board[8][0] == mark):
        return True
    elif (board[9][0] == board[9][1] and board[9][0] == board[9][2] and board[9][0] == board[9][3] and board[9][0] == board[9][4] and board[9][0] == board[9][5] and board[9][0] == board[9][6] and board[9][0] == board[9][7] and board[9][0] == board[9][8] and board[9][0] == board[9][9] and board[9][0] == mark):
        return True
    elif (board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] == board[3][0] and board[0][0] == board[4][0] and board[0][0] == board[5][0] and board[0][0] == board[6][0] and board[0][0] == board[7][0] and board[0][0] == board[8][0] and board[0][0] == board[9][0] and board[0][0] == mark):
        return True
    elif (board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] == board[3][1] and board[0][1] == board[4][1] and board[0][1] == board[5][1] and board[0][1] == board[6][1] and board[0][1] == board[7][1] and board[0][1] == board[8][1] and board[0][1] == board[9][1] and board[0][1] == mark):
        return True
    elif (board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] == board[3][2] and board[0][2] == board[4][2] and board[0][2] == board[5][2] and board[0][2] == board[6][2] and board[0][2] == board[7][2] and board[0][2] == board[8][2] and board[0][2] == board[9][2] and board[0][2] == mark):
        return True
    elif (board[0][3] == board[1][3] and board[0][3] == board[2][3] and board[0][3] == board[3][3] and board[0][3] == board[4][3] and board[0][3] == board[5][3] and board[0][3] == board[6][3] and board[0][3] == board[7][3] and board[0][3] == board[8][3] and board[0][3] == board[9][3] and board[0][3] == mark):
        return True
    elif (board[0][4] == board[1][4] and board[0][4] == board[2][4] and board[0][4] == board[3][4] and board[0][4] == board[4][4] and board[0][4] == board[5][4] and board[0][4] == board[6][4] and board[0][4] == board[7][4] and board[0][4] == board[8][4] and board[0][4] == board[9][4] and board[0][4] == mark):
        return True
    elif (board[0][5] == board[1][5] and board[0][5] == board[2][5] and board[0][5] == board[3][5] and board[0][5] == board[4][5] and board[0][5] == board[5][5] and board[0][5] == board[6][5] and board[0][5] == board[7][5] and board[0][5] == board[8][5] and board[0][5] == board[9][5] and board[0][5] == mark):
        return True
    elif (board[0][6] == board[1][6] and board[0][6] == board[2][6] and board[0][6] == board[3][6] and board[0][6] == board[4][6] and board[0][6] == board[5][6] and board[0][6] == board[6][6] and board[0][6] == board[7][6] and board[0][6] == board[8][6] and board[0][6] == board[9][6] and board[0][6] == mark):
        return True
    elif (board[0][7] == board[1][7] and board[0][7] == board[2][7] and board[0][7] == board[3][7] and board[0][7] == board[4][7] and board[0][7] == board[5][7] and board[0][7] == board[6][7] and board[0][7] == board[7][7] and board[0][7] == board[8][7] and board[0][7] == board[9][7] and board[0][7] == mark):
        return True
    elif (board[0][8] == board[1][8] and board[0][8] == board[2][8] and board[0][8] == board[3][8] and board[0][8] == board[4][8] and board[0][8] == board[5][8] and board[0][8] == board[6][8] and board[0][8] == board[7][8] and board[0][8] == board[8][8] and board[0][8] == board[9][8] and board[0][8] == mark):
        return True
    elif (board[0][9] == board[1][9] and board[0][9] == board[2][9] and board[0][9] == board[3][9] and board[0][9] == board[4][9] and board[0][9] == board[5][9] and board[0][9] == board[6][9] and board[0][9] == board[7][9] and board[0][9] == board[9][9] and board[0][9] == board[9][9] and board[0][9] == mark):
        return True
    elif (board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == board[3][3] and board[0][0] == board[4][4] and board[0][0] == board[5][5] and board[0][0] == board[6][6] and board[0][0] == board[7][7] and board[0][0] == board[8][8] and board[0][0] == board[9][9] and board[0][0] == mark):
        return True
    elif (board[9][0] == board[8][1] and board[9][0] == board[7][2] and board[9][0] == board[6][3] and board[9][0] == board[5][4] and board[9][0] == board[4][5] and board[9][0] == board[3][6] and board[9][0] == board[2][7] and board[9][0] == board[1][8] and board[9][0] == board[0][9] and board[9][0] == mark):
        return True
    else:
        return False
    
    
    
def heuristic10(board):
    
    
    #mark is the first player looking to maximize the score
    mark = ' X '
    #Opp is the second player looking to minimize the score
    opp= ' O '
    
    xlines = 0
    olines = 0
    
    #check how many open lines exist for the X player
    if (board[0][0] != opp and board[0][1] != opp and board[0][2] != opp and board[0][3] != opp and board[0][4] != opp and board[0][5] != opp and board[0][6] != opp and board[0][7] != opp and board[0][8] != opp and board[0][9] != opp):
        xlines +=1
    if (board[1][0] != opp and board[1][1] != opp and board[1][2] != opp and board[1][3] != opp and board[1][4] != opp and board[1][5] != opp and board[1][6] != opp and board[1][7] != opp and board[1][8] != opp and board[1][9] != opp):
        xlines +=1
    if (board[2][0] != opp and board[2][1] != opp and board[2][2] != opp and board[2][3] != opp and board[2][4] != opp and board[2][5] != opp and board[2][6] != opp and board[2][7] != opp and board[2][8] != opp and board[2][9] != opp):
        xlines +=1
    if (board[3][0] != opp and board[3][1] != opp and board[3][2] != opp and board[3][3] != opp and board[3][4] != opp and board[3][5] != opp and board[3][6] != opp and board[3][7] != opp and board[3][8] != opp and board[3][9] != opp):
        xlines +=1
    if (board[4][0] != opp and board[4][1] != opp and board[4][2] != opp and board[4][3] != opp and board[4][4] != opp and board[4][5] != opp and board[4][6] != opp and board[4][7] != opp and board[4][8] != opp and board[4][9] != opp):
        xlines +=1
    if (board[5][0] != opp and board[5][1] != opp and board[5][2] != opp and board[5][3] != opp and board[5][4] != opp and board[5][5] != opp and board[5][6] != opp and board[5][7] != opp and board[5][8] != opp and board[5][9] != opp):
        xlines +=1
    if (board[6][0] != opp and board[6][1] != opp and board[6][2] != opp and board[6][3] != opp and board[6][4] != opp and board[6][5] != opp and board[6][6] != opp and board[6][7] != opp and board[6][8] != opp and board[6][9] != opp):
        xlines +=1
    if (board[7][0] != opp and board[7][1] != opp and board[7][2] != opp and board[7][3] != opp and board[7][4] != opp and board[7][5] != opp and board[7][6] != opp and board[7][7] != opp and board[7][8] != opp and board[7][9] != opp):
        xlines +=1  
    if (board[8][0] != opp and board[8][1] != opp and board[8][2] != opp and board[8][3] != opp and board[8][4] != opp and board[8][5] != opp and board[8][6] != opp and board[8][7] != opp and board[8][8] != opp and board[8][9] != opp):
        xlines +=1    
    if (board[9][0] != opp and board[9][1] != opp and board[9][2] != opp and board[9][3] != opp and board[9][4] != opp and board[9][5] != opp and board[9][6] != opp and board[9][7] != opp and board[9][9] != opp and board[9][9] != opp):
        xlines +=1    
    if (board[0][0] != opp and board[1][0] != opp and board[2][0] != opp and board[3][0] != opp and board[4][0] != opp and board[5][0] != opp and board[6][0] != opp and board[7][0] != opp and board[8][0] != opp and board[9][0] != opp):
       xlines +=1
    if (board[0][1] != opp and board[1][1] != opp and board[2][1] != opp and board[3][1] != opp and board[4][1] != opp and board[5][1] != opp and board[6][1] != opp and board[7][1] != opp and board[8][1] != opp and board[9][1] != opp):
        xlines +=1
    if (board[0][2] != opp and board[1][2] != opp and board[2][2] != opp and board[3][2] != opp and board[4][2] != opp and board[5][2] != opp and board[6][2] != opp and board[7][2] != opp and board[8][2] != opp and board[9][2] != opp):
        xlines +=1
    if (board[0][3] != opp and board[1][3] != opp and board[2][3] != opp and board[3][3] != opp and board[4][3] != opp and board[5][3] != opp and board[6][3] != opp and board[7][3] != opp and board[8][3] != opp and board[9][3] != opp):
        xlines +=1
    if (board[0][4] != opp and board[1][4] != opp and board[2][4] != opp and board[3][4] != opp and board[4][4] != opp and board[5][4] != opp and board[6][4] != opp and board[7][4] != opp and board[8][4] != opp and board[9][4] != opp):
        xlines +=1
    if (board[0][5] != opp and board[1][5] != opp and board[2][5] != opp and board[3][5] != opp and board[4][5] != opp and board[5][5] != opp and board[6][5] != opp and board[7][5] != opp and board[8][5] != opp and board[9][5] != opp):
        xlines +=1
    if (board[0][6] != opp and board[1][6] != opp and board[2][6] != opp and board[3][6] != opp and board[4][6] != opp and board[5][6] != opp and board[6][6] != opp and board[7][6] != opp and board[8][6] != opp and board[9][6] != opp):
        xlines +=1   
    if (board[0][7] != opp and board[1][7] != opp and board[2][7] != opp and board[3][7] != opp and board[4][7] != opp and board[5][7] != opp and board[6][7] != opp and board[7][7] != opp and board[8][7] != opp and board[9][7] != opp):
        xlines +=1  
    if (board[0][8] != opp and board[1][8] != opp and board[2][8] != opp and board[3][8] != opp and board[4][8] != opp and board[5][8] != opp and board[6][8] != opp and board[7][8] != opp and board[8][8] != opp and board[9][8] != opp):
        xlines +=1    
    if (board[0][9] != opp and board[1][9] != opp and board[2][9] != opp and board[3][9] != opp and board[4][9] != opp and board[5][9] != opp and board[6][9] != opp and board[7][9] != opp and board[9][9] != opp and board[9][9] != opp):
        xlines +=1     
    if (board[0][0] != opp and board[1][1] != opp and board[2][2] != opp and board[3][3] != opp and board[4][4] != opp and board[5][5] != opp and board[6][6] != opp and board[7][7] != opp and board[8][8] != opp and board[9][9] != opp):
        xlines +=1
    if (board[9][0] != opp and board[8][1] != opp and board[7][2] != opp and board[6][3] != opp and board[5][4] != opp and board[4][5] != opp and board[3][6] != opp and board[2][7] != opp and board[1][8] != opp and board[0][9] != opp):
        xlines +=1
    
    
    #Check open lines for the O player    
    if (board[0][0] != mark and board[0][1] != mark and board[0][2] != mark and board[0][3] != mark and board[0][4] != mark and board[0][5] != mark and board[0][6] != mark and board[0][7] != mark and board[0][8] != mark and board[0][9] != mark):
        olines +=1
    if (board[1][0] != mark and board[1][1] != mark and board[1][2] != mark and board[1][3] != mark and board[1][4] != mark and board[1][5] != mark and board[1][6] != mark and board[1][7] != mark and board[1][8] != mark and board[1][9] != mark):
        olines +=1
    if (board[2][0] != mark and board[2][1] != mark and board[2][2] != mark and board[2][3] != mark and board[2][4] != mark and board[2][5] != mark and board[2][6] != mark and board[2][7] != mark and board[2][8] != mark and board[2][9] != mark):
        olines +=1
    if (board[3][0] != mark and board[3][1] != mark and board[3][2] != mark and board[3][3] != mark and board[3][4] != mark and board[3][5] != mark and board[3][6] != mark and board[3][7] != mark and board[3][8] != mark and board[3][9] != mark):
        olines +=1
    if (board[4][0] != mark and board[4][1] != mark and board[4][2] != mark and board[4][3] != mark and board[4][4] != mark and board[4][5] != mark and board[4][6] != mark and board[4][7] != mark and board[4][8] != mark and board[4][9] != mark):
        olines +=1
    if (board[5][0] != mark and board[5][1] != mark and board[5][2] != mark and board[5][3] != mark and board[5][4] != mark and board[5][5] != mark and board[5][6] != mark and board[5][7] != mark and board[5][8] != mark and board[5][9] != mark):
        olines +=1
    if (board[6][0] != mark and board[6][1] != mark and board[6][2] != mark and board[6][3] != mark and board[6][4] != mark and board[6][5] != mark and board[6][6] != mark and board[6][7] != mark and board[6][8] != mark and board[6][9] != mark):
        olines +=1
    if (board[7][0] != mark and board[7][1] != mark and board[7][2] != mark and board[7][3] != mark and board[7][4] != mark and board[7][5] != mark and board[7][6] != mark and board[7][7] != mark and board[7][8] != mark and board[7][9] != mark):
        olines +=1  
    if (board[8][0] != mark and board[8][1] != mark and board[8][2] != mark and board[8][3] != mark and board[8][4] != mark and board[8][5] != mark and board[8][6] != mark and board[8][7] != mark and board[8][8] != mark and board[8][9] != mark):
        olines +=1    
    if (board[9][0] != mark and board[9][1] != mark and board[9][2] != mark and board[9][3] != mark and board[9][4] != mark and board[9][5] != mark and board[9][6] != mark and board[9][7] != mark and board[9][9] != mark and board[9][9] != mark):
        olines +=1    
    if (board[0][0] != mark and board[1][0] != mark and board[2][0] != mark and board[3][0] != mark and board[4][0] != mark and board[5][0] != mark and board[6][0] != mark and board[7][0] != mark and board[8][0] != mark and board[9][0] != mark):
       olines +=1
    if (board[0][1] != mark and board[1][1] != mark and board[2][1] != mark and board[3][1] != mark and board[4][1] != mark and board[5][1] != mark and board[6][1] != mark and board[7][1] != mark and board[8][1] != mark and board[9][1] != mark):
        olines +=1
    if (board[0][2] != mark and board[1][2] != mark and board[2][2] != mark and board[3][2] != mark and board[4][2] != mark and board[5][2] != mark and board[6][2] != mark and board[7][2] != mark and board[8][2] != mark and board[9][2] != mark):
        olines +=1
    if (board[0][3] != mark and board[1][3] != mark and board[2][3] != mark and board[3][3] != mark and board[4][3] != mark and board[5][3] != mark and board[6][3] != mark and board[7][3] != mark and board[8][3] != mark and board[9][3] != mark):
        olines +=1
    if (board[0][4] != mark and board[1][4] != mark and board[2][4] != mark and board[3][4] != mark and board[4][4] != mark and board[5][4] != mark and board[6][4] != mark and board[7][4] != mark and board[8][4] != mark and board[9][4] != mark):
        olines +=1
    if (board[0][5] != mark and board[1][5] != mark and board[2][5] != mark and board[3][5] != mark and board[4][5] != mark and board[5][5] != mark and board[6][5] != mark and board[7][5] != mark and board[8][5] != mark and board[9][5] != mark):
        olines +=1
    if (board[0][6] != mark and board[1][6] != mark and board[2][6] != mark and board[3][6] != mark and board[4][6] != mark and board[5][6] != mark and board[6][6] != mark and board[7][6] != mark and board[8][6] != mark and board[9][6] != mark):
        olines +=1   
    if (board[0][7] != mark and board[1][7] != mark and board[2][7] != mark and board[3][7] != mark and board[4][7] != mark and board[5][7] != mark and board[6][7] != mark and board[7][7] != mark and board[8][7] != mark and board[9][7] != mark):
        olines +=1  
    if (board[0][8] != mark and board[1][8] != mark and board[2][8] != mark and board[3][8] != mark and board[4][8] != mark and board[5][8] != mark and board[6][8] != mark and board[7][8] != mark and board[8][8] != mark and board[9][8] != mark):
        olines +=1    
    if (board[0][9] != mark and board[1][9] != mark and board[2][9] != mark and board[3][9] != mark and board[4][9] != mark and board[5][9] != mark and board[6][9] != mark and board[7][9] != mark and board[9][9] != mark and board[9][9] != mark):
        olines +=1     
    if (board[0][0] != mark and board[1][1] != mark and board[2][2] != mark and board[3][3] != mark and board[4][4] != mark and board[5][5] != mark and board[6][6] != mark and board[7][7] != mark and board[8][8] != mark and board[9][9] != mark):
        olines +=1
    if (board[9][0] != mark and board[8][1] != mark and board[7][2] != mark and board[6][3] != mark and board[5][4] != mark and board[4][5] != mark and board[3][6] != mark and board[2][7] != mark and board[1][8] != mark and board[0][9] != mark):
        olines +=1
    
           
    heuristic = xlines - olines
    
    return heuristic










