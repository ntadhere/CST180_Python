class FileStats:
    def __init__(self, fileName: str):
        self.fileName = fileName
        self.wordCount = 0
        self.lineCount =0

    def GetWordCount(self) -> int:
        return self.wordCount


    def GetLineCount(self) -> int:
        return self.lineCount
    
    def GetFileStats(self):
        try:
            with open(self.fileName, 'r') as file:
                for line in file:
                    if len(line.strip()) == 0:
                        self.lineCount += 1
                        continue
                    
                    self.wordCount += len(line.split())
                    self.lineCount += 1
        except FileNotFoundError:
            print(f"File {self.fileName} not found.")