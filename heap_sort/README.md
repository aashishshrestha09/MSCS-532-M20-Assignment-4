# Heap Data Structures: Implementation, Analysis, and Applications

## Overview

This project implements and analyzes the **Heapsort** algorithm as part of a broader study of heap data structures. It includes:

- A clean, efficient Python implementation of Heapsort.
- Comparative benchmarking with **Merge Sort** and **Quick Sort**.
- Empirical performance analysis on various dataset sizes and types (sorted, reverse-sorted, random).
- Visualization of time and memory usage across sorting algorithms.

## Project Structure

```bash
.
├── img            # Performance plots for different dataset types
│   ├── sorting_performance_random.png
│   ├── sorting_performance_reverse.png
│   └── sorting_performance_sorted.png
├── main.py         # Main benchmarking and analysis runner script
├── outputs         # Benchmark results CSV files
│   ├── results_random.csv
│   ├── results_reverse.csv
│   └── results_sorted.csv
├── README.md
├── src             # Sorting algorithm implementations
│   ├── __init__.py
│   ├── heap_sort.py
│   ├── merge_sort.py
│   └── quick_sort.py
├── tests           # Unit tests for sorting algorithms
│   ├── test_heapsort.py
│   ├── test_mergesort.py
│   └── test_quicksort.py
└── utils           # Utility modules
    ├── __init__.py
    ├── dataset_utils.py
    ├── file_utils.py
    ├── metrics_utils.py
    └── plot_utils.py
```

## Heapsort Implementation

The Heapsort algorithm follows these key steps:

1. **Build Max-Heap** from the input array.
2. Repeatedly **extract the maximum element** from the heap and place it at the end of the array.
3. Restore the **heap property** after each extraction.

The implementation ensures:

- **Time Complexity**: O(n log n) in the best, average, and worst cases.
- **Space Complexity**: O(1) additional space (in-place sorting).
- Stability is not guaranteed due to swapping.

## Performance Analysis

- Benchmarks are performed across multiple dataset sizes: 500, 1000, 2000, and 5000 elements.
- Dataset types include **Sorted**, **Reverse-Sorted**, and **Random**.
- Metrics captured:
  - Execution time (in milliseconds).
  - Memory usage (in kilobytes).
- Results are saved as CSV files (`outputs/`) and visualized as PNG plots (`img/`).
- Heapsort is compared against Merge Sort and Quick Sort to observe practical performance differences and relate them to theoretical expectations.

## Setup

### Pre-requisites

- Install [`python`](https://www.python.org/downloads/).
- Install [`pip`](https://pip.pypa.io/en/stable/installation/).

### Clone the repository

```bash
git clone https://github.com/aashishshrestha09/MSCS-532-M20-Assignment-4.git
cd MSCS-532-M20-Assignment-4

```

### Create and Activate a Virtual Environment:

```bash
python3 -m venv .venv
. .venv/bin/activate
```

### Install as editable with "dev" packages

```bash
pip install --editable ".[dev]"
```

## Run Benchmarks

```bash
cd heap_sort
python main.py
```

## Running Tests

```bash
cd heap_sort
python -m unittest discover -s tests
```

## Results & Visualizations

### CSV result files: [/outputs/](./outputs/)

Contains detailed benchmark results (execution time in milliseconds and memory usage in kilobytes) for each algorithm on each dataset type:

- results_sorted.csv
- results_reverse.csv
- results_random.csv

### Performance graphs: [/img/](./img/)

Visual line charts comparing execution times and memory usage for the sorting algorithms across dataset sizes:

- sorting_performance_sorted.png
- sorting_performance_reverse.png
- sorting_performance_random.png

## Summary of Findings

This document summarizes the empirical performance results for **Heap Sort**, **Merge Sort**, and **Quick Sort** across different dataset types and sizes.

Each table below presents:

- **Time (ms)** → Execution time in milliseconds.
- **Memory (KB)** → Peak memory used during the sort in kilobytes.

**Table format**: `[Execution Time (ms) / Memory Usage (KB)]`

**Example:**

| Size | Heap Sort   |
| :--- | :---------- |
| 500  | 2.42 / 0.25 |

- **2.42 ms** → Time taken to sort
- **0.25 KB** → Peak memory usage during sort

### Sorted Dataset

| Size | Heap Sort    | Merge Sort    | Quick Sort   |
| :--- | :----------- | :------------ | :----------- |
| 500  | 2.42 / 0.25  | 1.14 / 7.81   | 3.57 / 1.52  |
| 1000 | 7.20 / 0.32  | 5.45 / 15.66  | 10.32 / 1.62 |
| 2000 | 18.65 / 0.38 | 17.57 / 31.31 | 26.98 / 1.79 |
| 5000 | 61.83 / 0.50 | 73.26 / 78.45 | 77.57 / 2.02 |

### Reverse-Sorted Dataset

| Size | Heap Sort    | Merge Sort    | Quick Sort   |
| :--- | :----------- | :------------ | :----------- |
| 500  | 1.52 / 0.25  | 1.08 / 7.81   | 3.37 / 1.40  |
| 1000 | 4.89 / 0.32  | 4.97 / 15.66  | 12.04 / 1.79 |
| 2000 | 14.01 / 0.38 | 15.99 / 31.31 | 24.61 / 2.02 |
| 5000 | 47.92 / 0.50 | 67.74 / 78.28 | 73.33 / 2.15 |

### Random Dataset

| Size | Heap Sort    | Merge Sort    | Quick Sort   |
| :--- | :----------- | :------------ | :----------- |
| 500  | 3.16 / 0.25  | 1.15 / 7.81   | 3.14 / 1.23  |
| 1000 | 6.03 / 0.32  | 5.28 / 15.66  | 10.05 / 1.60 |
| 2000 | 16.28 / 0.38 | 17.31 / 31.31 | 24.58 / 1.76 |
| 5000 | 55.13 / 0.50 | 72.83 / 78.28 | 79.98 / 1.99 |

### Observations

- **Heapsort** maintained consistently low memory usage (approx. **O(1)**) and competitive execution times, especially on **reverse-sorted** and **random** datasets.
- **Merge Sort** was typically fastest for small datasets but incurred high memory overhead (approx. **O(n)**) due to additional arrays.
- **Quick Sort** demonstrated good average-case performance on **random datasets** but slower results on **sorted** and **reverse-sorted** datasets due to pivot selection inefficiencies.

## Theoretical Time Complexity Confirmation

| Algorithm  | Best Case  | Average Case | Worst Case                     |
| :--------- | :--------- | :----------- | :----------------------------- |
| Heap Sort  | O(n log n) | O(n log n)   | O(n log n)                     |
| Merge Sort | O(n log n) | O(n log n)   | O(n log n)                     |
| Quick Sort | O(n log n) | O(n log n)   | O(n²) (if pivot poorly chosen) |

- All algorithms demonstrated **O(n log n)** scaling behavior as dataset size increased.
- **Merge Sort** uses extra space (O(n)) while **Heapsort** is in-place (O(1) auxiliary space).
- **Quick Sort**'s variability in performance on pre-sorted and reverse-sorted inputs is a known issue due to poor pivot selection.
