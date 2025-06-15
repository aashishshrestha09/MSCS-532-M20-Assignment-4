import matplotlib.pyplot as plt
import os


def plot_performance(
    dataset_sizes,
    results_time,
    results_memory,
    title_suffix="",
    output_file="outputs/sorting_performance.png",
    log_scale=True,
):
    """
    Plot execution time and memory usage for sorting algorithms.

    Args:
        dataset_sizes (list of int): List of dataset sizes tested.
        results_time (dict): Mapping of algorithm names to execution times (ms).
        results_memory (dict): Mapping of algorithm names to memory usages (KB).
        title_suffix (str, optional): Suffix to append to plot titles.
        output_file (str, optional): Path to save the generated plot image.
        log_scale (bool, optional): Whether to use log scale for y-axes. Default is True.
    """

    # Ensure output directory exists
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create figure with two subplots
    plt.figure(figsize=(14, 6))

    # Execution Time Plot
    plt.subplot(1, 2, 1)
    for algo in results_time:
        plt.plot(dataset_sizes, results_time[algo], marker="o", label=algo)
    plt.xlabel("Dataset Size")
    plt.ylabel("Execution Time (ms)")
    plt.title(f"Execution Time {title_suffix}")
    if log_scale:
        plt.yscale("log")
    plt.legend()
    plt.grid(True, which="both", ls="--")

    # Memory Usage Plot
    plt.subplot(1, 2, 2)
    for algo in results_memory:
        plt.plot(dataset_sizes, results_memory[algo], marker="o", label=algo)
    plt.xlabel("Dataset Size")
    plt.ylabel("Memory Usage (KB)")
    plt.title(f"Memory Usage {title_suffix}")
    if log_scale:
        plt.yscale("log")
    plt.legend()
    plt.grid(True, which="both", ls="--")

    # Optimize layout and save
    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()
