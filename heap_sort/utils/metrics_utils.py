import time
import tracemalloc


def measure_performance(func, data):
    """
    Measure the execution time and peak memory usage of a function.

    Args:
        func (callable): The sorting function to test.
        data (list): The input dataset (list of numbers).

    Returns:
        tuple: (execution time in milliseconds, peak memory usage in KB)
    """

    # Copy the data to avoid in-place modifications affecting other tests
    data_copy = data.copy()

    # Start memory tracking
    tracemalloc.start()

    # Start timer
    start_time = time.perf_counter()

    # Execute the function
    func(data_copy)

    # Stop timer
    end_time = time.perf_counter()

    # Measure peak memory usage
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Convert time to milliseconds and memory to KB
    elapsed_time_ms = (end_time - start_time) * 1000
    peak_memory_kb = peak / 1024

    return elapsed_time_ms, peak_memory_kb
