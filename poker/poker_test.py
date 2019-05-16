
import unittest
from poker import Poker

class TestPoker(unittest.TestCase):
    def test_royal_flush(self):
        result = [1,2,3,4,5]
        self.assertEqual(7, Poker.CheckScore(result))

    def test_royal_flush_no_order(self):
        result = [2,6,5,4,3]
        self.assertEqual(7, Poker.CheckScore(result))

    def test_five_of_a_kind_at_1 (self):
        result = [1,1,1,1,1]
        self.assertEqual(6, Poker.CheckScore(result))

    def test_five_of_a_kind_at_3 (self):
        result = [3,3,3,3,3]
        self.assertEqual(6, Poker.CheckScore(result))

    def test_full_house1_2 (self):
        result = [1,1,2,2,2]
        self.assertEqual(5, Poker.CheckScore(result))

    def test_full_house1_6 (self):
        result = [6,1,6,1,6]
        self.assertEqual(5, Poker.CheckScore(result))

    def test_three_of_a_kind (self):
        result = [6,1,6,2,6]
        self.assertEqual(4, Poker.CheckScore(result))
    def test_two_pair (self):
        result = [3,3,1,6,6]
        self.assertEqual(3, Poker.CheckScore(result))
    def test_one_pair (self):
        result = [4,2,2,3,5]
        self.assertEqual(2, Poker.CheckScore(result))
    
    def test_high_card (self):
        result = [2,3,1,4,6]
        self.assertEqual(1, Poker.CheckScore(result))

    def test_check_p1win_score7_vs_score1 (self):
        result1 = [1,2,3,4,5]
        result2 = [2,3,1,4,6]
        self.assertEqual(1, Poker.winner(result1,result2))

    def test_check_p2win_score1_vs_score7 (self):
        result1 = [2,3,1,4,6]
        result2 = [1,2,3,4,5]
        self.assertEqual(2, Poker.winner(result1,result2))

    def test_check_alays_score7_vs_score7_totalp1_is_win (self):
        result1 = [6,2,3,4,5]
        result2 = [1,2,3,4,5]
        self.assertEqual(1, Poker.winner(result1,result2))
    
    def test_check_always(self):
        result1 = [6,2,3,4,5]
        result2 = [6,2,3,4,5]
        self.assertEqual(0, Poker.winner(result1,result2))

if __name__ == '__main__':
    unittest.main()