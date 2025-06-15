import os
import csv
from src import merge_sort, quick_sort, heap_sort
from utils import dataset_utils, metrics_utils, plot_utils, file_utils

def main():
    """
    Benchmarks Heap Sort, Merge Sort, and Quick Sort on various dataset types and sizes.
    Saves performance results to CSV files and generates plots.
    """
    dataset_sizes = [500, 1000, 2000, 5000]
    dataset_types = ["Sorted", "Reverse", "Random"]

    os.makedirs("outputs", exist_ok=True)
    os.makedirs("img", exist_ok=True)

    for dtype in dataset_types:
        print(f"\nDataset Type: {dtype}")
        print(f"{'Size':<8} {'Algorithm':<12} {'Time (ms)':<12} {'Memory (KB)':<12}")
        print("=" * 60)

        results_time = {"Heap Sort": [], "Merge Sort": [], "Quick Sort": []}
        results_memory = {"Heap Sort": [], "Merge Sort": [], "Quick Sort": []}

        for size in dataset_sizes:
            if dtype == "Sorted":
                data = dataset_utils.generate_sorted_dataset(size)
            elif dtype == "Reverse":
                data = dataset_utils.generate_reverse_sorted_dataset(size)
            else:
                data = dataset_utils.generate_random_dataset(size)

            # Heapsort
            time_ms, memory_kb = metrics_utils.measure_performance(
                heap_sort.heap_sort, data.copy()
            )
            print(f"{size:<8} {'Heap Sort':<12} {time_ms:<12.2f} {memory_kb:<12.2f}")
            results_time["Heap Sort"].append(time_ms)
            results_memory["Heap Sort"].append(memory_kb)

            # Merge Sort
            time_ms, memory_kb = metrics_utils.measure_performance(
                merge_sort.merge_sort, data.copy()
            )
            print(f"{size:<8} {'Merge Sort':<12} {time_ms:<12.2f} {memory_kb:<12.2f}")
            results_time["Merge Sort"].append(time_ms)
            results_memory["Merge Sort"].append(memory_kb)

            # Quick Sort
            time_ms, memory_kb = metrics_utils.measure_performance(
                quick_sort.quick_sort, data.copy()
            )
            print(f"{size:<8} {'Quick Sort':<12} {time_ms:<12.2f} {memory_kb:<12.2f}")
            results_time["Quick Sort"].append(time_ms)
            results_memory["Quick Sort"].append(memory_kb)

        csv_filename = f"results_{dtype.lower()}.csv"
        try:
            file_utils.save_results_to_csv(
                "outputs", csv_filename, dtype, dataset_sizes, results_time, results_memory
            )
            print(f"\nResults saved to outputs/{csv_filename}")
        except Exception as e:
            print(f"Failed to save CSV for {dtype}: {e}")

        try:
            plot_utils.plot_performance(
                dataset_sizes,
                results_time,
                results_memory,
                title_suffix=f"({dtype} Data)",
                output_file=f"img/sorting_performance_{dtype.lower()}.png",
            )
        except Exception as e:
            print(f"Failed to plot performance for {dtype}: {e}")

if __name__ == "__main__":
    main()
