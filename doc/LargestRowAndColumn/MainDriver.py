from LargestRowAndColumn import LargestRowAndColumn

def Main():
    runner = LargestRowAndColumn()
    grid = runner.GetGrid()
    print("The grid looks like: ")
    for row in grid:
        print("    ".join(map(str, row)))
    print()

    print(f"Row with most ones has a index of: {runner.RowWithMostOnes()}")
    print(f"Column with most ones has an index of: {runner.ColumnWithMostOnes()}")

Main()