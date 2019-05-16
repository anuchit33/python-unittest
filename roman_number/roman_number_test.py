
import unittest
from roman_number import RomanNumber

class TestRomanNumber(unittest.TestCase):
    def test_over_1000(self):
        self.assertEqual("Input Error!", RomanNumber(1001))
    
    def test_less_1(self):
        self.assertEqual("Input Error!", RomanNumber(0))

    # base
    def test_M_1000(self):
        self.assertEqual("M", RomanNumber(1000))
    def test_D_500(self):
        self.assertEqual("D", RomanNumber(500))
    def test_C_100(self):
        self.assertEqual("C", RomanNumber(100))
    def test_L_50(self):
        self.assertEqual("L", RomanNumber(50))
    def test_X_10(self):
        self.assertEqual("X", RomanNumber(10))
    def test_V_5(self):
        self.assertEqual("V", RomanNumber(5))
    def test_I_1(self):
        self.assertEqual("I", RomanNumber(1))

    # added
    def test_I_added_II(self):
        self.assertEqual("III", RomanNumber(3))

    def test_X_added_XX(self):
        self.assertEqual("XXX", RomanNumber(30))
    
    def test_C_added_CC(self):
        self.assertEqual("CCC", RomanNumber(300))
    
    def test_V_added_I(self):
        self.assertEqual("VI", RomanNumber(6))

    def test_X_added_I(self):
        self.assertEqual("XI", RomanNumber(11))

    def test_X_added_I(self):
        self.assertEqual("XI", RomanNumber(11))

    def test_X_added_XXVIII(self):
        self.assertEqual("XXXVIII", RomanNumber(38))
    
    def test_L_added_I(self):
        self.assertEqual("LI", RomanNumber(51))
    
    def test_L_added_III(self):
        self.assertEqual("LIII", RomanNumber(53))
    
    def test_L_added_XXXIX(self):
        self.assertEqual("LXXXIX", RomanNumber(89))
    
    def test_L_added_XXXIX(self):
        self.assertEqual("LXXXIX", RomanNumber(89))

    #subtracted
    def test_V_subtracted_I(self):
        self.assertEqual("IV", RomanNumber(4))

    def test_X_subtracted_I(self):
        self.assertEqual("IX", RomanNumber(9))

    def test_L_subtracted_X(self):
        self.assertEqual("XL", RomanNumber(40))
    
    def test_L_subtracted_XLIX(self):
        self.assertEqual("XLIX", RomanNumber(49))

    def test_C_subtracted_X(self):
        self.assertEqual("XC", RomanNumber(90))
    def test_C_subtracted_CIX(self):
        self.assertEqual("XCIX", RomanNumber(99))
    
    def test_D_subtracted_C(self):
        self.assertEqual("CD", RomanNumber(400))
    def test_D_subtracted_C(self):
        self.assertEqual("CDXCIX", RomanNumber(499))

    def test_M_subtracted_C(self):
        self.assertEqual("CM", RomanNumber(900))

    def test_M_subtracted_CMXCIX(self):
        self.assertEqual("CMXCIX", RomanNumber(999))
        

if __name__ == '__main__':
    unittest.main()
