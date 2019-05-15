
import unittest
from gameoflife import Gameoflife

class TestGameoflife(unittest.TestCase):

    
    def test_L_center_L_around_has_1(self):
        array = [
                    ['D','D','L'],
                    ['D','L','D'],
                    ['D','D','D'],
                ]
        
        self.assertEqual("Dies!", Gameoflife(array))

    def test_L_center_L_around_has_2(self):
        array = [
                    ['D','D','L'],
                    ['D','L','L'],
                    ['D','D','D'],
                ]
        
        self.assertEqual("Becomes alive!", Gameoflife(array))

    def test_L_center_L_around_has_3(self):
        array = [
                    ['D','D','L'],
                    ['D','L','L'],
                    ['D','L','D'],
                ]
        self.assertEqual("Becomes alive!", Gameoflife(array))

    def test_L_center_L_around_over_3(self):
        array = [
                    ['L','D','L'],
                    ['D','L','L'],
                    ['D','L','D'],
                ]
        self.assertEqual("Dies!", Gameoflife(array))

    def test_D_center_D_around_has_3(self):
        array = [
                    ['L','D','L'],
                    ['D','D','L'],
                    ['D','L','L'],
                ]
        self.assertEqual("Becomes alive!", Gameoflife(array))
if __name__ == '__main__':
    unittest.main()
