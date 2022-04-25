import io
import unittest
import robot
from unittest.mock import patch
from io import StringIO


class TestRobot(unittest.TestCase):
    def test_command_help(self):
        self.assertEqual(robot.command_help(), """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move robot forward a given number of steps
BACK - move robot back a given number of steps
RIGHT - turn the robot 90 degrees to the right
LEFT - turn the robot 90 degrees to the left
SPRINT - sprint forward according to a number of steps""")
    
    
    def test_check_valid_command(self):
        result = robot.check_valid_command
        self.assertEqual(result("HAL", "forward"), None)
        self.assertEqual(result("HAL", "forward 10"), True)
        self.assertEqual(result("HAL", ""), None)
        self.assertEqual(result("HAL", "HELP"), True)
        self.assertEqual(result("HAL", "help"), True)
        self.assertEqual(result("HAL", "oFF"), True)
        self.assertEqual(result("HAL", "Off"), True)


    def test_track_position(self):
        result = robot.track_position
        self.assertEqual(result("HAL", [0, 0], "forward;10","up", 10), (0, 10))
        self.assertEqual(result("HAL", [5, 0], "forward;5","right", 10), (15, 0))
        self.assertEqual(result("HAL", [0, 0], "back;10","left", 10), (10, 0))
        self.assertEqual(result("HAL", [0, 0], "back;5","down", 5), (0, 5))


    def test_forward_movement(self):
        result = robot.forward_movement
        self.assertEqual(result("HAL",[0,10],"forward", "up", 10), " > HAL moved forward by 10 steps.")
        self.assertEqual(result("HAL",[0,0],"forward","up", 0), " > HAL moved forward by 0 steps.")
        self.assertEqual(result("HAL",[0,-10],"forward","up", -10), " > HAL moved forward by -10 steps.")
    
    # def test_sprint_movement(self):
    #     result = robot.sprint_movement
    #     self.assertEqual(result("HAL",[0,0],"forward", "up", 5), " > HAL now at position (0,15).")
    #     self.assertEqual(result("HAL",[0,0],"forward","up", 0), "HAL: Sorry, I cannot go outside my safe zone.")
    #     self.assertEqual(result("HAL",[0,-10],"back","left", 10), "HAL: Sorry, I cannot go outside my safe zone.")


    def test_change_direction(self):
        result = robot.change_direction
        self.assertEqual(result("up", "R"), "up")
        self.assertEqual(result("down", "R"), "down")
        self.assertEqual(result("right", "L"), "right")
        self.assertEqual(result("left", "L"), "left")


if __name__ == "__main__":
    unittest.main()