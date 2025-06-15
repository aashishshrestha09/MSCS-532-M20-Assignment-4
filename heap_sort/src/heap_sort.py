def heapify(arr: list[int], n: int, i: int) -> None:
    """
    Ensure the subtree rooted at index i obeys the max-heap property.

    Args:
        arr (list[int]): The heap array.
        n (int): Size of the heap.
        i (int): Index of the root element of the subtree.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr: list[int]) -> None:
    """
    Perform Heapsort on the given list in-place.

    Args:
        arr (list[int]): The array to be sorted.
    """
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
