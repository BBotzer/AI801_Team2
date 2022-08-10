# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 07:01:12 2022

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
from fastWinConMark import *
from winConditionsMarks import *
from displayBoard import *
import copy
import site
import time
import random



def humanMove(board, player, ntWin):
    
    #Human Move
    
    
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
        
    return




def randomMove(gboard, letter, ntWin):
    
    flag = False
    
    endRange = len(gboard) - 1
    
    
    while flag == False:
        
        x = random.randint(0, endRange)
        y = random.randint(0, endRange)
        
        if spaceIsFree(gboard, x, y) == True:
            
            #Check to see if game ended
            if letter == ' X ':
                check = ' O '
            else:
                check = ' X '
            
            #Check to see if the game ended for different board lengths so you don't make an extra move:
             
            if len(gboard) == 3:
                if fastWinCon3Mark(gboard, check):
                    showGrid(gboard)
                    return False
                
                if drawCondition(gboard):
                    showGrid(gboard)
                    print("this is a draw and I don't want to play")
                    return False
                
            elif len(gboard) == 5:    
                if fastWinCon5Mark(gboard, check):
                    showGrid(gboard)
                    return False
                if drawCondition(gboard):
                    showGrid(gboard)
                    print("this is a draw and I don't want to play")
                    return False
                
            elif len(gboard) == 6:
                if fastWinCon6Mark(gboard, check):
                    showGrid(gboard)
                    return False
                if drawCondition(gboard):
                    showGrid(gboard)
                    print("this is a draw and I don't want to play")
                    return False
                
            elif len(gboard) == 7:
                if fastWinCon7Mark(gboard, check):
                    showGrid(gboard)
                    return False
                if drawCondition(gboard):
                    showGrid(gboard)
                    print("this is a draw and I don't want to play")
                    return False  
            
            elif len(gboard) == 8:
                if fastWinCon8Mark(gboard, check):
                    showGrid(gboard)
                    return False
                if drawCondition(gboard):
                    showGrid(gboard)
                    print("this is a draw and I don't want to play")
                    return False
        
            elif len(gboard) == 9:
                if fastWinCon9Mark(gboard, check):
                    showGrid(gboard)
                    return False
                if drawCondition(gboard):
                    showGrid(gboard)
                    print("this is a draw and I don't want to play")
                    return False
                
            elif len(gboard) == 10:
                if fastWinCon10Mark(gboard, check):
                    showGrid(gboard)
                    return False
                if drawCondition(gboard):
                    showGrid(gboard)
                    print("this is a draw and I don't want to play")
                    return False
        
            #used to update the board
            gboard[x][y] =  letter 
        
            
            #return used to create the board
            return gboard
        else:
            return
            
            
            


def makeMove(letter, xloc, yloc, gboard, ntWin):
    #take the move letter, the x and y location, and the current board state
   
    #get x, y location
    x, y = (xloc,yloc)
    
    if spaceIsFree(gboard,x,y) == False:
        #print("That space is taken.  Try again.\n")
        return False
    else:
        
    
        #Check to see if game ended
        if letter == ' X ':
            check = ' O '
        else:
            check = ' X '
        
        #Check to see if the game ended for different board lengths so you don't make an extra move:
         
        if len(gboard) == 3:
            if fastWinCon3Mark(gboard, check):
                showGrid(gboard)
                return False
            
            if drawCondition(gboard):
                showGrid(gboard)
                print("this is a draw and I don't want to play")
                return False
            
        elif len(gboard) == 5:    
            if fastWinCon5Mark(gboard, check):
                showGrid(gboard)
                return False
            if drawCondition(gboard):
                showGrid(gboard)
                print("this is a draw and I don't want to play")
                return False
            
        elif len(gboard) == 6:
            if fastWinCon6Mark(gboard, check):
                showGrid(gboard)
                return False
            if drawCondition(gboard):
                showGrid(gboard)
                print("this is a draw and I don't want to play")
                return False
            
        elif len(gboard) == 7:
            if fastWinCon7Mark(gboard, check):
                showGrid(gboard)
                return False
            if drawCondition(gboard):
                showGrid(gboard)
                print("this is a draw and I don't want to play")
                return False  
        
        elif len(gboard) == 8:
            if fastWinCon8Mark(gboard, check):
                showGrid(gboard)
                return False
            if drawCondition(gboard):
                showGrid(gboard)
                print("this is a draw and I don't want to play")
                return False
    
        elif len(gboard) == 9:
            if fastWinCon9Mark(gboard, check):
                showGrid(gboard)
                return False
            if drawCondition(gboard):
                showGrid(gboard)
                print("this is a draw and I don't want to play")
                return False
            
        elif len(gboard) == 10:
            if fastWinCon10Mark(gboard, check):
                showGrid(gboard)
                return False
            if drawCondition(gboard):
                showGrid(gboard)
                print("this is a draw and I don't want to play")
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
    
    start = time.perf_counter()
    
    player = player
    bot = bot
    bestMax = -1000
    minimax.counter = 0

    
    xloc = 0
    yloc = 0

    start = time.perf_counter()

    #Look for forced moves.  If one is made, return without running miniMax
    if playerForcedMoves(board, player, bot, ntWin) == True:
        return


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
    end = time.perf_counter()
    showGrid(board)
    print("Calls to miniMax: " + str(minimax.counter))
    minimax.totalcalls += minimax.counter
    print("runtime: " + str(end - start))

    return 


