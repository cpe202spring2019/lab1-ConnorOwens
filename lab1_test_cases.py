import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        self.assertEqual(max_list_iter([1,4,3,2,6]), 6) #checks for end bound
        self.assertEqual(max_list_iter([]), None) #Checks for 0 length case
        self.assertEqual(max_list_iter([6,2,4,5,1]), 6) #checks for beginning bound
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1]) #checks for functionality
        self.assertEqual(reverse_rec([]), []) # checks for 0 length case
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(None)

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4) #checks for functionality
        self.assertEqual(bin_search(4, 0, 2, [1,2,3,4,5,6]), None) #checks for target not in list range case and end bound
        self.assertEqual(bin_search(1, 1, 2, [1, 2, 3, 4, 5, 6]), None)  # checks for target not in list range case and beginning bound


if __name__ == "__main__":
        unittest.main()


