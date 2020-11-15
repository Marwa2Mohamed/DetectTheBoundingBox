import unittest
from bounding import *

class MyTestCase(unittest.TestCase):

    def test_InvalidInput(self):
        # self.assertRaises(Error, BoundingBoxStraightLine([0, 1],3,7))
        self.assertRaises(TypeError, BoundingBoxStraightLine,[0,8],1, 3, 7)
        self.assertRaises(TypeError, BoundingBoxStraightLine,"hello", 1, 3, 7)




if __name__ == '__main__':
    unittest.main()
