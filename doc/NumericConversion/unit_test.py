import unittest
from NumericConversion import NumericConversion

class TestNumericConversions(unittest.TestCase):
    def setUp(self):
        self.converter = NumericConversion()

    def test_NumericStrToInt(self):
        self.assertEqual(self.converter.NumericStrToInt("21"),21)
        self.assertEqual(self.converter.NumericStrToInt("156"),156)
    def test_BinaryStrToInt(self):
        self.assertEqual(self.converter.BinaryStrToInt("10110"),22)
        self.assertEqual(self.converter.BinaryStrToInt("0110101"),53)
    def test_HexStrToInt(self):
        self.assertEqual(self.converter.HexStrToInt("1A"),26)
        self.assertEqual(self.converter.HexStrToInt("1d3F"),7487)