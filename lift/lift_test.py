
import unittest
from lift import Lift

class TestLift(unittest.TestCase):
    def test_lift_current_floor(self):
        # floor_max = 100, current_floor = 1
        lift = Lift(current_floor=10,floor_max=100)
        self.assertEqual(10, lift.getCurrentFloor())

    def test_lift_call_is_valid_and_status_stop(self):
        # floor_max = 100, current_floor = 1
        lift = Lift(current_floor=1,floor_max=100)

        # call lift at floor 10
        lift.callAt(1)
        self.assertEqual('STOP', lift.getStatus())

    def test_lift_call_is_valid_and_status_up(self):
        # floor_max = 100, current_floor = 1
        lift = Lift(current_floor=1,floor_max=100)

        # call lift at floor 10
        lift.callAt(10)
        self.assertEqual('UP', lift.getStatus())

    def test_lift_call_is_valid_and_status_down(self):
        # floor_max = 100, current_floor = 10
        lift = Lift(current_floor=10,floor_max=100)

        # call lift at floor 1
        lift.callAt(1)
        self.assertEqual('DOWN', lift.getStatus())

    def test_lift_call_isnot_valid_and_status_stop(self):
        # floor_max = 100, current_floor = 10
        lift = Lift(current_floor=10,floor_max=100)

        # call lift at floor 101
        lift.callAt(101)

        self.assertEqual('STOP', lift.getStatus())

    def test_lift_select_floor_is_valid_and_status_up(self):
        # floor_max = 100, current_floor = 1
        lift = Lift(current_floor=1,floor_max=100)
        
        # call lift at floor 1
        lift.callAt(1)

        # select floor = 10
        lift.start(10)

        self.assertEqual('UP', lift.getStatus())

    def test_lift_select_floor_is_valid_and_status_down(self):
        # floor_max = 100, current_floor = 1
        lift = Lift(current_floor=1,floor_max=100)
        
        # call lift at floor 10
        lift.callAt(10)

        # select floor = 1
        lift.start(1)

        self.assertEqual('DOWN', lift.getStatus())

    def test_lift_select_floor_isnot_valid_and_status_stop(self):
        # floor_max = 100, current_floor = 1
        lift = Lift(current_floor=1,floor_max=100)
        
        # call lift at floor 1
        lift.callAt(1)

        # select floor = 101
        lift.start(101)

        self.assertEqual('STOP', lift.getStatus())
    
    def test_lift_select_floor_is_valid_and_status_stop(self):
        # floor_max = 100, current_floor = 1
        lift = Lift(current_floor=1,floor_max=100)
        
        # call lift at floor 1
        lift.callAt(1)

        # select floor = 1
        lift.start(1)

        self.assertEqual('STOP', lift.getStatus())
     
    def test_lift_weight_is_valid_and_status_down_and_not_beep(self):
        # floor_max = 100, current_floor = 1
        lift = Lift(current_floor=1,floor_max=100)
        
        # call lift at floor 10
        lift.callAt(10)

        # select floor = 1,weight = 100
        lift.start(1,weight=100)

        self.assertEqual('DOWN', lift.getStatus())
        self.assertEqual(False, lift.getBeep())

    def test_lift_weight_isnot_valid_and_status_stop_and_beep(self):
        # floor_max = 100, current_floor = 1
        lift = Lift(current_floor=1,floor_max=100)
        
        # call lift at floor 1
        lift.callAt(1)

        # select floor = 10,weight = 100
        lift.start(10,weight=1001)

        self.assertEqual('STOP', lift.getStatus())
        self.assertEqual(True, lift.getBeep())

if __name__ == '__main__':
    unittest.main()
