import unittest
from LockerPuzzle import LockerSolver
# Class name often is lower case

class TestLockerSolver(unittest.TestCase):
    def test_LockerSolver(self):
        lockerSolver = LockerSolver(5)
        lockerSolver.RunPuzzle()
        openLockers = lockerSolver.GetOpenLockers()
        self.assertEqual(openLockers, [1, 4])