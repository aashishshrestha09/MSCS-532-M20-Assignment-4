# scheduling_simulation.py

import random
from typing import List, Tuple
from priority_queue import PriorityQueue, Task


class SchedulerSimulation:
    """
    Simulates a scheduling system using a max-heap priority queue.

    Tasks are generated with random priorities, arrival times, and deadlines.
    The scheduler processes tasks in order of priority once they arrive,
    simulating task execution and tracking deadline misses and wait times.
    """

    def __init__(self):
        self.pq = PriorityQueue()
        self.completed_tasks: List[Tuple[Task, float]] = []

    def generate_tasks(self, num_tasks: int):
        """
        Generate random tasks with priority, arrival time, and deadline.
        """
        for i in range(1, num_tasks + 1):
            priority = random.randint(1, 10)  # Priority from 1 (low) to 10 (high)
            arrival_time = random.uniform(
                0, 10
            )  # Tasks arrive anytime in first 10 seconds
            deadline = arrival_time + random.uniform(
                5, 15
            )  # Deadline 5-15 seconds after arrival
            task = Task(
                priority=priority,
                task_id=i,
                arrival_time=arrival_time,
                deadline=deadline,
            )
            self.pq.insert(task)

    def run(self):
        """
        Run the scheduling simulation.
        Processes tasks in priority order as they arrive over time.
        """
        print("Starting Scheduler Simulation...")
        # Extract all tasks, sorted by arrival time for simulating time flow
        tasks = sorted(self.pq.heap, key=lambda t: t.arrival_time)
        self.pq.heap.clear()

        current_time = 0
        i = 0  # Index to track next task arrival

        while i < len(tasks) or not self.pq.is_empty():
            # Add all tasks that have arrived by current_time
            while i < len(tasks) and tasks[i].arrival_time <= current_time:
                self.pq.insert(tasks[i])
                i += 1

            if self.pq.is_empty():
                # If no tasks are available, jump to next arrival time
                if i < len(tasks):
                    current_time = tasks[i].arrival_time
                else:
                    break
                continue

            # Extract highest priority task and process it
            task = self.pq.extract_max()
            print(f"Time {current_time:.2f}: Processing {task}")

            # Simulate processing time of 1 unit
            current_time += 1

            # Check for deadline miss
            if current_time > task.deadline:
                print(
                    f"--> Task {task.task_id} missed its deadline at time {current_time:.2f}"
                )

            self.completed_tasks.append((task, current_time))

        self.print_summary()

    def print_summary(self):
        """
        Prints a summary of tasks and their wait times.
        """
        print("\n--- Simulation Summary ---")
        for task, completion_time in self.completed_tasks:
            wait_time = completion_time - task.arrival_time
            print(
                f"Task {task.task_id} with priority {task.priority} waited {wait_time:.2f} seconds."
            )


if __name__ == "__main__":
    sim = SchedulerSimulation()
    sim.generate_tasks(5)
    sim.run()
