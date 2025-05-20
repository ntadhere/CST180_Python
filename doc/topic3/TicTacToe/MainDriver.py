from CellStates import CellStates
from Cell import Cell
from WinStatus import WinStatus
from TicTacToe import TicTacToe

def Main():
    gameBoard = TicTacToe()
    isPlayer1 = False
    
    while (gameBoard.GetWinStatus() == WinStatus.NO_Winner and 
            gameBoard.OpenCell() > 0):
        DisplayBoard(gameBoard)

def DisplayBoard(tttObj):
    board = tttObj.board
    print("   0   1   2   ")
    print("  +---+---+---+")
    for row in range(TicTacToe.BOARD_SIZE):
        print(f"   (row) | ", end=" ")
        for col in range(TicTacToe.BOARD_SIZE):
            print(f"{GetCellOutput(board[row][col])}  |  ", end=" ")
        print(f"\n   +---+---+---+")

def GetCellOutput(cell):
    return {CellStates.PLAYER1:  "X",
            CellStates.PLAYER2:  "O",
            CellStates.COMPUTER:  "O"
        }.get(cell.state)
    
Main()