import random

class LargestRowAndColumn:
    GRID_SIZE = 4

    def __init__(self):
        self.grid = [[random.randint(0,1) for _ in range(self.GRID_SIZE)] for _ in range(self.GRID_SIZE)]

    def GetGrid(self):
        return self.grid

    def RowWithMostOnes(self):
        retIdx = 0
        mostRow = 0
        for row in range(self.GRID_SIZE):
            rowCnt = sum(self.grid[row])
            if rowCnt > mostRow:
                mostRow = rowCnt 
                retIndx = row
        return mostRow

    def ColumnWithMostOnes(self):
        retIdx = 0
        mostColumn = 0
        for column in range(self.GRID_SIZE):
            colCnt = sum(self.grid[row][column] for row in range(self.GRID_SIZE))
            if (colCnt > mostColumn):
                mostColumn = colCnt
                retIdx = column
        return mostColumn
