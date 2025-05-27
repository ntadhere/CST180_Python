from FileStats import FileStats

def Main():
    fileStats = FileStats("FileIO\\InputData.txt")
    fileStats.GetFileStats()

    msg = f"Nunber of words: {fileStats.GetWordCount()}, Number of lines: {fileStats.GetLineCount()}"

    print(msg)

    with open("FileIO\\OutputData.txt", 'w') as file:
        file.write(f"{msg}\n")
Main()