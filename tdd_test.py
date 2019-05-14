
import unittest
from tdd import cal

class TestStringMethods(unittest.TestCase):
    def test_cal(self):
        self.assertEqual(3, cal(1,2))

if __name__ == '__main__':
    unittest.main()
