class TruthTables:
    def __init__(self):
        self.MaxTruthTable = 2

    def CreateAndTable(self):
        table = [[False for _ in range(self.MaxTruthTable)] for _ in range(self.MaxTruthTable)] 
        for row in range(self.MaxTruthTable):
            for col in range(self.MaxTruthTable):
                rowFlag = row == 1
                colFlag = col == 1
                table[row][col] = rowFlag and colFlag
        return table

    def CreateOrTable(self):
        table = [[False for _ in range(self.MaxTruthTable)] for _ in range(self.MaxTruthTable)] 
        for row in range(self.MaxTruthTable):
            for col in range(self.MaxTruthTable):
                rowFlag = row == 1
                colFlag = col == 1
                table[row][col] = rowFlag or colFlag
        return table

    def CreateXorTable(self):
        table = [[False for _ in range(self.MaxTruthTable)] for _ in range(self.MaxTruthTable)] 
        for row in range(self.MaxTruthTable):
            for col in range(self.MaxTruthTable):
                rowFlag = row == 1
                colFlag = col == 1
                table[row][col] = rowFlag != colFlag  # XOR
        return table

    @staticmethod
    def BooltoString(flag):
        return "True" if flag else "False"