def compMove(board, player, bot, ntWin):
    
    
    
    player = player
    bot = bot
    bestMin = 1000
    minimax.counter = 0


    xloc = 0
    yloc = 0
    
    start = time.perf_counter()
    
    #Look for forced moves.  If one is made, return without running miniMax
    if compForcedMoves(board, player, bot, ntWin) == True:
       return

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
    end = time.perf_counter()
    showGrid(board)
    print("Calls to miniMax: " + str(minimax.counter))
    minimax.totalcalls += minimax.counter
    print("runtime: " + str(end - start))

    return 

#Junk test minimax (delete)
def minimaxz(board, depth, isMaximizing, player, bot, ntWin):
    return 1


def callCount():
    
    count = count + 1
    





def minimax(board, depth, isMaximizing, player, bot, ntWin, alpha, beta):
    
    minimax.counter += 1

    depthlimit = 2
    
    #Check which size board you have to choose the right win and heuristic calls len(board)
    if len(board) == 3:
        if fastWinCon3Mark(board, player):
            #Faster win conditions (lower depth) are better to play
            return ((len(board)**2) - depth)
        elif fastWinCon3Mark(board, bot):
            return (depth - (len(board)**2))
        elif drawCondition(board):
            return 0    
        else:
            if depth > depthlimit:
                return heuristic3(board)
    elif len(board) == 5:
        if fastWinCon5Mark(board, player):
            #Faster win conditions (lower depth) are better to play
            return ((len(board)**2) - depth)
        elif fastWinCon5Mark(board, bot):
            return (depth - (len(board)**2))
        elif drawCondition(board):
            return 0    
        else:
            if depth > depthlimit:
                return heuristic5(board)
    elif len(board) == 6:
        if fastWinCon6Mark(board, player):
            #Faster win conditions (lower depth) are better to play
            return ((len(board)**2) - depth)
        elif fastWinCon6Mark(board, bot):
            return (depth - (len(board)**2))
        elif drawCondition(board):
            return 0    
        else:
            if depth > depthlimit:
                return heuristic6(board)
    elif len(board) == 7:
        if fastWinCon7Mark(board, player):
            #Faster win conditions (lower depth) are better to play
            return ((len(board)**2) - depth)
        elif fastWinCon7Mark(board, bot):
            return (depth - (len(board)**2))
        elif drawCondition(board):
            return 0    
        else:
            if depth > depthlimit:
                return heuristic7(board)
    elif len(board) == 8:
        if fastWinCon8Mark(board, player):
            #Faster win conditions (lower depth) are better to play
            return ((len(board)**2) - depth)
        elif fastWinCon8Mark(board, bot):
            return (depth - (len(board)**2))
        elif drawCondition(board):
            return 0    
        else:
            if depth > depthlimit:
                return heuristic8(board)
    elif len(board) == 9:
        if fastWinCon9Mark(board, player):
            #Faster win conditions (lower depth) are better to play
            return ((len(board)**2) - depth)
        elif fastWinCon9Mark(board, bot):
            return (depth - (len(board)**2))
        elif drawCondition(board):
            return 0    
        else:
            if depth > depthlimit:
                return heuristic9(board)
    elif len(board) == 10:
        if fastWinCon10Mark(board, player):
            #Faster win conditions (lower depth) are better to play
            return ((len(board)**2) - depth)
        elif fastWinCon10Mark(board, bot):
            return (depth - (len(board)**2))
        elif drawCondition(board):
            return 0    
        else:
            if depth > depthlimit:
                return heuristic10(board)


    #Run the miniMax to obtain best move
    if isMaximizing:
        bestMax = -1000

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

minimax.totalcalls = 0