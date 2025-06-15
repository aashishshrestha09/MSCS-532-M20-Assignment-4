import unittest
from src.merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):
    def test_random(self):
        arr = [4, 2, 7, 1, 3]
        expected = sorted(arr)
        merge_sort(arr)
        self.assertEqual(arr, expected)

    def test_sorted(self):
        arr = [1, 2, 3, 4, 5]
        merge_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_empty(self):
        arr = []
        merge_sort(arr)
        self.assertEqual(arr, [])

    def test_one_element(self):
        arr = [42]
        merge_sort(arr)
        self.assertEqual(arr, [42])

if __name__ == "__main__":
    unittest.main()
