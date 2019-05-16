
import unittest
from tictactoe import Tictactoe

class TestTictactoe(unittest.TestCase):

    def test_playing(self):
        o = 1
        x = 2
        grid = [
            [0,0,0],
            [0,0,0],
            [x,0,0]
        ]
        self.assertEqual("Runing", Tictactoe().getStatus(grid))

    def test_win_row1(self):
        o = 1
        x = 2
        grid = [
            [o,o,o],
            [x,0,x],
            [x,0,0]
        ]
        self.assertEqual("O is Winner!", Tictactoe().getStatus(grid))

    def test_win_row2(self):
        o = 1
        x = 2
        grid = [
            [o,0,o],
            [x,x,x],
            [o,0,0]
        ]
        self.assertEqual("X is Winner!", Tictactoe().getStatus(grid))

    def test_win_row3(self):
        o = 1
        x = 2
        grid = [
            [o,0,o],
            [o,0,0],
            [x,x,x]
        ]
        self.assertEqual("X is Winner!", Tictactoe().getStatus(grid))

    def test_win_backslash(self):
        o = 1
        x = 2
        grid = [
            [x,0,0],
            [o,x,0],
            [o,o,x]
        ]
        self.assertEqual("X is Winner!", Tictactoe().getStatus(grid))

    def test_win_slash(self):
        o = 1
        x = 2
        grid = [
            [o,0,x],
            [o,x,0],
            [x,o,o]
        ]
        self.assertEqual("X is Winner!", Tictactoe().getStatus(grid))

    def test_stopped(self):
        o = 1
        x = 2
        grid = [
            [x,o,o],
            [o,x,x],
            [x,x,o]
        ]
        self.assertEqual("Always", Tictactoe().getStatus(grid))
if __name__ == '__main__':
    unittest.main()
