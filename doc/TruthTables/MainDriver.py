from TruthTables import TruthTables

def Main():
    truthTables = TruthTables()
    
    andTruthTable = truthTables.CreateAndTable()
    orTruthTable = truthTables.CreateOrTable()
    xorTruthTable = truthTables.CreateXorTable()
    
    PrintTruthTable("AND", andTruthTable)
    PrintTruthTable("OR", orTruthTable)
    PrintTruthTable("XOR", xorTruthTable)

def PrintTruthTable(operation, table):
    print(f"{operation} Table:")
    print(f"      | {'False':<5} | {'True':<5} |")
    print("------------------------")
    for row in range(2):
        rowFlag = row == 1
        print(f"{TruthTables.BooltoString(rowFlag):<5} |", end=" ")
        for col in range(len(table[0])):
            print(f"{TruthTables.BooltoString(table[row][col]):<5} |", end=" ")
        print("\n------------------------")
    print()

Main()
