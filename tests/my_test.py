import unittest
from src import my_sort

class MySortTest(unittest.TestCase):
    def test_my_sort_v1(self):
        self.assertEqual(my_sort([1, -3, 7]), [-3, 1, 7])
    def test_my_sort_v2(self):
        self.assertEqual(my_sort([13, 19, -8, 0]), [-8, 0, 13, 19])


if __name__ == '__main__':
    unittest.main()