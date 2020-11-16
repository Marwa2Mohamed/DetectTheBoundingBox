import unittest
from boundingmain import findTheSlope


class TestTheStraightLineSlope(unittest.TestCase):
    def test_validArguments(self):
        # Test that both deltaX and deltaY > 0
        self.assertEqual(findTheSlope(0,1,3,7), 2)
        self.assertEqual(findTheSlope(0.0,1,3,7), 2)
        self.assertEqual(findTheSlope(0,1.0,3,7), 2)
        self.assertEqual(findTheSlope(0,1,3.0,7), 2)
        self.assertEqual(findTheSlope(0, 1, 3, 7.0), 2)
        self.assertEqual(findTheSlope(0.0, 1.0, 3.0, 7.0), 2)
        self.assertEqual(findTheSlope("0", 1.0, 3.0, 7.0), 2)
        self.assertEqual(findTheSlope("0", 1, 3, 7), 2)
        self.assertEqual(findTheSlope(0,1,3,7), 2.0)
        self.assertEqual(findTheSlope(0.0,1,3,7), 2.0)
        self.assertEqual(findTheSlope(0,1.0,3,7), 2.0)
        self.assertEqual(findTheSlope(0,1,3.0,7), 2.0)
        self.assertEqual(findTheSlope(0, 1, 3, 7.0), 2.0)
        self.assertEqual(findTheSlope(0.0, 1.0, 3.0, 7.0), 2.0)
        self.assertEqual(findTheSlope("0.0", 1.0, 3.0, 7.0), 2.0)

    def test_InvalidArguments(self):
        # Test that both deltaX and deltaY > 0
        self.assertRaises(ZeroDivisionError, findTheSlope, 3,1,3,7)
        self.assertRaises(ValueError, findTheSlope,0,1 ,3, 1)
        self.assertRaises(TypeError, findTheSlope, [0, 8], 1, 3, 7)
        self.assertRaises(TypeError, findTheSlope, "hello", 1, 3, 7)
        self.assertRaises(TypeError, findTheSlope, "0.o", 1, 3, 7)



if __name__ == '__main__':
    unittest.main()
