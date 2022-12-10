import unittest
# import obstacles
from world.text import world as world
from world import obstacles as obstacles
from io import StringIO
from test_base import run_unittests
from test_base import captured_io
import sys


class MyTestCase(unittest.TestCase):
    def test_do_right_turn(self):
        sys.stdout = StringIO()
        result = world.do_right_turn
        self.assertTrue(result("Hal"))

if __name__ == '__main__':
    unittest.main()