from CellStates import CellStates
from Cell import Cell
from WinStatus import WinStatus

class TicTacToe:
    BOARD_SIZE = 3

    def __init__(self):
        self.board = [[Cell() for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]

    def SetCellState(self, row, column, cellState):
        if self.board[row][column].state != CellStates.OPEN:
            return False
        
        self.board[row][column].state = cellState
        return True
    
    def GetWinStatus(self):
        for row in range(self.BOARD_SIZE):
            if ((self.board[row][0].state == self.board[row][1].state == self.board[row][2].state) and 
                (self.board[row][0].state != CellStates.OPEN)):
                return self.ConvertCellStateToWinState(self.board[row][0].state)
            
        for col in range(self.BOARD_SIZE):
            if ((self.board[0][col].state == self.board[1][col].state == self.board[2][col].state) and 
                (self.board[0][col].state != CellStates.OPEN)):
                return self.ConvertCellStateToWinState(self.board[0][col].state)
            
        if ((self.board[0][0].state == self.board[1][1].state == self.board[2][2].state) and 
            (self.board[0][0].state != CellStates.OPEN)):
            return self.ConvertCellStateToWinState(self.board[0][0].state)
        
        if ((self.board[0][2].state == self.board[1][1].state == self.board[2][0].state) and 
            (self.board[0][0].state != CellStates.OPEN)):
            return self.ConvertCellStateToWinState(self.board[0][2].state)\
            
        return WinStatus.NO_Winner
    
    def OpenCells(self):
        return sum(1 for row in self.board for cell in row if cell.state == CellStates.OPEN)

    @staticmethod
    def ConvertCellStateToWinState (cellState):
        if cellState == CellStates.PLAYER1:
            return WinStatus.PLAYER1
        elif cellState == CellStates.PLAYER2:
            return WinStatus.PLAYER2
        elif cellState == CellStates.COMPUTER:
            return WinStatus.COMPUTER
        return WinStatus.NO_Winner

     