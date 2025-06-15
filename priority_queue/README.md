# Priority Queue Scheduler Simulation

## Overview

This project implements a max-heap priority queue tailored to managing scheduled tasks, alongside a scheduler simulation that uses the priority queue to process tasks based on their priority, arrival times, and deadlines.

The simulation models a simple scheduling environment where tasks arrive over time and are processed in order of priority, simulating a real-world scheduler prioritizing urgent work.

## Project Structure

```bash
.
├── README.md
├── src
│   ├── __init__.py
│   ├── priority_queue.py
│   └── scheduler_simulation.py
└── tests
    └── test_priority_queue.py
```

## Setup

## Pre-requisites

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

## Running the Scheduler Simulation

```bash
cd priority_queue
python src/scheduler_simulation.py
```

This will:

- Generate a random set of tasks with priorities, arrival times, and deadlines.
- Simulate the scheduling and processing of tasks.
- Print processing logs and a summary including task wait times.

## Running Tests

```bash
cd priority_queue
python -m unittest discover -s tests
```

## Design Decisions

### Priority Queue

- Implemented as a max-heap so the task with the highest priority is always processed first.
- Rationale for max-heap: Ensures higher priority tasks preempt lower priority ones, which aligns with typical real-world scheduling needs.
- Tasks are represented using a Task dataclass with attributes
- **priority**: Integer priority (higher means higher urgency)
- **task_id**: Unique identifier
- **arrival_time**: Task arrival time (float)
- **deadline**: Task deadline (float)
- Supports core heap operations: `insert`, `extract_max`, `increase_key`,`decrease_key`, all maintaining the heap property efficiently.

### Scheduler Simulation

- Randomly generates tasks with priority (1–10), arrival time (0–10 seconds), and deadline (arrival + 5–15 seconds).
- Simulation time advances according to task arrival times.
- Tasks are processed one at a time, assuming each takes exactly 1 time unit.
- Calculates wait time as the difference between task arrival and processing start time.
- Reports deadline misses to highlight scheduling performance (though no deadline enforcement yet).

## Implementation Details

### Priority Queue (priority_queue.py)

- Uses an internal list to represent a binary max-heap.
- Heapify operations (`_heapify_up` and `_heapify_down`) maintain heap property after insertions or priority updates.
- Time complexities:
  - `insert(task)`: O(log n)
  - `extract_max()`: O(log n)
  - `increase_key(task_id, new_priority)`: O(n) for lookup + O(log n) heapify
  - `decrease_key(task_id, new_priority)`: O(n) + O(log n)

### Scheduler Simulation (scheduler_simulation.py)

- Tasks generated with random priorities (1–10), arrival times (0–10 seconds), and deadlines (arrival + 5–15 seconds).
- Tasks sorted by arrival time to simulate real-time processing.
- Outputs logs for each processed task and a summary of wait times.

## Analysis of Scheduling Results

```text
Starting Scheduler Simulation...
Time 1.95: Processing Task(id=4, priority=6, arrival=1.948, deadline=16.229)
Time 2.95: Processing Task(id=1, priority=9, arrival=2.136, deadline=14.399)
Time 3.95: Processing Task(id=3, priority=8, arrival=2.649, deadline=9.188)
Time 5.08: Processing Task(id=2, priority=10, arrival=5.078, deadline=18.686)
Time 7.67: Processing Task(id=5, priority=4, arrival=7.667, deadline=13.810)

--- Simulation Summary ---
Task 4 with priority 6 waited 1.00 seconds.
Task 1 with priority 9 waited 1.81 seconds.
Task 3 with priority 8 waited 2.30 seconds.
Task 2 with priority 10 waited 1.00 seconds.
Task 5 with priority 4 waited 1.00 seconds.
```

- **Wait Times Reflect Task Arrival and Priority Interplay**: Task 4 arrived earliest (at 1.948s) and started processing almost immediately at 1.95s, resulting in minimal wait (≈1.00s). Task 1 and Task 3 arrived slightly later (2.136s and 2.649s) but had higher priorities (9 and 8 respectively). Despite arriving later, their higher priorities did not guarantee immediate processing because Task 4 was already being processed, so they waited 1.81s and 2.30s, respectively.

- **Out-of-Order Priority Processing due to Arrival Times**: Task 2 has the highest priority (10) but arrived at 5.078s, well after several other tasks started processing. It begins processing at 5.08s with only 1.00s wait since no higher priority tasks arrived before it. This shows the scheduler respects both arrival time and priority: a high priority task cannot preempt a currently processing task but will be processed as soon as it arrives if it’s the highest priority at that time.

- **Lower Priority Tasks May Experience Minimal Wait If They Arrive Late and No Higher Priority Tasks Are Waiting**: Task 5 has the lowest priority (4) but also arrives late (7.667s) and starts processing immediately, resulting in a wait time of about 1.00s.

- **Deadline Considerations Are Not Enforced Yet: Although tasks have deadlines, the simulation currently processes tasks in priority order without preempting or reordering to avoid deadline misses**. This could cause deadline misses, especially for tasks with early deadlines arriving late, suggesting a direction for future enhancements.

- **Scheduler Behavior Summary**: The scheduler effectively uses a max-heap to pick the highest priority task available at the current simulation time. However, since tasks are processed sequentially and non-preemptively, the arrival time heavily influences the actual start time of each task. This results in some lower priority tasks waiting longer if they arrive early and are overtaken by higher priority tasks that arrive shortly after.

## Time Complexity Analysis

| Operation    | Complexity      | Notes                           |
| ------------ | --------------- | ------------------------------- |
| Insert       | O(log n)        | Heap insertion                  |
| Extract Max  | O(log n)        | Remove root and heapify down    |
| Increase Key | O(n) + O(log n) | Find task (O(n)) + heapify up   |
| Decrease Key | O(n) + O(log n) | Find task (O(n)) + heapify down |
| Is Empty     | O(1)            | Check if heap list is empty     |

_Note:_ Priority update operations can be optimized to O(log n) by maintaining an auxiliary dictionary mapping task_id to heap indices, which was not implemented here for simplicity.

## Summary of Findings

- The max-heap priority queue efficiently prioritizes higher urgency tasks.
- The simulation shows how tasks with earlier arrival times and higher priority are processed earlier, minimizing wait times.
- Some tasks experience longer waits due to later arrival or lower priority, reflecting realistic scheduling delays.
- Deadline misses highlight the need for deadline-aware scheduling in future work.
- This framework is a solid foundation for exploring advanced scheduling policies and real-world constraints.
