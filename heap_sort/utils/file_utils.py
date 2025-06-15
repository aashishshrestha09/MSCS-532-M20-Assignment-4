import csv
import os


def save_results_to_csv(
    output_dir, filename, dataset_type, dataset_sizes, results_time, results_memory
):
    """
    Save benchmarking results to a CSV file.

    Args:
        output_dir (str): Directory to save the CSV file.
        filename (str): Name of the CSV file.
        dataset_type (str): Type of dataset (e.g., 'Sorted', 'Random').
        dataset_sizes (list): List of dataset sizes.
        results_time (dict): Dictionary mapping algorithms to execution times.
        results_memory (dict): Dictionary mapping algorithms to memory usage.
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filepath = os.path.join(output_dir, filename)

    # Write CSV file
    with open(filepath, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Write header
        header = [
            "Dataset Type",
            "Dataset Size",
            "Algorithm",
            "Execution Time (ms)",
            "Memory Usage (KB)",
        ]
        writer.writerow(header)

        # Write data rows
        for size in dataset_sizes:
            for algo in results_time.keys():
                writer.writerow(
                    [
                        dataset_type,
                        size,
                        algo,
                        results_time[algo][dataset_sizes.index(size)],
                        results_memory[algo][dataset_sizes.index(size)],
                    ]
                )
