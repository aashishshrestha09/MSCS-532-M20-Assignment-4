import unittest
from src.quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):
    def test_random(self):
        arr = [4, 2, 7, 1, 3]
        expected = sorted(arr)
        quick_sort(arr)
        self.assertEqual(arr, expected)

    def test_sorted(self):
        arr = [1, 2, 3, 4, 5]
        quick_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_empty(self):
        arr = []
        quick_sort(arr)
        self.assertEqual(arr, [])

    def test_one_element(self):
        arr = [42]
        quick_sort(arr)
        self.assertEqual(arr, [42])

if __name__ == "__main__":
    unittest.main()
