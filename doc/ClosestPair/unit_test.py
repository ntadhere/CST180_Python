import unittest
from ClosestPair import ClosestPair

class TestClosestPair(unittest.TestCase):
    def test_FindClosestPair(self):
        points = [
            (-1, 3),
            (-1, -1),
            (1, 1),
            (2, 0.5),
            (2, -1),
            (3, 3),
            (4, 2),
            (4, -0.5)
        ]

        retList = ClosestPair.FindClosestPair(points)
        expected = [(1, 1), (2, 0.5)]
        self.assertEqual(retList, expected)