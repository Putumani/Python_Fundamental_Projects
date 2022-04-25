import io
import unittest
import robot
from unittest.mock import patch
from io import StringIO


class TestRobot(unittest.TestCase):


    def test_command_replay(self):
        result = robot.do_command_replay
        self.assertEqual(result("HAL"), (True,' > HAL replayed 0 commands.'))
    
    
    def test_do_command_silent_replay(self):
        result = robot.do_command_silent_replay
        self.assertEqual(result("HAL"), (True, " > HAL replayed 0 commands silently."))


    def test_do_replay_reversed(self):
        result = robot.do_replay_reversed
        self.assertEqual(result("HAL"), (True, " > HAL replayed 0 commands in reverse."))
 

if __name__ == "__main__":
    unittest.main()