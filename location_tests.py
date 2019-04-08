import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        self.assertNotEqual(repr(loc), "not")

    
    # Add more tests!
    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        loc3 = Location("NO", 910, 21)
        self.assertEqual(loc1 == loc2, True)
        self.assertEqual(loc1 == loc3, False)

if __name__ == "__main__":
        unittest.main()
