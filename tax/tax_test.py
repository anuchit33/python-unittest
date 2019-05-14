import unittest
from tax import Tax

class TestTax(unittest.TestCase):
    def test_not_number(self):
        self.assertEqual("Input Error!", Tax("str"))

    def test_min_0 (self):
        self.assertEqual("Input Error!", Tax(-1))

    def test_net_rate_0_net_is_0(self):
        self.assertEqual(0.0, Tax(0.0))

    def test_net_rate_0_net_is_150000 (self):
        self.assertEqual(0.0, Tax(150000))

    def test_net_rate_5_net_is_150001 (self):
        self.assertEqual(0.05, Tax(150001))

    def test_net_rate_5_net_is_300000 (self):
        self.assertEqual(7500, Tax(300000))
    
    def test_net_rate_10_net_is_300001 (self):
        self.assertEqual(7500.1, Tax(300001))

    def test_net_rate_10_net_is_500000 (self):
        self.assertEqual(37500.0, Tax(500000))

    def test_net_rate_15_net_is_500001 (self):
        self.assertEqual(37500.15, Tax(500001))
    
    def test_net_rate_15_net_is_750000 (self):
        self.assertEqual(112500.0, Tax(750000))

    def test_net_rate_20_net_is_750001 (self):
        self.assertEqual(112500.20, Tax(750001))

    def test_net_rate_20_net_is_1000000 (self):
        self.assertEqual(262500.0, Tax(1000000))

    def test_net_rate_25_net_is_1000001 (self):
        self.assertEqual(262500.25, Tax(1000001))
    
    def test_net_rate_25_net_is_2000000 (self):
        self.assertEqual(512500.0, Tax(2000000))

    def test_net_rate_30_net_is_2000001 (self):
        self.assertEqual(512500.30, Tax(2000001))

    def test_net_rate_30_net_is_5000000 (self):
        self.assertEqual(1112500.0, Tax(5000000))

    def test_net_rate_35_net_is_5000001 (self):
        self.assertEqual(1112500.35, Tax(5000001))

    def test_net_rate_35_net_is_9999999999_99 (self):
        self.assertEqual(2862500.0, Tax(9999999999.99))

    def test_net_rate_35_net_is_10000000000_00 (self):
        self.assertEqual(2862500.0, Tax(10000000000.00))
if __name__ == '__main__':
    unittest.main()