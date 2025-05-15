class LockerSolver:
    def __init__(self, numLockers:int):
        self.numLockers = numLockers
        self.lockerStatus = [False] + self.numLockers

    def GetNumberOfLocker(self):
        return self.numLockers
    
    def InitLockers(self):
        self.lockerStatus = [False] * self.numLockers

    def RunPuzzle(self):
        for cnt in range(1, self.numLockers + 1):
            self.StudentLockerChange[cnt]

    def GetOpenLockers(self):
        return [i + 1 for i in range(self.numLockers) if self.lockerStatus[i]]
    
    def StudentLockerChange(self, studentNum: int):
        lockerNum = studentNum - 1 
        while lockerNum < self.numLockers:
            self.LockerStatus[lockerNum] = not self.lockerStatus[lockerNum]
            lockerNum += studentNum