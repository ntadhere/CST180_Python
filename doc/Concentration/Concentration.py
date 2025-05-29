import random

class Concentration:
    MAX_PAIRS = 6
    MAX_SHUFFLE = 1000

    def __init__(self):
        self.board = [0] * (self.MAX_PAIRS * 2)
        self.InitBoard()

    def InitBoard(self):
        for i in range(self.MAX_PAIRS):
            # give each pair a unique value, e.g. 0, 10, 20, …
            self.board[i] = self.board[i + self.MAX_PAIRS] = i * 10

    def NewGame(self):
        self.InitBoard()
        self.ShuffleBoard()

    def ShuffleBoard(self):
        for _ in range(self.MAX_SHUFFLE):
            idx1 = random.randint(0, len(self.board) - 1)
            idx2 = random.randint(0, len(self.board) - 1)
            # **swap** the two cards
            self.board[idx1], self.board[idx2] = self.board[idx2], self.board[idx1]

    def GameOver(self):
        return all(value == 0 for value in self.board)
    
    def CorrectMatch(self, index1, index2):
        if not self.IndexInRange(index1) or not self.IndexInRange(index2):
            return False
        if self.board[index1] != self.board[index2]:
            return False
        self.board[index1] = self.board[index2] = 0 
        return True

    def IndexInRange(self, index):
        return 0 <= index < len(self.board)
