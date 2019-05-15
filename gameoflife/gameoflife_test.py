
import unittest
from gameoflife import Gameoflife

class TestGameoflife(unittest.TestCase):

    def test_not_array(self):
        array = 1
        self.assertEqual("Error!", Gameoflife(array))

    def test_array_not_3d(self):
        array = [
                    ['D','D','L'],
                    ['D','L'],
                    ['D','D'],
                ]
        self.assertEqual("Error!", Gameoflife(array))
    
    def test_L_center_L_around_lees_2_is_dies(self):
        array = [
                    ['D','D','L'],
                    ['D','L','D'],
                    ['D','D','D'],
                ]
        
        self.assertEqual("Dies!", Gameoflife(array))

    def test_L_center_L_around_has_2_is_alive(self):
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

    def test_L_center_L_around_over_3_is_alive(self):
        array = [
                    ['L','D','L'],
                    ['D','L','L'],
                    ['D','L','D'],
                ]
        self.assertEqual("Dies!", Gameoflife(array))

    def test_D_center_L_around_has_3_is_alive(self):
        array = [
                    ['D','D','L'],
                    ['D','D','L'],
                    ['D','D','L'],
                ]
        self.assertEqual("Becomes alive!", Gameoflife(array))

    def test_D_center_L_around_over_3_is_dies(self):
        array = [
                    ['D','D','L'],
                    ['D','D','L'],
                    ['D','L','L'],
                ]
        self.assertEqual("Dies!", Gameoflife(array))

    def test_D_center_L_around_less_3_is_dies(self):
        array = [
                    ['D','D','L'],
                    ['D','D','L'],
                    ['D','D','D'],
                ]
        self.assertEqual("Dies!", Gameoflife(array))
if __name__ == '__main__':
    unittest.main()
