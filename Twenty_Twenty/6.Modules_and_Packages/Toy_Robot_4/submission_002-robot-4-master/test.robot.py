import unittest
import robot
from world.text import world as world
from world import obstacles as obstacles
from io import StringIO
from test_base import run_unittests
from test_base import captured_io
import sys


class MyTestCase(unittest.TestCase):
    def test_handle_command(self):
        sys.stdout = StringIO()
        self.assertTrue(robot.handle_command("Hal", "forward 10"))


if __name__ == '__main__':
    unittest.main()