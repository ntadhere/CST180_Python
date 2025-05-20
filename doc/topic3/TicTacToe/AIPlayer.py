import math
from TicTacToe import TicTacToe
from CellStates import CellStates
from Cell import Cell
from AICell import AICell

class AIPlayer:
    WIN_SCORE = 100
    LOSE_SCORE = -100
    DRAW_SCORE = 0

    @staticmethod
    def GetAIPlacement(board):
        bestScore = -math.inf
        bestRow, bestCol = -1,-1

        for row in range(TicTacToe.BOARD_SIZE):
            for col in range(TicTacToe.BOARD_SIZE):
                if board[row][col].state == CellStates.OPEN:
                    board[row][col].state = CellStates.COMPUTER
                    score = AIPlayer.Minimax(board, 0, False)
                    board[row][col].state = CellStates.OPEN

                    if score > bestScore:
                        bestScore = score
                        bestRow, bestCol = row, col
        return AICell(bestRow, bestCol)
    
    @staticmethod
    def Minimax(board, depth, isMaximizing):
        if AIPlayer.IsWinning(board, CellStates.COMPUTER):
            return AIPlayer.WIN_SCORE - depth
        if AIPlayer.IsWinning(board, CellStates.PLAYER1):
            return AIPlayer.LOSE_SCORE + depth
        if sum(1 for row in board for cell in row if cell.state == CellStates.OPEN):
            return AIPlayer.DRAW_SCORE
        if isMaximizing:
            bestScore = math.inf
            for row in range(TicTacToe.BOARD_SIZE):
                for col in range(TicTacToe.BOARD_SIZE):
                    if board[row][col].state == CellStates.OPEN:
                        board[row][col].state = CellStates.COMPUTER
                        score = AIPlayer.Minimax(board, depth + 1 , False)
                        board[row][col].state = CellStates.OPEN
                        bestScore = max(bestScore, score)
            return bestScore
        else:
            bestScore = math. inf
            for row in range(TicTacToe.BOARD_SIZE):
                for col in range(TicTacToe.BOARD_SIZE):
                    if board[row][col].state == CellStates.OPEN:
                        board[row][col].state = CellStates.PLAYER1
                        score = AIPlayer.Minimax(board, depth + 1, True)
                        board[row][col].state = CellStates.OPEN
                        bestScore = min(bestScore, score)
            return bestScore
        
    @staticmethod
    def IsWinning(board, player):
        for row in range(TicTacToe.BOARD_SIZE):
            if all(board[row][col].state == player for col in range(TicTacToe.BOARD_SIZE)):
                return True
        for col in range(TicTacToe.BOARD_SIZE):
            if all(board[row][col].state == player for row in range(TicTacToe.BOARD_SIZE)):
                return True
            
        if all(board[i][i].state == player for i in range(TicTacToe.BOARD_SIZE)):
            return True
        
        if all(board[i][TicTacToe.BOARD_SIZE - 1 - i].state == player for i in range(TicTacToe.BOARD_SIZE)):
            return True
        
        return False