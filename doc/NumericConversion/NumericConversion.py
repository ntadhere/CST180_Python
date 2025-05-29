class NumericConversion:
    def NumericStrToInt(self, numStr: str) -> int:
        total = 0
        position = 1
        for ch in reversed(numStr):
            total += (ord(ch) - ord('0')) * self.Power(10, position - 1)
            position += 1

        return total
    
    def BinaryStrToInt(self, numStr: str) -> int:
        total = 0
        position = 1
        for ch in reversed(numStr):
            total += (ord(ch) - ord('0')) * self.Power(2, position - 1)
            position += 1

        return total
    
    def HexStrToInt(self, hexStr:str) -> int:
        total = 0
        position = 1
        for ch in reversed(hexStr.upper()):
            if '0' <= ch <= '9':
                value = ord(ch) - ord('0')
            else:
                value = ord(ch) - ord('A') + 10

            total += value * self.Power(16, position -1)
            position += 1

        return total
    
    def Power(self, base: int, exponent:int) -> int:
        total = 1
        for _ in range(exponent):
            total *= base

        return total