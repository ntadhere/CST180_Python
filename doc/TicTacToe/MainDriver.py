from CellStates import CellStates
from Cell import Cell
from WinStatus import WinStatus
from TicTacToe import TicTacToe
from AIPlayer import AIPlayer

def Main():
    gameBoard = TicTacToe()
    isPlayer1 = False
    
    while (gameBoard.GetWinStatus() == WinStatus.NO_Winner and 
            gameBoard.OpenCells() > 0):
        DisplayBoard(gameBoard)

        cellState = CellStates.PLAYER1 if isPlayer1 else CellStates.PLAYER2
        if isPlayer1:
            row,col = GetUserInput("Player 1")
        else:
            aiCell = AIPlayer.GetAIPlacement(gameBoard.board)
            # row,col = GetUserInput("Player 2")
            row, col = aiCell.row, aiCell.col

        if gameBoard.SetCellState(row, col, cellState):
            isPlayer1 = not isPlayer1
        else:
            print("That cell is already taken.")



def DisplayBoard(tttObj):
    board = tttObj.board
    print("   0   1   2   ")
    print("  +---+---+---+")
    for row in range(TicTacToe.BOARD_SIZE):
        print(f"{row} |", end=" ")
        for col in range(TicTacToe.BOARD_SIZE):
            print(f"{GetCellOutput(board[row][col])} |", end=" ")
        print(f"\n  +---+---+---+")

def GetCellOutput(cell):
    return {CellStates.PLAYER1:  "X",
            CellStates.PLAYER2:  "O",
            CellStates.COMPUTER:  "O",
            CellStates.OPEN: " "
    }.get(cell.state, "?")  # Use .state here since cell is a Cell  


def GetUserInput(playerStr):
    while True:
        try:
            row = int(input(f"{playerStr}, enter row (0-2): "))
            col = int(input(f"{playerStr}, enter col (0-2): "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            print("Invalid input: Enter numbers between 0 and 2.")
        
        except:
            print("Invalid input. Please enter a number")
            
Main()