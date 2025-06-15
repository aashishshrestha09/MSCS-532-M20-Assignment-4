# Assignment 4: Heap Data Structures: Implementation, Analysis, and Applications

## Overview

This assignment aims to solidify your understanding of heap data structures, their implementation using arrays (lists), and their applications in sorting algorithms (Heapsort) and priority queue operations. You will implement Heapsort, perform empirical analysis against other sorting algorithms (Merge Sort, Quick Sort), and build a custom Priority Queue with task scheduling capabilities.

## Project Structure

```bash
.
├── heap_sort
│   ├── img
│   │   ├── sorting_performance_random.png
│   │   ├── sorting_performance_reverse.png
│   │   └── sorting_performance_sorted.png
│   ├── main.py
│   ├── outputs
│   │   ├── results_random.csv
│   │   ├── results_reverse.csv
│   │   └── results_sorted.csv
│   ├── README.md
│   ├── src
│   │   ├── __init__.py
│   │   ├── heap_sort.py
│   │   ├── merge_sort.py
│   │   └── quick_sort.py
│   ├── tests
│   │   ├── test_heapsort.py
│   │   ├── test_mergesort.py
│   │   └── test_quicksort.py
│   └── utils
│       ├── __init__.py
│       ├── dataset_utils.py
│       ├── file_utils.py
│       ├── metrics_utils.py
│       └── plot_utils.py
├── priority_queue
│   ├── README.md
│   ├── src
│   │   ├── __init__.py
│   │   └── priority_queue.py
│   └── tests
│       └── test_priority_queue.py
├── pyproject.toml
├── README.md
└── src

```

## Components

### Heapsort Implementation & Analysis

- Implemented Heapsort using a max-heap structure.
- Performed time and space complexity analysis for best, average, and worst cases.
- Empirically compared Heapsort, Merge Sort, and Quick Sort on datasets of varying sizes and distributions (sorted, reverse-sorted, random).
- Visualized performance metrics.

📂 Refer to: [/heap_sort/](./heap_sort/)

**Key Outputs**:

- 📊 CSV results: [/heap_sort/outputs/](./heap_sort/outputs/)
- 📈 Graph images: [/heap_sort/img/](./heap_sort/img/)
- 📖 [Summary of Findings](./heap_sort/README.md#summary-of-findings)

### 📌 Priority Queue Implementation & Applications

- Developed a Priority Queue (binary heap) from scratch.
- Implemented core operations:
  - `insert()`
  - `extract_max()` / `extract_min()`
  - `increase_key()` / `decrease_key()`
  - `is_empty()`
- Designed a Task class to simulate a basic task scheduler.
- Analyzed time complexity of all queue operations.
- Included comprehensive unit tests.

📂 Refer to: [/priority_queue/](./priority_queue/)

## Setup

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

## How to Run the Code

### Run Heapsort Benchmark

Full setup instructions, execution steps, summary of findings, graphs, and outputs are available in the [Heapsort README](./heap_sort/README.md).

### Run Priority Queue Tests

Complete instructions for running the Priority Queue implementation and unit tests are available in the [Priority Queue README](./priority_queue/README.md).
