def merge_sort(arr: list) -> None:
    """
    In-place stable merge sort.
    
    Sorts the input list `arr` by modifying it directly.
    Maintains the order of equal elements (stable).
    
    Args:
        arr (list): The list to be sorted.
    """
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    # Merge the sorted halves back into arr
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements if any
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
