import random


def quick_sort(arr):
    """
    In-place Quicksort with randomized pivot selection.

    Args:
        arr (list): The list of elements to be sorted.
    """

    def partition(a, low, high):
        # Choose a random pivot and move it to the end
        pivot_index = random.randint(low, high)
        a[pivot_index], a[high] = a[high], a[pivot_index]
        pivot = a[high]

        i = low
        for j in range(low, high):
            if a[j] < pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        # Place pivot at its correct position
        a[i], a[high] = a[high], a[i]
        return i

    def _quick_sort(a, low, high):
        if low < high:
            p = partition(a, low, high)
            _quick_sort(a, low, p - 1)
            _quick_sort(a, p + 1, high)

    if len(arr) <= 1:
        return
    _quick_sort(arr, 0, len(arr) - 1)
