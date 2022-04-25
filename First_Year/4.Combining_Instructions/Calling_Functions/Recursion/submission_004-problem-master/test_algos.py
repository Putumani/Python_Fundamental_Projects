import unittest
import super_algos

class MyTestCase(unittest.TestCase):

    def test_find_min(self):
        result = super_algos.find_min
        self.assertEqual(result([]),-1)
        self.assertEqual(result(["a",8,4,5,3]),-1)
        self.assertEqual(result([1,5,6,3,5,1]),1)
        self.assertEqual(result([1,5,6,3,-54,1]),-54)
        self.assertEqual(result([8]),8)

    
    def test_sum_all(self):
        result = super_algos.sum_all
        self.assertEqual(result([]),-1)
        self.assertEqual(result(["a",8,4,5,3]),-1)
        self.assertEqual(result([1,5,6,3,5,1]),21)
        self.assertEqual(result([1,5,6,3,-5,1]),11)
        self.assertEqual(result([5]),5)
    
    def test_find_possible_strings(self):
        result = super_algos.find_possible_strings
        self.assertEqual(result(["a","b",1], 2),[])
        self.assertEqual(result([8,4,5,3],2),[])
        self.assertEqual(result(["a","b","c","d","e"],1),["a","b","c","d","e"])
        self.assertEqual(result(["a","b"],2),["aa","ab","ba","bb"])
    
if __name__ == "__main__":
    unittest.main()

