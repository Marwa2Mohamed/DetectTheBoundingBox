import unittest
from boundingmain import findTheSlope


class TestTheStraightLineSlope(unittest.TestCase):
    def test_validArguments(self):
        # Test that both deltaX and deltaY > 0
        self.assertEqual(findTheSlope(3, 6), 2)
        self.assertEqual(findTheSlope(3.0, 6), 2)
        self.assertEqual(findTheSlope(3, 6.0), 2)
        self.assertEqual(findTheSlope(3.0, 6.0), 2)
        self.assertEqual(findTheSlope(3, 6), 2.0)
        self.assertEqual(findTheSlope(3.0, 6), 2.0)
        self.assertEqual(findTheSlope(3, 6.0), 2.0)
        self.assertEqual(findTheSlope(3.0, 6.0), 2.0)

    def test_InvalidArguments(self):
        # Test that both deltaX and deltaY > 0
        self.assertRaises(ZeroDivisionError, findTheSlope, 0, 3)
        self.assertRaises(ValueError, findTheSlope, 3, 0)



if __name__ == '__main__':
    unittest.main()
