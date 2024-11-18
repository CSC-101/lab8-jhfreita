import math
import unittest
import group

class TestCases(unittest.TestCase):
    def test_grous_of_3_1(self):
        self.assertEqual(group.groups_of_3([1, 2, 3, 4, 5, 6, 7]), [[1, 2, 3], [4, 5, 6], [7]])
    def test_groups_of_3_2(self):
        self.assertEqual(group.groups_of_3([2, 4, 6, 8, 10]), None)