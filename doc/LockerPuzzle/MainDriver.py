from LockerPuzzle import LockerSolver

def Main():
    lockerSolver = LockerSolver(100)
    lockerSolver.RunPuzzle()
    openLocker = lockerSolver.GetOpenLockers()

    print("Open lockers are: ")
    print(", ".join(map(str, openLocker)))

Main()