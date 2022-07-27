# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 06:53:44 2022

@author: btb51
"""

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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    