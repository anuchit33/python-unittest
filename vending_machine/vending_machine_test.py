
import unittest
from vending_machine import VendingMachine

class TestVendingMachine(unittest.TestCase):
    def test_coin_fit_product_can_change(self):
        one = 3
        five = 0
        ten = 1
        product = 1

        result = VendingMachine(one,five,ten,product)
        self.assertEqual(result['one'],0)
        self.assertEqual(result['five'],0)
        self.assertEqual(result['ten'],0)
        self.assertEqual(result['status'],0)

    def test_coin_over_product_can_change_one(self):
        one = 4
        five = 0
        ten = 1
        product = 1

        result = VendingMachine(one,five,ten,product)
        self.assertEqual(result['one'],1)
        self.assertEqual(result['five'],0)
        self.assertEqual(result['ten'],0)
        self.assertEqual(result['status'],0)

    def test_coin_over_product_can_change_five(self):
        one = 3
        five = 1
        ten = 1
        product = 1

        result = VendingMachine(one,five,ten,product)
        self.assertEqual(result['one'],0)
        self.assertEqual(result['five'],1)
        self.assertEqual(result['ten'],0)
        self.assertEqual(result['status'],0)

    def test_coin_over_product_can_change_ten(self):
        one = 3
        five = 0
        ten = 2
        product = 1

        result = VendingMachine(one,five,ten,product)
        self.assertEqual(result['one'],0)
        self.assertEqual(result['five'],0)
        self.assertEqual(result['ten'],1)
        self.assertEqual(result['status'],0)

    def test_coin_less_product_not_change(self):
        one = 3
        five = 0
        ten = 0
        product = 1

        result = VendingMachine(one,five,ten,product)
        self.assertEqual(result['one'],3)
        self.assertEqual(result['five'],0)
        self.assertEqual(result['ten'],0)
        self.assertEqual(result['status'],1)

    def test_not_product_not_change(self):
        one = 1
        five = 1
        ten = 1
        product = 4

        result = VendingMachine(one,five,ten,product)
        self.assertEqual(result['one'],1)
        self.assertEqual(result['five'],1)
        self.assertEqual(result['ten'],1)
        self.assertEqual(result['status'],1)

if __name__ == '__main__':
    unittest.main()