
import unittest
from fuzzbuzz import Fuzzbuzz

class TestFuzzbuzz(unittest.TestCase):
    def test_not_number(self):
        self.assertEqual("Input Error!", Fuzzbuzz("str"))
    def test_input_0(self):
        self.assertEqual("Input Error!", Fuzzbuzz(0))
    def test_input_min_0(self):
        self.assertEqual("Input Error!", Fuzzbuzz(-1))
    def test_input_1_return_1(self):
        self.assertEqual("1", Fuzzbuzz(1))
    def test_input_3_return_12fuzz(self):
        self.assertEqual("1,2,fuzz", Fuzzbuzz(3))
    def test_input_5_return_12fuzz4buzz(self):
        self.assertEqual("1,2,fuzz,4,buzz", Fuzzbuzz(5))
    def test_return_fuzzbuzz_in_result(self):
        self.assertIn("fuzzbuzz", Fuzzbuzz(15))
if __name__ == '__main__':
    unittest.main()
