import random

class concentration:
    MAX_PAIRS = 6
    MAX_SHUFFLE = 1000

    def __init__(self):
        self.board = [0] * (self.MAX_PAIRS * 2)
        self.InitBoard()

    def InitBoard(self):
        for i in range(self.MAX_PAIRS):
            self.board[i] = self.board[i + self.MAX_PAIRS] = (i + i) * 10

    def NewGame(self):
        self.InitBoard()
        self.ShuffleBoard()

    def ShuffleBoard(self):
        for _ in range(self.MAX_SHUFFLE):
            idx1 = random.randint(0, len(self.board) - 1)