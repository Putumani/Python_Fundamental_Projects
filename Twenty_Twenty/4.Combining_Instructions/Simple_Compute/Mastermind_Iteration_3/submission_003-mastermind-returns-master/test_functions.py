import unittest
from unittest.mock import patch 
from io import StringIO
import mastermind

class TestMastermind(unittest.TestCase):

    for i in range(100):
       
        def test_create_code(self):
            result = mastermind.create_code()
            self.assertNotEqual(result, 0)
            self.assertNotEqual(result, 9)
            self.assertEqual(len(result), 4)
            
        
        def test_check_correcteness(self):
            
            result = mastermind.check_correctness
            self.assertEqual(result(11,True,4),True)
            self.assertEqual(result(8,False,2),None)
    
        @patch("sys.stdin", StringIO("1234\n5412\n"))
        def test_get_user_input(self):
            result =  mastermind.get_user_input
            self.assertEqual(result([1234]), "1234")
    
        @patch("sys.stdin", StringIO("1254\n1254\n"))   
        def test_take_turn(self):
            self.assertEqual(mastermind.take_turn([1,2,5,4],"1254"),(4,0))
            self.assertEqual(mastermind.take_turn([1,2,5,4],"8754"),(2,0))
            self.assertEqual(mastermind.take_turn([1,2,5,4],"2187"),(0,2))
            self.assertEqual(mastermind.take_turn([1,2,5,4],"6387"),(0,0))
        
if __name__ == "__main__":
    unittest.main()
    
