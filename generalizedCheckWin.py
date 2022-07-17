
#checks wins based on players needing to completely fill the row, column or diagonal
#if the board is 3x3 it checks for 3 in a row; if 5x5 it checks for 5 in a row
#if we want to use different win requirements for different sized boards we will need different check win functions 
# to change the math while using the len(board) function
def checkWin(board):

    #check rows
    for row in range(len(board)):
        for col in range(len(board) -1):
            if board[row][col] == "_" or board[row][col+1] == "_" or board[row][col] != board[row][col+1]:
                break
            else:
                return True
        
        #check columns
        for col in range(len(board)):
            for row in range(len(board) -1):
                if board[row][col] == "_" or board[row+1][col] == "_" or board[row][col] != board[row+1][col]:
                    break
            else: 
                return True

        #check left diagonal
        for cell in range(len(board)-1):
            if board[cell][cell] == "_" or board[cell+1][cell+1] == "_" or board[cell][cell] != board[cell+1][cell+1]:
                break
            else:
                return True
        #check right diagonal
        for cell in range(len(board)-1):
            emptyCell = board[cell][len(board)-cell-1] == "_" or board[cell+1][len(board)-cell-2] == "_"
            different  = board[cell][len(board)-cell-1] != board[cell+1][len(board)-cell-2]
            if emptyCell or different:
                break
        else:
            return True
        
        #no win
        return False
