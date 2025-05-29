import unittest
from Concentration import Concentration

class TestConcentration(unittest.TestCase):
    def test_concentrationInit(self):
        game = Concentration()
        self.assertEqual(game.board[0],10)
        self.assertEqual(game.board[1],20)
        self.assertEqual(game.board[2],30)
        self.assertEqual(game.board[3],40)
        self.assertEqual(game.board[4],50)
        self.assertEqual(game.board[5],60)
        self.assertEqual(game.board[6],10)
        self.assertEqual(game.board[7],20)
        self.assertEqual(game.board[8],30)
        self.assertEqual(game.board[9],40)
        self.assertEqual(game.board[10],50)
        self.assertEqual(game.board[11],60)

        self.assertFalse(game.CorrectMatch(0,5))
        self.assertTrue(game.CorrectMatch(0,6))

        self.assertFalse(game.GameOver())

        self.assertTrue(game.CorrectMatch(1,7))
        self.assertTrue(game.CorrectMatch(2,8))
        self.assertTrue(game.CorrectMatch(3,9))
        self.assertTrue(game.CorrectMatch(4,10))
        self.assertTrue(game.CorrectMatch(5,11))

        self.assertTrue(game.GameOver())
